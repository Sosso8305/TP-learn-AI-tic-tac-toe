import pygame,math
from .logger import logger  as log
from collections import defaultdict
from .constants import DEFAULT_BUTTON_IMAGE, DEFAULT_HOVERED_BUTTON_IMAGE, DEFAULT_FONT



############################################################################################
#                                   Button class                                           #
############################################################################################
class Button(pygame.sprite.Sprite):
    def __init__(self, game, pos, text, size, imgPath = DEFAULT_BUTTON_IMAGE  ,textScale=0.5, textLineSpacing=1, hoverMode='scale', action=None):
        super().__init__()
        self.game = game

        img = pygame.image.load(imgPath)
        if not size:
            size = img.get_rect().size

        self.size= size
        self.path= imgPath

        self.hoverMode = hoverMode

        self.isPressed = False
        self.hovered = False

        self.action = action

        self.tmpImage = pygame.transform.scale(img, size)
        game.textDisplayer.write(text,(6,0), scale=textScale, lineSpacing=textLineSpacing, rectSize=(size[0]-10, size[1]), center=True, screen=self.tmpImage)

        if self.hoverMode=='overlay':
            self.hoveredImage = self.tmpImage.copy()
            self.hoveredImage.blit(pygame.transform.scale(pygame.image.load(DEFAULT_HOVERED_BUTTON_IMAGE), size), (0,0))
        else:
            if self.hoverMode!='scale':
                log.warning(f"Unknown hover mode {self.hoverMode} for button {text}")
            self.hoveredImage = pygame.transform.scale(self.tmpImage, (size[0]+10, size[1]+10))

        self.tmpImage.set_colorkey((0,0,0))
        self.hoveredImage.set_colorkey((0,0,0))

        self.image = self.tmpImage
        self.rect = self.image.get_rect()
        self.rect.topleft = pos



    def update(self, events):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and not self.hovered:
            self.hovered = True
            if self.hoverMode=='scale':
                self.rect.inflate_ip(10, 10)
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.hovered:
            if self.hoverMode=='scale':
                self.rect.inflate_ip(-10, -10)
            self.hovered = False

        if self.hovered:
            self.image = self.hoveredImage
        else:
            self.image = self.tmpImage


        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.hovered:
                self.isPressed = True
                if self.action:
                    self.action()
        
        self.isPressed = False

    
    def isPressed(self):
        return self.isPressed

    def setAction(self, action):
        self.action = action





############################################################################################
#                                TextDisplayer class                                       #
############################################################################################


class TextDisplayer:
	def __init__(self, game, fontPath=DEFAULT_FONT, sepColor=pygame.Color(0,255,0)):
		self.game = game
		fontImg = pygame.image.load(fontPath)
		self.height = fontImg.get_height()
		self.__chars = {}

		asciiIndex = ord(' ')
		x=0; tx=0
		while x <= fontImg.get_width():
			if x==fontImg.get_width() or fontImg.get_at((x, 0)) == sepColor:
				self.__chars[chr(asciiIndex)] = pygame.Surface((tx, self.height))
				self.__chars[chr(asciiIndex)].blit(fontImg, (0,0), (x-tx, 0, tx, self.height))
				self.__chars[chr(asciiIndex)].set_colorkey((0,0,0))
				asciiIndex += 1
				tx=-1
			x+=1; tx+=1

	def convertText(self, text:str) -> str:
		""" Returns a new text where almost all accents are replaced """
		old = 'áàâäéèêëíìîïóòôöúùûüÁÀÂÄÉÈÊËÍÌÎÏÓÒÔÖÚÙÛÜ'
		new = 'aaaaeeeeiiiioooouuuuAAAAEEEEIIIIOOOOUUUU'
		for i in range(len(old)):
			text = text.replace(old[i], new[i])
		return text

	def getWidthOf(self, text, scale=1):
		""" Returns the width that the given text will take, according to
		the specified scale """
		text = self.convertText(text)
		return sum([self.__chars[c].get_width()*scale for c in text])

	def write(self, text, pos,screen, scale=1, lineSpacing=1, rectSize=(0,0), center=False, center_y=True):
		self.Yoffset=0
		text = self.convertText(text)


		if rectSize[0]:
			formattedText = defaultdict(list)

			for i, word in enumerate(text.split('\n')):
				formattedText[str(i)]+=[word]

			for i in list(formattedText.keys()):
				j=1
				# if self.getWidthOf(formattedText[i][0], scale) >= rectSize[0]:
				for word in formattedText[i][0].split(' '):
					if self.getWidthOf(' '.join(formattedText[i+'.'+str(j)]+[word]), scale) >= rectSize[0]:
						j+=1
					formattedText[i+'.'+str(j)]+=[word]
				del formattedText[i]
		else:
			formattedText = {0: [text]}
		if center_y:
			offsetY = (rectSize[1]-self.height*scale*lineSpacing*(len(formattedText)))//2
		else:
			offsetY=0
		for i in formattedText:
			offsetX = (rectSize[0]-self.getWidthOf(' '.join(formattedText[i]), scale))//2 if center else 0
			for c in ' '.join(formattedText[i]):
				if not c in self.__chars:
					c = '?'
				size = self.__chars[c].get_size()
				charImg = pygame.transform.scale(self.__chars[c], (math.floor(size[0]*scale), math.floor(size[1]*scale)))
				screen.blit(charImg, (pos[0]+offsetX, pos[1]+offsetY))
				offsetX += charImg.get_width()
			offsetY+=self.height*scale*lineSpacing
			self.Yoffset+=self.height*scale*lineSpacing	
		self.Yoffset+=self.height*scale*lineSpacing	


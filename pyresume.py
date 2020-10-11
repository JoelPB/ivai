# Exercitando o uso da bibliteca pygame
import os
import pyautogui
import pygame as game


# finaliza o pyGame
def end_():
    game.quit()


# Atualiza a janela
def update_():
    game.display.flip()


# Atualiza só a parte da janela indicada
def updatePart(rec=(0, 0, 500, 50)):
    game.display.update(rec)


# Retorna evento
def event_():
    for event in game.event.get():
        if 'key' in event.__dict__:
            return {'type': event.type, 'key': event.__dict__['key']}

        return {'type': event.type, 'key': -1}

    return {'type': -1, 'key': -1}


# retorna o evento
def getEvent():
    return game.event.get()


# carrega a imagem
def img(local='img', name='sorriso.png'):
    return game.image.load(os.path.join(local, name))


def rec100(wind, color, xy):
    game.draw.rect(wind, color, (xy[0], xy[1], 100, 100))


class PyWindow:

    def __init__(self):
        game.init()
        game.display.set_icon(game.image.load('icon1.png'))  # icone da janela
        game.display.set_caption('GAME')
        game.font.init()
        font = game.font.get_default_font()

        self.fontSys = game.font.SysFont(font, 50)
        self.texto = self.fontSys.render("Início", 1, (255, 255, 255))

        self.MOUSE = game.MOUSEBUTTONDOWN
        self.ESCAPE = game.K_ESCAPE  # Esc
        self.DOWN_T = game.KEYDOWN  # tecla pressionada
        self.A = game.K_a
        self.LEFT = game.K_LEFT
        self.S = game.K_s
        self.DOWN = game.K_DOWN
        self.D = game.K_d
        self.RIGHT = game.K_RIGHT
        self.W = game.K_w
        self.UP = game.K_UP
        self.QUIT = game.QUIT  # fecha a janela
        self.VIDEOR = game.VIDEORESIZE  # evento de maximizar a tela
        self.ACTIVE = game.ACTIVEEVENT

        self.width = (int(pyautogui.size()[0] / 2))
        self.height = (int(pyautogui.size()[1] / 2))
        self.clock = game.time.Clock()
        self.window = game.display.set_mode((self.width, self.height), game.RESIZABLE)  # main window
        self.surf = game.Surface((100, 100))  # background bloco
        self.surfMov = game.Surface((100, 100))  # background bloco
        self.surfYellow = game.Surface((100, 100))
        self.carta = game.Surface((200, 300))

    def getTexto(self):
        return self.texto

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getClock(self):
        return self.clock

    def getWindow(self):
        return self.window

    def getSurface(self):
        return self.surf

    def getSurfaceMov(self):
        return self.surfMov

    def getYellow(self):
        return self.surfYellow

    def getCarta(self):
        return self.carta

    def setTexto(self, texto):
        self.texto = self.fontSys.render(texto, 1, (255, 255, 255))

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setClock(self, quad=100):
        return self.clock.tick(quad)  # frequência de quadros

    def setWindow(self, width, height):
        self.window = game.display.set_mode((width, height), game.RESIZABLE)

    def setWindowColor(self, color=(0, 0, 0)):
        self.window.fill(color)

    def setSurface(self, width, height):
        self.surf = game.Surface((width, height))

    def setSurfaceMov(self, width, height):
        self.surfMov = game.Surface((width, height))

    def setSurfaceColor(self, color=(255, 0, 255)):
        self.surf.fill(color)

    def setSurfaceMovColor(self, color=(0, 255, 255)):
        self.surfMov.fill(color)

    def setSurfaceYellowColor(self, color=(200, 255, 0)):
        self.surfYellow.fill(color)

    def setCartaColor(self, color=(50, 55, 50)):
        self.carta.fill(color)

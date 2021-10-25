import pygame
import sys
from pygame.locals import *
from raycaster import Game

width = 1000
height = 500

background = pygame.image.load('background.jpg')


class Menu(object):

    def __init__(self):
        super().__init__()

        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Main Menu')
        self.screen = pygame.display.set_mode(
            (width, height), pygame.DOUBLEBUF | pygame.HWACCEL)
        self.screen.set_alpha(None)

        self.titleFont = pygame.font.SysFont("Arial", 60)
        self.buttonFont = pygame.font.SysFont("Arial", 40)

        self.click = False
        self.mouse_hover = False
        self.currentButton = 0

        self.start()

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_background(self):
        tex = pygame.transform.scale(background, (width, height))
        rect = tex.get_rect()
        self.screen.blit(tex, rect)

    def create_rect(self, width, height, border, color, border_color):
        surf = pygame.Surface(
            (width+border*2, height+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, color, (border, border, width, height), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i,
                                                  border-i, width+5, height+5), 1)
        return surf

    def start(self):

        while 1:

            self.screen.fill((0, 0, 0))
            self.draw_background()
            self.draw_text('Main menu', self.titleFont,
                           (255, 255, 255), self.screen, 360, 50)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(190, 250, 200, 75)
            button_2 = pygame.Rect(560, 250, 200, 75)

            button_1_is_hover = False
            button_2_is_hover = False

            if button_1.collidepoint((mx, my)):
                if self.click:
                    Game(self.screen, self.mainClock, width, height)

                elif self.mouse_hover:
                    button_1_is_hover = True

            if button_2.collidepoint((mx, my)):
                if self.click:
                    pygame.quit()
                    sys.exit()
                elif self.mouse_hover:
                    button_2_is_hover = True

            button_color = (255, 255, 255)
            button_color_hover = (200, 200, 200)

            button_1_color = button_color if button_1_is_hover or self.currentButton == 0 else button_color_hover
            button_2_color = button_color if button_2_is_hover or self.currentButton == 1 else button_color_hover

            # Start button
            pygame.draw.rect(self.screen, button_1_color,
                             button_1,  border_radius=10)
            self.draw_text('Start', self.buttonFont,
                           (0, 0, 0), self.screen, 250, 265)

            # Exit button
            pygame.draw.rect(self.screen, button_2_color,
                             button_2,  border_radius=10)
            self.draw_text('Exit', self.buttonFont,
                           (0, 0, 0), self.screen, 630, 265)

            self.click = False
            self.mouse_hover = False

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:

                    if event.key == K_RIGHT:
                        self.currentButton = 1
                    elif event.key == K_LEFT:
                        self.currentButton = 0
                    elif event.key == K_RETURN or event.key == K_KP_ENTER:
                        if self.currentButton == 0:
                            Game(self.screen, self.mainClock, width, height)
                        else:
                            pygame.quit()
                            sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                elif event.type == MOUSEMOTION:
                    self.mouse_hover = True

            pygame.display.update()
            self.mainClock.tick(60)

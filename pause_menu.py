import pygame
import sys
from pygame.locals import *
from map_textures import *

width = 500
height = 500

background = pygame.image.load('./pause_background.jpg')


class PauseMenu(object):

    def __init__(self, screen, clock):
        super().__init__()

        self.mainClock = clock
        self.screen = screen
        self.buttonFont = pygame.font.SysFont("Arial", 40)
        self.click = False
        self.mouse_hover = False
        self.currentButton = 0


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

        #play music
        pygame.mixer.music.load('./audios/pause.mp3')
        pygame.mixer.music.play(-1)

        
        while 1:

            self.screen.fill((0, 0, 0))
            self.draw_background()

            mx, my = pygame.mouse.get_pos()

            # Buttons
            button_level_1 = pygame.Rect(80, 300, 150, 75)  # Level 1 Button
            button_level_2 = pygame.Rect(270, 300, 150, 75)  # Level 2 Button

            button_level_1_is_hover = False
            button_level_2_is_hover = False

            if button_level_1.collidepoint((mx, my)):  # Nivel 1
                if self.click:
                    pygame.mixer.music.stop()
                    return 0

                elif self.mouse_hover:
                    button_level_1_is_hover = True

            if button_level_2.collidepoint((mx, my)):  # Nivel 2
                if self.click:
                    pygame.mixer.music.stop()
                    return 1

                elif self.mouse_hover:
                    button_level_1_is_hover = True

            button_color = (255, 255, 255)
            button_color_hover = (200, 200, 200)

            button_level_1_color = button_color if button_level_1_is_hover or self.currentButton == 0 else button_color_hover
            button_level_2_color = button_color if button_level_2_is_hover or self.currentButton == 1 else button_color_hover

            #  Button
            pygame.draw.rect(self.screen, button_level_1_color,
                             button_level_1,  border_radius=10)
            self.draw_text('Resumir', self.buttonFont,(0, 0, 0), self.screen, 90, 320)

            # 2 Button
            pygame.draw.rect(self.screen, button_level_2_color, button_level_2,  border_radius=10)
            self.draw_text('Menu', self.buttonFont, (0, 0, 0), self.screen, 300, 320)

            self.click = False
            self.mouse_hover = False

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:

                    if event.key == K_RIGHT:
                        self.currentButton = (self.currentButton + 1) % 2
                    elif event.key == K_LEFT:
                        self.currentButton = (self.currentButton - 1) % 2

                    elif event.key == K_RETURN or event.key == K_KP_ENTER:
                        if self.currentButton == 0:
                            return 0
                        elif self.currentButton == 1:
                            return 1


                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                elif event.type == MOUSEMOTION:
                    self.mouse_hover = True

            pygame.display.update()
            self.mainClock.tick(60)
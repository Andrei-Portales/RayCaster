import pygame
import sys
from pygame.locals import *
from raycaster import Game
from map_textures import *

width = 500
height = 500

background = pygame.image.load('background.jpg')


class Menu(object):

    def __init__(self):
        super().__init__()

        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Andrei Portales 19825')
        self.screen = pygame.display.set_mode(
            (width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
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

    def play_music(self):
        pygame.mixer.music.load('audios/menu.mp3')
        pygame.mixer.music.play(-1)

    def start(self):
        
        self.play_music()

        while 1:

            self.screen.fill((0, 0, 0))
            self.draw_background()
            self.draw_text('Main menu', self.titleFont,(255, 255, 255), self.screen, 150, 50)

            mx, my = pygame.mouse.get_pos()

            # Buttons
            button_level_1 = pygame.Rect(15, 250, 150, 75)  # Level 1 Button
            button_level_2 = pygame.Rect(175, 250, 150, 75)  # Level 2 Button
            button_level_3 = pygame.Rect(335, 250, 150, 75)  # Level 3 Button
            button_exit = pygame.Rect(170, 375, 150, 75)  # Exit button

            button_level_1_is_hover = False
            button_level_2_is_hover = False
            button_level_3_is_hover = False
            button_exit_is_hover = False

            if button_level_1.collidepoint((mx, my)):  # Nivel 1
                if self.click:
                    pygame.mixer.music.stop()
                    Game(self.screen, self.mainClock, width,
                         height, 'maps/map.txt', map_textures1, 'audios/nivel1.mp3')
                    self.play_music()

                elif self.mouse_hover:
                    button_level_1_is_hover = True

            if button_level_2.collidepoint((mx, my)):  # Nivel 2
                if self.click:
                    pygame.mixer.music.stop()
                    Game(self.screen, self.mainClock, width,
                         height, 'maps/map1.txt', map_textures2, 'audios/nivel2.mp3')
                    self.play_music()

                elif self.mouse_hover:
                    button_level_1_is_hover = True

            if button_level_3.collidepoint((mx, my)):  # Nivel 3
                if self.click:
                    pygame.mixer.music.stop()
                    Game(self.screen, self.mainClock, width, height, 'maps/map2.txt', map_textures3, 'audios/nivel3.mp3')
                    self.play_music()

                elif self.mouse_hover:
                    button_level_1_is_hover = True

            if button_exit.collidepoint((mx, my)):
                if self.click:
                    pygame.quit()
                    sys.exit()
                elif self.mouse_hover:
                    button_exit_is_hover = True

            button_color = (255, 255, 255)
            button_color_hover = (200, 200, 200)

            button_level_1_color = button_color if button_level_1_is_hover or self.currentButton == 0 else button_color_hover
            button_level_2_color = button_color if button_level_2_is_hover or self.currentButton == 1 else button_color_hover
            button_level_3_color = button_color if button_level_3_is_hover or self.currentButton == 2 else button_color_hover
            button_exit_color = button_color if button_exit_is_hover or self.currentButton == 3 else button_color_hover

            # Nivel 1 Button
            pygame.draw.rect(self.screen, button_level_1_color,
                             button_level_1,  border_radius=10)
            self.draw_text('Nivel 1', self.buttonFont,
                           (0, 0, 0), self.screen, 45, 265)

            # Nivel 2 Button
            pygame.draw.rect(self.screen, button_level_2_color,
                             button_level_2,  border_radius=10)
            self.draw_text('Nivel 2', self.buttonFont,
                           (0, 0, 0), self.screen, 200, 265)

            # Nivel 3 Button
            pygame.draw.rect(self.screen, button_level_3_color,
                             button_level_3,  border_radius=10)
            self.draw_text('Nivel 3', self.buttonFont,
                           (0, 0, 0), self.screen, 365, 265)

            # Exit button
            pygame.draw.rect(self.screen, button_exit_color,
                             button_exit,  border_radius=10)
            self.draw_text('Exit', self.buttonFont,
                           (0, 0, 0), self.screen, 215, 390)

            self.click = False
            self.mouse_hover = False

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:

                    if event.key == K_RIGHT:
                        self.currentButton = (self.currentButton + 1) % 4
                    elif event.key == K_LEFT:
                        self.currentButton = (self.currentButton - 1) % 4

                    elif event.key == K_RETURN or event.key == K_KP_ENTER:
                        if self.currentButton == 0:
                            Game(self.screen, self.mainClock, width,
                         height, 'maps/map.txt', map_textures1, 'audios/nivel1.mp3')
                        elif self.currentButton == 1:
                            Game(self.screen, self.mainClock, width,
                            height, 'maps/map1.txt', map_textures2, 'audios/nivel2.mp3')
                        elif self.currentButton == 2:
                            Game(self.screen, self.mainClock, width, height, 'maps/map2.txt', map_textures3, 'audios/nivel2.mp3')
                        elif self.currentButton == 3:
                            pygame.quit()
                            sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                elif event.type == MOUSEMOTION:
                    self.mouse_hover = True

            pygame.display.update()
            self.mainClock.tick(80)


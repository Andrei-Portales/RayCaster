import pygame

from math import cos, sin, pi

RAY_AMOUNT = 100

wallTextures = {
    '1': pygame.image.load('textures/wall.jpg'),
    '2': pygame.image.load('textures/obsidean.jpg'),
    '3': pygame.image.load('textures/window.png'),
    '4': pygame.image.load('textures/pumpkin.jpg'),
}


class Raycaster(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        self.map = []
        self.blocksize = 50
        self.wallheight = 50

        self.maxdistance = 300

        self.stepSize = 5
        self.turnSize = 5

        self.state = {
            'x': -1,
            'y': -1,
            'fov': -1,
            'angle': -1
        }

        self.player = {
            'x': 200,
            'y': 175,
            'fov': 60,
            'angle': 180
        }

    def load_map(self, filename):
        with open(filename) as file:
            for line in file.readlines():
                self.map.append(list(line.rstrip()))

    def compareStates(self):
        return self.player['x'] == self.state['x'] and \
            self.player['y'] == self.state['y'] and \
            self.player['fov'] == self.state['fov'] and \
            self.player['angle'] == self.state['angle']

    def drawBlock(self, x, y, id):
        tex = wallTextures[id]
        tex = pygame.transform.scale(tex, (self.blocksize, self.blocksize))
        rect = tex.get_rect()
        rect = rect.move((x, y))
        self.screen.blit(tex, rect)

    def drawPlayerIcon(self, color):
        if self.player['x'] < self.width / 2:
            rect = (self.player['x'] - 2, self.player['y'] - 2, 5, 5)
            self.screen.fill(color, rect)

    def castRay(self, angle):
        rads = angle * pi / 180
        dist = 0
        stepSize = 1
        stepX = stepSize * cos(rads)
        stepY = stepSize * sin(rads)

        playerPos = (self.player['x'], self.player['y'])

        x = playerPos[0]
        y = playerPos[1]

        while 1:
            dist += stepSize

            x += stepX
            y += stepY

            i = int(x/self.blocksize)
            j = int(y/self.blocksize)

            if j < len(self.map):
                if i < len(self.map[j]):
                    if self.map[j][i] != ' ':

                        hitX = x - i*self.blocksize
                        hitY = y - j*self.blocksize

                        hit = 0

                        if 1 < hitX < self.blocksize-1:
                            if hitY < 1:
                                hit = self.blocksize - hitX
                            elif hitY >= self.blocksize-1:
                                hit = hitX
                        elif 1 < hitY < self.blocksize-1:
                            if hitX < 1:
                                hit = hitY
                            elif hitX >= self.blocksize-1:
                                hit = self.blocksize - hitY

                        tx = hit / self.blocksize

                        pygame.draw.line(self.screen, pygame.Color(
                            'white'), playerPos, (x, y))
                        return dist, self.map[j][i], tx

    def render(self):

        halfWidth = int(self.width / 2)
        halfHeight = int(self.height / 2)

        for x in range(0, halfWidth, self.blocksize):
            for y in range(0, self.height, self.blocksize):

                i = int(x/self.blocksize)
                j = int(y/self.blocksize)

                if j < len(self.map):
                    if i < len(self.map[j]):
                        if self.map[j][i] != ' ':
                            self.drawBlock(x, y, self.map[j][i])

        self.drawPlayerIcon(pygame.Color('black'))


        for column in range(RAY_AMOUNT):
            angle = self.player['angle'] - (self.player['fov'] / 2) + \
                (self.player['fov'] * column / RAY_AMOUNT)
            dist, id, tx = self.castRay(angle)

            rayWidth = int((1 / RAY_AMOUNT) * halfWidth)

            startX = halfWidth + int(((column / RAY_AMOUNT) * halfWidth))

            h = self.height / \
                (dist *
                 cos((angle - self.player["angle"]) * pi / 180)) * self.wallheight
            startY = int(halfHeight - h/2)
            endY = int(halfHeight + h/2)

            color_k = (1 - min(1, dist / self.maxdistance)) * 255

            tex = wallTextures[id]
            tex = pygame.transform.scale(
                tex, (tex.get_width() * rayWidth, int(h)))
            tex.fill((color_k, color_k, color_k),
                     special_flags=pygame.BLEND_MULT)
            tx = int(tx * tex.get_width())

            self.screen.blit(tex, (startX, startY),
                             (tx, 0, rayWidth, tex.get_height()))

        # Columna divisora
        for i in range(self.height):
            self.screen.set_at((halfWidth, i), pygame.Color('black'))
            self.screen.set_at((halfWidth+1, i), pygame.Color('black'))
            self.screen.set_at((halfWidth-1, i), pygame.Color('black'))
            

        self.state = {**self.player}


class Game(object):

    def __init__(self, screen, clock, width, height):
        super().__init__()

        self.screen = screen
        self.clock = clock
        self.width = width
        self.height = height

        self.rCaster = Raycaster(screen)
        self.rCaster.load_map("map.txt")
        self.font = pygame.font.SysFont("Arial", 25)

        self.start()


    def updateFPS(self):
        fps = str(int(self.clock.get_fps()))
        fps = self.font.render(fps, 1, pygame.Color("white"))
        return fps

    def start(self):

        isRunning = True
        while isRunning:

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    isRunning = False

                elif ev.type == pygame.KEYDOWN:
                    newX = self.rCaster.player['x']
                    newY = self.rCaster.player['y']
                    forward = self.rCaster.player['angle'] * pi / 180
                    right = (self.rCaster.player['angle'] + 90) * pi / 180

                    if ev.key == pygame.K_ESCAPE:
                        isRunning = False
                    elif ev.key == pygame.K_w:
                        newX += cos(forward) * self.rCaster.stepSize
                        newY += sin(forward) * self.rCaster.stepSize
                    elif ev.key == pygame.K_s:
                        newX -= cos(forward) * self.rCaster.stepSize
                        newY -= sin(forward) * self.rCaster.stepSize
                    elif ev.key == pygame.K_a:
                        newX -= cos(right) * self.rCaster.stepSize
                        newY -= sin(right) * self.rCaster.stepSize
                    elif ev.key == pygame.K_d:
                        newX += cos(right) * self.rCaster.stepSize
                        newY += sin(right) * self.rCaster.stepSize
                    elif ev.key == pygame.K_q:
                        self.rCaster.player['angle'] -= self.rCaster.turnSize
                    elif ev.key == pygame.K_e:
                        self.rCaster.player['angle'] += self.rCaster.turnSize

                    i = int(newX/self.rCaster.blocksize)
                    j = int(newY/self.rCaster.blocksize)

                    if self.rCaster.map[j][i] == ' ':
                        self.rCaster.player['x'] = newX
                        self.rCaster.player['y'] = newY


            if not self.rCaster.compareStates():
 
                self.screen.fill(pygame.Color("gray"))

                # Techo
                self.screen.fill(pygame.Color("saddlebrown"),(int(self.width / 2), 0,  int(self.width / 2), int(self.height / 2)))

                # Piso
                self.screen.fill(pygame.Color("dimgray"), (int(self.width / 2), int(self.height / 2),  int(self.width / 2), int(self.height / 2)))

                self.rCaster.render()

            # FPS
            self.screen.fill(pygame.Color("black"), (0, 0, 40, 30))
            self.screen.blit(self.updateFPS(), (0, 0))

            pygame.display.update()
            self.clock.tick(60)


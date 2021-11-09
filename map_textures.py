import pygame

map_textures1 = {
    'enemies': [
        {
            "x": 100,
            "y": 200,
            "sprite": pygame.image.load('sprites/sprite1.png')
        },

        {
            "x": 350,
            "y": 200,
            "sprite": pygame.image.load('sprites/sprite2.png')
        },

        {
            "x": 350,
            "y": 75,
            "sprite": pygame.image.load('sprites/sprite4.png')
        },

        {
            "x": 300,
            "y": 420,
            "sprite": pygame.image.load('sprites/sprite3.png')
        }

    ],
    'walls': {
        '1': pygame.image.load('textures/wall.jpg'),
        '2': pygame.image.load('textures/obsidean.jpg'),
        '3': pygame.image.load('textures/window.png'),
        '4': pygame.image.load('textures/pumpkin.jpg'),
        '5': pygame.image.load('textures/leaf.jpg'),
    }}

map_textures2 = {
    'enemies': [
        {
            "x": 75,
            "y": 200,
            "sprite": pygame.image.load('sprites/creeper.png')
        },

        {
            "x": 415,
            "y": 200,
            "sprite": pygame.image.load('sprites/creeper.png')
        },

        {
            "x": 250,
            "y": 75,
            "sprite": pygame.image.load('sprites/creeper.png')
        },
        {
            "x": 250,
            "y": 415,
            "sprite": pygame.image.load('sprites/creeper.png')
        },

        {
            "x": 250,
            "y": 300,
            "sprite": pygame.image.load('sprites/creeper.png')
        },

    ],
    'walls': {
        '1': pygame.image.load('textures/wall.jpg'),
        '2': pygame.image.load('textures/lava.jpg'),
    }}


map_textures3 = {
    'enemies': [
        {
            "x": 250,
            "y": 300,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },
         {
            "x": 250,
            "y": 100,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },
         {
            "x": 150,
            "y": 400,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },
         {
            "x": 75,
            "y": 300,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },
         {
            "x": 300,
            "y": 300,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },

         {
            "x": 300,
            "y": 100,
            "sprite": pygame.image.load('sprites/zoombie.png')
        },
    ],
    'walls': {
        '1': pygame.image.load('textures/sand.png'),
    }
}

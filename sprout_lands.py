import pgzrun
from pgzhelper import *

WIDTH = 960
HEIGHT = 640

bg = Actor('map')
bg.scale = 2
bg.pos = (WIDTH/2, HEIGHT/2)

player_down = [
    'player/tile000',
    'player/tile001',
    'player/tile002',
    'player/tile003',
]

player_up = [
    'player/tile004',
    'player/tile005',
    'player/tile006',
    'player/tile007',
]

player_left = [
    'player/tile008',
    'player/tile009',
    'player/tile010',
    'player/tile011',
]

player_right = [
    'player/tile012',
    'player/tile013',
    'player/tile014',
    'player/tile015',
]

player = Actor(player_down[0])
player.pos = (WIDTH/2, HEIGHT/2)
player.images = player_down
player.scale = 3

def update():
    player.animate()
    if keyboard.UP:
        player.y -=5
        player.images = player_up
    if keyboard.DOWN:
        player.y +=5
        player.images = player_down
    if keyboard.LEFT:
        player.x -=5
        player.images = player_right
    if keyboard.RIGHT:
        player.x +=5
        player.images = player_right

    if player.top <0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.left <0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH



def draw():
    screen.clear()
    bg.draw()
    player.draw()


pgzrun.go()
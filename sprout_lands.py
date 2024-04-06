import random
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
player.score = 0

chicken_img = [
    'chicken/tile000',
    'chicken/tile001',
    'chicken/tile004',
    'chicken/tile005',
    'chicken/tile006',
    'chicken/tile007',
]

chicken_list = []


def update():
    player.animate()
    if keyboard.UP:
        player.y -=6
        if player.images !=player_up:
            player.images = player_up
    if keyboard.DOWN:
        player.y +=5
        if player.images !=player_down:
            player.images = player_down
    if keyboard.LEFT:
        player.x -=5
        if player.images !=player_left:
            player.images = player_left
    if keyboard.RIGHT:
        player.x +=5
        if player.images !=player_right:
            player.images = player_right


    if player.top <0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.left <0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    if random.randint(0,100)<2:
        chicken = Actor(chicken_img[0])
        chicken.images = chicken_img
        chicken.scale = 3
        chicken.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
        chicken_list.append(chicken)

    for c in chicken_list:
        c.animate()
        if player.collide_pixel(c):
            player.score += 1
            sounds.coin.play() 
            chicken_list.remove(c) 
            break


def draw():
    screen.clear()
    bg.draw()
    screen.draw.text(str(player.score), center=(WIDTH/2, HEIGHT/2), fontsize=300)
    for c in chicken_list:
        c.draw()
    player.draw()


pgzrun.go()

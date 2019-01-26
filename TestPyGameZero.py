import pgzero

WIDTH = HEIGHT = 600


def draw():
    pgzero.screen.clear()
    pgzero.screen.draw.circle((400, 300), 30, 'white')


draw()

#pgzero.pgzrun.go()
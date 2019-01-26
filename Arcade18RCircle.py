import arcade
import math
import random

xFlyt = 400
yFlyt = 300
radius = 10
rotationRadius1 = 200
rotationRadius2 = 30
vinkelRadians1 = 0
vinkelRadians2 = 0

red = 255
green = 255
blue = 255


arcade.open_window(1200, 600, "Mirsads vindue")
#arcade.set_background_color((255,255,255))
arcade.start_render()

while True:

    xPoss = rotationRadius1 * math.cos(vinkelRadians1) + xFlyt + rotationRadius2 * math.cos(vinkelRadians2)
    yPoss = rotationRadius1 * math.sin(vinkelRadians1) + yFlyt + rotationRadius2 * math.sin(vinkelRadians2)

    arcade.draw_circle_filled(xPoss, yPoss, radius, (red,green,blue))

    vinkelRadians1 = vinkelRadians1 + 0.005
    vinkelRadians2 = vinkelRadians2 - 0.1

    xFlyt = xFlyt + 0.02


    if (vinkelRadians1 > 2 *math.pi):
        vinkelRadians1 = 0
        red = random.randint(0,255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)



    arcade.finish_render()


arcade.run()


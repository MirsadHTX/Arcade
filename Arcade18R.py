import arcade
import random
radius = 20

arcade.open_window(600, 600, "Mirsads vindue")
arcade.set_background_color((255,0,0))


arcade.start_render()
for y in range(25,600,60):
    for x in range(25,600,60):
        red = random.randint(0,255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        arcade.draw_circle_filled(x, y, radius, (red,green,blue))

arcade.finish_render()


arcade.run()






#arcade.open_window(1600, 600, "Mirsads vindue")
#arcade.start_render()
#arcade.draw_circle_outline(50, 50, 50, (0,0,255))

#arcade.finish_render()

#arcade.run()
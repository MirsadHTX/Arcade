import arcade
x = 0
y = 300
radius = 20
speed = 1
acc = 0.03

arcade.open_window(1200, 600, "Mirsads vindue")
arcade.set_background_color((255,255,255))

while True:
    arcade.start_render()

    arcade.draw_circle_filled(x, y, radius, (0,255,0))

    x = x + speed

    speed  = speed + acc

    if (x > 600):
        print("før " + str(speed))
        speed = speed * (-0.8)
        print("effter " + str(speed))


    arcade.finish_render()


arcade.run()


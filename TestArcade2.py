import arcade

arcade.open_window(600, 600, "Mirsads vindue")
x = 0
arcade.start_render()
while True:

    #arcade.start_render()
    arcade.draw_circle_outline(x, 200, 10, (0,0,255))
    x = x + 5
    arcade.finish_render()




#arcade.run()
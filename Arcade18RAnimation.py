import arcade
x = 300
y = 300
radius = 20


arcade.open_window(600, 600, "Mirsads vindue")
arcade.set_background_color((255,255,255))

arcade.start_render()

arcade.draw_circle_filled(x, y, radius, (0,255,0))


arcade.finish_render()


arcade.run()





















#while True:
#    arcade.start_render()

#    arcade.draw_circle_filled(x, y, radius, (0,255,0))

#    minBillede = arcade.load_texture("../ZZPicturesFiles/trekant.png")


#    arcade.draw_texture_rectangle(300, 300, scale * minBillede.width,scale * minBillede.height, minBillede, vinkel)

#    x = x + 5
#    vinkel = vinkel - 1
#    scale = scale - 0.001

#    arcade.finish_render()
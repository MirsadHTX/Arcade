import arcade

x = int(input("x "))
y = int(input("y "))

arcade.open_window(600, 600,"Moj Prozor")


arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()



arcade.draw_circle_filled(x, y, 50, (0,0,255))


arcade.finish_render()

arcade.run()
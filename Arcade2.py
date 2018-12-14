import arcade

arcade.open_window(600, 600, "Drawing Example")


arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

arcade.draw_text("draw_point", 30, 405, arcade.color.BLACK, 50)
arcade.draw_point(60, 495, arcade.color.RED, 10)
arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 3)
arcade.draw_circle_outline(300, 285, 18, arcade.color.WISTERIA, 3)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

arcade.draw_rectangle_outline(295, 100, 45, 65, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_rectangle_outline(295, 160, 20, 45, arcade.color.BRITISH_RACING_GREEN, 8, 80)
arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)

arcade.finish_render()

arcade.run()

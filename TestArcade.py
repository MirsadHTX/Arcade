import arcade


def draw_pine_tree(x, y):
    """ This function draws a pine tree at the specified location. """

    # Draw the triangle on top of the trunk.
    # We need three x, y points for the triangle.
    arcade.draw_triangle_filled(x + 40, y,  # Point 1
                                x, y - 100,  # Point 2
                                x + 80, y - 100,  # Point 3
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)
x = 200
y = 100

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color((0,255,0))

arcade.start_render()


arcade.draw_circle_outline(x, y, 20, arcade.color.WISTERIA, 1)
draw_pine_tree(20, 300)
draw_pine_tree(200, 120)
#draw_pine_tree(20, 80)
#draw_pine_tree(20, 100)



arcade.finish_render()
arcade.run()
import arcade
import random

high = 600
width = 600

xPos = width / 2
yPos = high / 2
radius = 15

arcade.open_window(high, width, "Drawing Example")
arcade.set_background_color(arcade.color.DEEP_JUNGLE_GREEN)

while True:
    xSpeedVector = random.randint(-3, 3)
    ySpeedVector = random.randint(-3, 3)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    arcade.draw_circle_filled(xPos, yPos, radius, arcade.color.RED_DEVIL)

    xPos = xPos + xSpeedVector
    yPos = yPos + ySpeedVector

    arcade.finish_render()

arcade.run()

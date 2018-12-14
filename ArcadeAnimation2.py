import arcade
import random





def on_draw(delta_time):

    global x
    x = random.randint(0, 600)
    y = random.randint(0,600)
    radius = random.randint(5,80)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    arcade.start_render()

    arcade.draw_circle_filled(x, y, radius, (red,green,blue))


def main():
    # Open up our window
    arcade.open_window(600, 600, "Mirsad Window")
    arcade.set_background_color((0,0,0))

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 1)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()
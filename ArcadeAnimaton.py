
import arcade


x = 200
y = 300


def on_draw(delta_time):

    global x
    x = x + 1

    arcade.start_render()

    arcade.draw_circle_filled(x, y, 10, (255,0,0))




def main():
    # Open up our window
    arcade.open_window(600, 600, "Mirsad Window")
    arcade.set_background_color((0,0,0))

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 100)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()

import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50


speedX = 8
speedY = 8

def on_draw(delta_time):

    arcade.start_render()


    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,RECT_WIDTH, RECT_HEIGHT,arcade.color.ALIZARIN_CRIMSON)

    positionX = positionX + speedX
    on_draw.center_y = on_draw.center_y + on_draw.speedY

    # Figure out if we hit the edge and need to reverse.
    if on_draw.center_x < RECT_WIDTH // 2 \
            or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
        on_draw.speedX *= -1
    if on_draw.center_y < RECT_HEIGHT // 2 \
            or on_draw.center_y > SCREEN_HEIGHT - RECT_HEIGHT // 2:
        on_draw.speedY *= -1




def main():
    positionX = 100
    positionY = 50
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Rectangle Example")
    arcade.set_background_color((0,255,0))

    arcade.schedule(on_draw, 1 / 50)

    arcade.run()


if __name__ == "__main__":
    main()
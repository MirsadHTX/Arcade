import arcade

y = int(input("Indtast Y  "))

arcade.open_window(600, 600, "Mirsads vindue")


arcade.start_render()



arcade.draw_circle_outline(100, y, 10, (0,0,255))
arcade.draw_triangle_outline(20,30,60,180,200,300,(0,0,255))
for x in range(0,600,30):
    arcade.draw_circle_filled(x,400,20,(255,0,0))



arcade.finish_render()
arcade.run()
#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 1500              #width of the window
SCREEN_HEIGHT = 800              #height of the window
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3       #movement speed of the ball


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them. 
        self.position_x = position_x            #these are all of the variables for the ball
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #draws the ball using the variables we have entered

    def update(self):
        # Move the ball
        self.position_y += self.change_y      #So both of these allows the ball to move     
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius: #position is less than radius so i assume this prevents the ball from going offscreen or something.
            self.position_x = self.radius #this as well

        if self.position_x > SCREEN_WIDTH - self.radius:    #I understand that this section of the code deals with the ball hitting the edged, but I don't quite fully understand the code
            self.position_x = SCREEN_WIDTH - self.radius      #(Above)

        if self.position_y < self.radius:     #(Above)
            self.position_y = self.radius     #(Above)

        if self.position_y > SCREEN_HEIGHT - self.radius:      #(Above)
            self.position_y = SCREEN_HEIGHT - self.radius      #(Above)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #background color

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN) #creates the ball

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()               #deals with the ball

    def update(self, delta_time):        #updates ball
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED #hitting left arrow makes ball move left
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED #hitting right arrow makes ball move right
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED #hitting up arrow makes ball move up
            
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED ##hitting down arrow makes ball move down 

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT: #moving left or right affects the ball horizontally (x)
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN: #moving up or down affects the ball vertically (y)
            self.ball.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #window = the name of the game
    arcade.run() #allows it to run


if __name__ == "__main__":
    main()
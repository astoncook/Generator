import random
import arcade
import math
import os

from arcade.color import BLACK, WHITE

#constants
SPRITE_SCALING_PLAYER = .60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Quiz"

SPRITE_SPEED = 0.20

MOVEMENT_SPEED = 5

class PLAYER(arcade.Sprite):

    def __init__(self, image, scale):
        super().__init__(image, scale)

    def update(self):
        """ Move the player """
        # Move player around the screen

        self.center_x += self.change_x
        self.center_y += self.change_y
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
    # Make sure he cant go off the screen
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        start_x = 255
        start_y = 370
        arcade.draw_text("Python Quiz", start_x, start_y, arcade.color.WHITE, 50)

        self.player_sprite = PLAYER(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png", SPRITE_SCALING_PLAYER)

        start_x = 200
        start_y = 270
        arcade.draw_text("Use the arrow keys on your keyboard to move around", start_x, start_y, arcade.color.RED, 15)
        
        start_x = 310
        start_y = 240
        arcade.draw_text("Use your mouse to aim", start_x, start_y, arcade.color.RED, 15)

        start_x = 340
        start_y = 210
        arcade.draw_text("Click to Shoot", start_x, start_y, arcade.color.RED, 15)

        start_x = 330
        start_y = 110
        arcade.draw_text("Click to start", start_x, start_y, arcade.color.WHITE, 20)
        arcade.draw_rectangle_outline(center_x=395, center_y=123, width=200, height=50, color=WHITE)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)
        arcade.run()

class GameOverView(arcade.View):
    """ Class to manage the game over view """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over!\n", SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5,
                         arcade.color.RED, 100, anchor_x="center")

        start_x = 290
        start_y = 270
        arcade.draw_text(f"Your score was: ", start_x, start_y, arcade.color.RED, 20)


        arcade.draw_text("Click ESCAPE to return to Main Menu.\n", SCREEN_WIDTH/2, SCREEN_HEIGHT/4,
                         arcade.color.WHITE, 25, anchor_x="center")
                

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class MyGame(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        super().__init__()


        # Variables that will hold sprite lists
        self.player_list = None
        

        # Set up the player
        self.player_sprite = None
        self.good = True
        self.speed = SPRITE_SPEED

        # Game Sounds

        self.left_pressed = False
        self.right_pressed = False

        self.width = SCREEN_WIDTH

        # Background image will be stored in this variable
        self.background = None

    def setup(self):
        
        # Set up the game

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.player_sprite = PLAYER(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # Set the background color

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
    
    def on_draw(self):
        # render the screen befroe start drawing
        arcade.start_render()

        # Draw all the sprites
        self.player_list.draw()
    
    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        self.player_list.update()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Python Quiz")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
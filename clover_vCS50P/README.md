# CLOVER
#### [Video Demo](https://youtu.be/QoN3dDK799c)
## What is Clover?
Clover is a video game in Python that has been created from scratch by a person knowing nothing about code and that has been learning Python with CS50P.
### The game
In Clover, you can click on pots and randomly generate three-leaf and four-leaf clovers in a satisfying way thanks to the cute animated sprite and various 'pop' sound effects.
## How is it made?
### Pygame
[Pygame](https://www.pygame.org/docs/ref/mixer.html) is a well known Python library for creating video games. It allows to manage graphics, user inputs, sprites, sounds and lots of different convinient things for video game programming.
### Project framework
#### Focus on OOP
The main file `project.py` is structured around one `main` function and the two following classes:
- The **Clover** class is a subclass of a pygame Sprite class (learn more in the [pygame documentation](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)). A Sprite object must have a position (rect) and a surface (image) as attributes.

The **Clover** class contains and manages everything needed to generate clovers in the game and takes two arguments : a **position** (an (x,y) tuple) and a **droprate** (an int).

Its `__init__` method determines the spritesheet of the clover: *a horizontal 336x60px png sheet* of six successive images representing the growing animation and the final state of a grown clover. It can be any type of clover we want *as long as its spritesheet is made of six 56x60px png images arranged horizontally*.
\
The **droprate** variable determines the type of the clover: three-leaf or four-leaf, and the **type** variable determines which spritesheet will be used. For that to work, *every spritesheet file name must follow this specific format* : '{type}_leaf_sheet_56_60.png'.
\
The **position** variable is a tuple used to create the variable **rect**: a pygame **Rect** object that determines the position of the clover in the game screen. See `generate_clover` in the **Game** class to learn how a Clover object is created in the game.

`update` is a method of the **Sprite** class used in the **Clover** class to update the sprite of a clover at every game loop iteration. The **index** variable is used to stop the animation of the clover when it reaches its final image (for a clover, it is its 6th image).

`get_image` uses pygame's **blit** method to paste sections of the spritesheet on an empty pygame **Surface** object and returns the image as a **Surface** object. It takes the **x, y** coordinates of the top-left corner pixel of the sprite in the spritesheet as an argument.

- The **Game** class - contains the game variables, loop and main mechanics.

A lot of the setup is done in the **Game** class `__init__` method (setting up the screen size, loading graphics and sounds, creating sprite groups and rectangle objects for the background...), whereas the events of the game are managed in its `launch` method.

`generate_clover` takes a position (an (x,y) tuple) as an argument to create a **Clover** object from this position.
It first generates a random **droprate** variable between 0 and 100 in order to determine which type of clover will be created, according to the drop rate fixed in the **Clover** class.
Then, while creating the Clover object, it adjusts the clover display position on the screen to fit the graphic element representing the stem of the clover sprite (+10). This design choice allows to create sprites with different stem positions.
It then adds the created clover object to its defined group called `clover_group`. **Group** is a pygame container class used in `project.py` for displaying an entire group of sprites at the same time with pygame's `draw` method.
Finally it sets the **clovers** boolean to `True`, meaning at least one clover has been created and now can be displayed at the end of the game loop (`draw` method).

`play_pop_sound` generates a random number between 0 and 2 and plays a sound chosen between the three possible 'pop' sound effects in the 3 elements list containing the sound library of the game.
Then it sets the **clover.pop** boolean attribute to `True` so the sound is played only one time per created clover.

`launch` contains the logic of the game loop. 1 loop = 1 frame and the framerate has been set at 60fps in `__init__` with the **clock**.
If an event of type `MOUSEBUTTONDOWN` is detected on a pot, a clover animation will be generated along with a 'pop' sound.

- Last but not least, the `main` function creates a **Game** object and executes its `launch` method!

The game can now be played.
## Test file
## Possible improvements
- Sprites : The `get_image` function could be improved to manage any type of spritesheets. It currently can only manage 366x60px pngs with exactly 6 sprites. It would be great to add the possibility to give more arguments to the function depending on the type of the spritesheet.
- Collisions : The `generate_clover` function could be improved by keeping in memory sprites positions and making impossible to generate 2 clovers in the same position, using maybe `pygame.spritecollide`
- Error handeling : there's... just none !
- Fancier graphics
- More game features

### The already envisaged future of Clover
This little program is only a start for Clover which hopefully has a lot of features to come, such as different sizes of pots or the possibility for the player to harvest their clovers and add them to an inventory. Clovers could die if not watered or you could get special clovers if you treat them well... (golden clovers?!)
\
Stay tuned!

## Thanks for reading!
Clover has been created by Cecil, France.

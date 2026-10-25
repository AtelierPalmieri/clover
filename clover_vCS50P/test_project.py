from project import *
import pytest
import pygame
pygame.init()
pygame.display.set_mode((1000, 700))

def main():
    test_update()
    test_get_image()
    test_generate_clover()
    test_Clover()
    test_play_pop_sound()

def test_update():
    clover = Clover((0,0),1)

    clover.index = 7
    with pytest.raises(EOFError):
        assert clover.update()

    clover.index = -2
    with pytest.raises(EOFError):
        assert clover.update()

    clover.index = 3
    clover.update()
    assert clover.index == 4
    assert clover.image == clover.images["growing_4"]

def test_get_image():
    clover = Clover((0,0),1)
    #does the function return a Surface object?
    assert isinstance(clover.get_image(0,0), pygame.Surface)

    #is the retured Surface size to the right 56x60px format?
    image = clover.get_image(0,0)
    assert image.get_size() == (56, 60)

    # Does the Surface has the right alpha flag ? (SRCALPHA)
    # Adding another flag to the image (RLEACCEL) for the test:

    image.set_colorkey(pygame.RLEACCEL)
    flags = image.get_flags()

    # Comparing binary values to see if the SRCALPHA flag is present in 'flags':

    assert (flags & pygame.SRCALPHA) == pygame.SRCALPHA
    
    """(
    binary of 65536 (SRCALPHA fag) : 10000000000000000 
    binary of 69632 (SRCALPHA and RLEACCEL flags) : 10001000000000000 
    65536 & 69632 == 10000000000000000 (== binary of SRCALPHA flag)
    )
    """

def test_generate_clover():
    game = Game()
    game.generate_clover((0,0))
    assert game.clovers
    assert len(game.clover_group) == 1

    assert game.clover.rect == pygame.Rect(-18, -60, 56, 60) 
    # clover class rect is set to midbottom corresponding to : (x=-28,y=-60)
    # then generate_clover() aligns the sprite stem to the event position by adding 10 to x

def test_Clover():
    clover1 = Clover((0,0),2)
    assert clover1.type == "four"
    clover2 = Clover((0,0),21)
    assert clover2.type == "three"

def test_play_pop_sound():
    game = Game()
    game.generate_clover((0,0))
    assert game.clover.pop == False

    game.play_pop_sound()
    assert game.clover.pop

if __name__ == "__main__":
    main()
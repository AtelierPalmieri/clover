import pygame
from random import randint

class Clover(pygame.sprite.Sprite):
    def __init__(self, position, droprate):
        super().__init__()

        if droprate < 20:
            self.type = "four"
        else:
            self.type = "three"

        self.sprite_sheet = pygame.image.load(f"images/{self.type}_leaf_sheet_56_60.png").convert_alpha()
        self.index = 1
        self.images = {
            "growing_1": self.get_image(0, 0),
            "growing_2": self.get_image(56, 0),
            "growing_3": self.get_image(56*2, 0),
            "growing_4": self.get_image(56*3, 0),
            "growing_5": self.get_image(56*4, 0),
            "growing_6": self.get_image(56*5, 0),
        }

        self.rect = self.images[f"growing_{self.index}"].get_rect(midbottom=position)
        self.image = self.images[f"growing_{self.index}"]
        self.pop = False
    
    def update(self):
        if self.index == 6:
            self.image = self.images["growing_6"]
        elif self.index > 6 or self.index < 0:
            raise EOFError
        else:
            self.index += 1
            self.image = self.images[f"growing_{self.index}"]

    def get_image(self, x, y):
        image = pygame.Surface((56, 60), pygame.SRCALPHA, 32)
        image.blit(self.sprite_sheet, (0, 0), (x, y, 56, 60))
        image = image.convert_alpha()
        return image

class Game():

    def __init__(self):

        pygame.init()

        """SCREEN AND ICON SETUP"""
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Clover")
        self.ICON = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.ICON)

        """SOUNDS"""
        self.pop_sound_1 = pygame.mixer.Sound("sound_effects/pop_sound_1.wav")
        self.pop_sound_2 = pygame.mixer.Sound("sound_effects/pop_sound_2.wav")
        self.pop_sound_3 = pygame.mixer.Sound("sound_effects/pop_sound_3.wav")
        
        self.pop_sounds = [self.pop_sound_1,self.pop_sound_2,self.pop_sound_3]

        """GRAPHICS"""
        self.background = pygame.image.load("images/background.png").convert_alpha()

        """FRAMERATE"""
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        """SPRITES GROUP"""
        self.clover_group = pygame.sprite.Group()

        """POT POSITIONS"""
        self.pot1_rect = pygame.Rect(223, 367, 251, 117)
        self.pot2_rect = pygame.Rect(690, 370, 134, 76)
        self.pot3_rect = pygame.Rect(546, 425, 168, 80)
        self.pot4_rect = pygame.Rect(548, 539, 263, 152)
        self.pot5_rect = pygame.Rect(170, 517, 316, 164)

        self.pots = [self.pot1_rect, self.pot2_rect, self.pot3_rect, self.pot4_rect, self.pot5_rect]

        self.running = True
        self.frame = 0
        self.clovers = False

    def generate_clover(self, position):
        droprate = randint(0,100)
        self.clover = Clover((position[0]+10,position[1]), droprate)
        self.clover_group.add(self.clover)
        self.clovers = True

    def play_pop_sound(self):
        n = randint(0,2)
        self.pop_sounds[n].play()
        self.clover.pop = True

    def launch(self):
        while self.running:

            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if any(pot.collidepoint(event.pos) for pot in self.pots):
                            self.generate_clover(event.pos)
                            if self.clover.pop == False:
                                self.play_pop_sound()

                if event.type == pygame.QUIT:
                    self.running = False

            if self.frame%30 == 0:
                self.clover_group.update()

            if self.clovers == True:
                self.clover_group.draw(self.screen)

            self.frame += 1
            pygame.display.flip()

def main():
    game = Game()
    game.launch()

if __name__ == "__main__":
    main()
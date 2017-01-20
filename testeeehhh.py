import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.pause()
        pygame.mixer.music.stop()
        self.green = (0,255,0)
        self.white = (255, 255, 255)

        self.height = 900
        self.width = int(self.height * 1.777777778)
        self.size = (self.width, self.height)

        self.tpos1 = ((self.height / 2) - 0)
        self.tpos2 = ((self.height / 2) - 110)
        self.tpos3 = ((self.height / 2) - 220)

        #x,y,r
        self.player1 = player((self.width / 2 ) - 50, (self.tpos1 - 60), 30)
        self.player2 = player((self.width / 2 ) - 50, (self.tpos3 - 60), 30)

        #tile xpos,ypos,height,width
        self.tile1 = tile(((self.width / 2) - 100), self.tpos1, 100, 100)
        self.tile2 = tile(((self.width / 2) - 100), self.tpos2, 100, 100)
        self.tile3 = tile(((self.width / 2) - 100), self.tpos3, 100, 100)

        self.screen = pygame.display.set_mode(self.size)

        # Set up the default font
        self.Menufont = pygame.font.Font(None, 80)
        self.Normalfont = pygame.font.Font(None, 30)

    def game_loop(self):
        while not process_events():
            self.update()
            self.draw()

    # Update game logic
    def update(self):
        self.player1.update()
        self.player2.update()

    # Draw everything
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tile1.draw(self.screen)
        self.tile2.draw(self.screen)
        self.tile3.draw(self.screen)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        # Flip the screen
        pygame.display.flip()

class tile:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (int(self.x), int(self.y), int(self.width), int(self.height)))


class player:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y = var
        elif keys[pygame.K_DOWN]:
            self.y = var

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0),(int(self.x), int(self.y)), int(self.r))


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False


game = Game()
def program():
    game.game_loop()

var = (game.tpos2 - 60)

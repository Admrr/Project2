import pygame, random, time

def process_events():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

class Game:
    def __init__(self):

        pygame.init()

        self.display_height = 800
        self.display_width = int(self.display_height * 1.77777778)
        self.scherm = pygame.display.set_mode((self.display_width, self.display_height))


    def images(self):
        #Loading dice images and positioning them
        self.dd1 = pygame.image.load('dice1.png')
        self.pd1 = self.scherm.blit(pygame.transform.scale(self.dd1, (self.display_width / 2)), (self.display_height / 2))
        self.dd2 = pygame.image.load('dice2.png')
        self.pd2 = self.scherm.blit(pygame.transform.scale(self.dd2, (self.display_width / 2)), (self.display_height / 2))
        self.dd3 = pygame.image.load('dice3.png')
        self.pd3 = self.scherm.blit(pygame.transform.scale(self.dd3, (self.display_width / 2)), (self.display_height / 2))
        self.dd4 = pygame.image.load('dice4.png')
        self.pd4 = self.scherm.blit(pygame.transform.scale(self.dd4, (self.display_width / 2)), (self.display_height / 2))
        self.dd5 = pygame.image.load('dice5.png')
        self.pd5 = self.scherm.blit(pygame.transform.scale(self.dd5, (self.display_width / 2)), (self.display_height / 2))
        self.dd6 = pygame.image.load('dice6.png')
        self.pd6 = self.scherm.blit(pygame.transform.scale(self.dd6, (self.display_width / 2)), (self.display_height / 2))

    def update(self):
        self.images().update()
        self.dice().update()

    def draw(self):
        self.scherm.fill(255, 255, 255)
        pygame.display.flip()

    def dice(self):
        for d in range(12):
            if d == 1:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 2:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 3:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 4:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 5:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 6:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 7:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 8:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 9:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 10:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
            elif d == 11:
                random.random(self.pd1, self.pd2, self.pd3, self.pd4, self.pd5, self.pd6)
                pygame.time.delay(300)

    def gameloop(self):
        while not process_events():
            self.update()
            self.draw()


def program():
    game = Game()
    game.gameloop()

program()
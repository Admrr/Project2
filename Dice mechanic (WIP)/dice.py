import pygame, random, time


pygame.init()

display_height = 800
display_width = int(display_height * 1.77777778)
scherm = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
white = (205,205,205)
intro = True

def dice():
    d1 = pygame.image.load('dice1.png')
    d2 = pygame.image.load('dice2.png')
    d3 = pygame.image.load('dice3.png')
    d4 = pygame.image.load('dice4.png')
    d5 = pygame.image.load('dice5.png')
    d6 = pygame.image.load('dice6.png')
    def diceimg(img):
        scherm.blit(pygame.transform.scale(img, (200, 200)), (0, 0))
    for d in range(0, 12):
        scherm.fill(white)
        n = random.randint(1, 6)
        if n == 1:
            diceimg(d1)
        elif n == 2:
            diceimg(d2)
        elif n == 3:
            diceimg(d3)
        elif n == 4:
            diceimg(d4)
        elif n == 5:
            diceimg(d5)
        elif n == 6:
            diceimg(d6)
        time.sleep(0.1)
        pygame.display.flip()
    time.sleep(3)

def loop():
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scherm.fill(white)
        k = pygame.key.get_pressed()
        if k[pygame.K_SPACE]:
            dice()
        else:
            print("Press space to roll the dice!")
        clock.tick(30)
        pygame.display.flip()

loop()
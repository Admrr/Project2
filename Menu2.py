import pygame
import time
import random
import testeeehhh

pygame.init()

display_height = 800
display_width = int(display_height * 1.77777778)

pygame.mixer.music.load('8bit.mp3')
pygame.mixer.music.play(loops = 999, start = 0.0)

black = (0, 0, 0)
white = (255, 255, 255)
blue = (80,80,140)
bright_blue = (60,60,255)


scherm = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('')
clock = pygame.time.Clock()

bgimg = pygame.image.load('bg2.png')

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def background(x,y):
    scherm.blit(pygame.transform.scale(bgimg, (display_width, display_height)), (0, 0))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(scherm, ac,(x,y,w,h))

        if click[0] == 1 and action == "opt1":
            pygame.QUIT()
        if click[0] == 1 and action == "opt2":
            print("opt2")
        if click[0] == 1 and action == "opt3":
            print("opt3")
        if click[0] == 1 and action == "opt4":
            print("opt4")
        if click[0] == 1 and action == "opt5":
            pygame.mixer.music.pause()
            testeeehhh.program()
            pygame.mixer.music.unpause()
    else:
        pygame.draw.rect(scherm, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("None",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scherm.blit(textSurf, textRect)

def Menu():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        buttonwidth = display_height / 3.5
        buttonheight = 60
        buttonposx = ((display_width / 2) - (buttonwidth / 2))
        button1ypos = display_height - (buttonheight * 2)
        button2ypos = display_height - (buttonheight * 3.5)
        button3ypos = display_height - (buttonheight * 5)
        button4ypos = display_height - (buttonheight * 6.5)
        button5ypos = display_height - (buttonheight * 8)

        scherm.fill(white)
        background(0,0)
        largeText = pygame.font.SysFont("None", 90)
        TextSurf, TextRect = text_objects("naam v/d game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        scherm.blit(TextSurf, TextRect)


        #button  x-pos, y-pos, width, height
        button("Quit", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue, "opt1")
        button("Help", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt2")
        button("Options", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt3")
        button("Continue", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt4")
        button("NewGame", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt5")

        pygame.display.update()
        clock.tick(30)

Menu()
pygame.quit()
quit()
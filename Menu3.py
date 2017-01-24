import pygame
import time
import random
import test

pygame.init()
fullscreen = pygame.FULLSCREEN
display_height = 720
display_width = int(display_height * 1.77777778)

pagenum = 1

naamvdgame = "naam van de game"

black = (0, 0, 0)
white = (255, 255, 255)
blue = (80,80,140)
bright_blue = (130,130,255)

buttonwidth = display_height / 3.5
buttonheight = 60
buttonposx = ((display_width / 2) - (buttonwidth / 2))
button1ypos = display_height - (buttonheight * 2)
button2ypos = display_height - (buttonheight * 3.5)
button3ypos = display_height - (buttonheight * 5)
button4ypos = display_height - (buttonheight * 6.5)
button5ypos = display_height - (buttonheight * 8)


scherm = pygame.display.set_mode((display_width, display_height), fullscreen)
pygame.display.set_caption('')
clock = pygame.time.Clock()

bgimg = pygame.image.load('bg3.png')
popup = pygame.image.load('popup.png')
helpmsg1 = pygame.image.load('text1.png')
helpmsg2 = pygame.image.load('text2.png')
helpmsg3 = pygame.image.load('text3.png')
helpmsg4 = pygame.image.load('text4.png')

pagetext = helpmsg1

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def background(x,y):
    scherm.blit(pygame.transform.scale(bgimg, (display_width, display_height)), (0, 0))

graadnum = 0
graadtext = "easy"
def graad():
    time.sleep(0.3)
    global graadnum
    global graadtext
    graadnum += 1
    if graadnum > 2:
        graadnum = 0
    if graadnum == 0:
        graadtext = "Easy"
    elif graadnum == 1:
        graadtext = "Medium"
    elif graadnum == 2:
        graadtext = "Hard"

volumenum = 0.9
volumetext = 90
def volumeh():
    time.sleep(0.1)
    global volumetext
    global volumenum
    volumetext += 10
    volumenum += 0.1
    if volumenum > 1:
        volumetext = 0
        volumenum = 0
    pygame.mixer.music.set_volume(float(volumenum))

def mute():
    time.sleep(0.2)
    global volumetext
    global volumenum
    if volumenum == float(0):
        volumenum = 0.9
        volumetext = 90
        pygame.mixer.music.set_volume(float(volumenum))
    else:
        volumenum = 0.0
        volumetext = 0
        pygame.mixer.music.set_volume(float(volumenum))


def optiesmenu():
    global Omenu
    Omenu = True
    clock.tick(60)
    while Omenu:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        scherm.fill(white)
        background(0, 0)
        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects(naamvdgame, largeText)
        TextRect.center = ((display_width / 2), (button5ypos/2))
        scherm.blit(TextSurf, TextRect)


        # button  x-pos, y-pos, width, height
        button("Back", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue, "opt6")
        button((str(volumetext)+ "%"), buttonposx + (display_width / 6), button2ypos, 100, buttonheight, blue, bright_blue,"opt7")
        button("Volume", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt7")
        button("Scoreboard", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt8")
        button(str(graadtext), buttonposx + (display_width/6), button4ypos, 100, buttonheight, blue, bright_blue, "opt9")
        button("Difficulty", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt9")
        button("{LEEG}", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt10")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapemsg()

        pygame.display.flip()

def escapemsg():
    global escmenu
    escmenu = True
    clock.tick(60  )
    while escmenu:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        s = pygame.Surface((display_width, display_height))
        s.fill((225, 225, 225))
        s.set_alpha(4)
        scherm.blit(s, (0, 0))

        scherm.blit(pygame.transform.scale(popup, (620, 350)), ((display_width/2)-310, (display_height/2)-140))


        button("No", buttonposx - 150, (display_height/2) + 100, 150, buttonheight, blue, bright_blue, "opt20")
        button("Yes ", buttonposx + 230, (display_height / 2) + 100, 150, buttonheight, blue, bright_blue, "opt1")
        largeText = pygame.font.Font("pixel.ttf", 50)
        TextSurf, TextRect = text_objects("do you want to quit?", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        scherm.blit(TextSurf, TextRect)



        pygame.display.flip()

def mainmenu():
    global Mmenu
    Mmenu = True
    clock.tick(60)
    while Mmenu:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        scherm.fill(white)
        background(0, 0)
        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects(naamvdgame, largeText)
        TextRect.center = ((display_width / 2), (button5ypos/2))
        scherm.blit(TextSurf, TextRect)

        # button  x-pos, y-pos, width, height
        button("Quit", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue, "opt1")
        button("Help", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt2")
        button("Options", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt3")
        button("Continue", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt4")
        button("NewGame", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt5")

        button("Mute", display_width - (buttonheight *2), button1ypos, buttonheight, buttonheight, blue, bright_blue, "opt0")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapemsg()

        pygame.display.flip()


def helpmenu():
    global Hmenu
    global pagetext
    Hmenu = True
    clock.tick(60)
    while Hmenu:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if pagenum < 1:
            global pagenum
            pagenum = 1
        elif pagenum > 4:
            global pagenum
            pagenum = 4
        elif pagenum == 1:
            scherm.blit(pygame.transform.scale(helpmsg1, (display_width - 100, display_height - 100)), (50, 50))
        elif pagenum == 2:
            scherm.blit(pygame.transform.scale(helpmsg2, (display_width - 100, display_height - 100)), (50, 50))
        elif pagenum == 3:
            scherm.blit(pygame.transform.scale(helpmsg3, (display_width - 100, display_height - 100)), (50, 50))
        elif pagenum == 4:
            scherm.blit(pygame.transform.scale(helpmsg4, (display_width - 100, display_height - 100)), (50, 50))

        button("<- page", buttonposx - 480, 600, 150, buttonheight, blue, bright_blue, "opt200")
        button("page -> ", buttonposx + 535, 600, 150, buttonheight, blue, bright_blue, "opt201")
        button("back", buttonposx, 600, 150, buttonheight, blue, bright_blue, "opt111")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapemsg()

        pygame.display.flip()

def introscherm():
    intro = True
    clock.tick(60)
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        scherm.fill(white)
        background(0, 0)

        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects("press space to continue", largeText)
        TextRect.center = ((display_width / 2), (display_height/2))
        scherm.blit(TextSurf, TextRect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        elif keys[pygame.K_SPACE]:
            pygame.mixer.music.load('8bit.mp3')
            pygame.mixer.music.play(loops=999, start=0.0)
            mainmenu()
            intro = False

        pygame.display.flip()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(scherm, ac,(x,y,w,h))

        if click[0] == 1 and action == "opt1":
            pygame.QUIT()
            quit()
        elif click[0] == 1 and action == "opt0":
            mute()
        elif click[0] == 1 and action == "opt2":
            helpmenu()
        elif click[0] == 1 and action == "opt3":
            global Mmenu
            Mmenu = False
            optiesmenu()
        elif click[0] == 1 and action == "opt4":
            print("opt4")
        elif click[0] == 1 and action == "opt5":
            pygame.mixer.music.pause()
            test.game_loop()
            pygame.mixer.music.unpause()
        elif click[0] == 1 and action == "opt6":
            time.sleep(0.3)
            global Omenu
            Omenu = False
            mainmenu()
        elif click[0] == 1 and action == "opt7":
            volumeh()
        elif click[0] == 1 and action == "opt8":
            pass
        elif click[0] == 1 and action == "opt9":
            graad()
        elif click[0] == 1 and action == "opt10":
            pass
        elif click[0] == 1 and action == "opt20":
            global escmenu
            escmenu = False
        elif click[0] == 1 and action == "opt200":
            global pagenum
            time.sleep(0.2)
            pagenum -= 1
        elif click[0] == 1 and action == "opt201":
            global pagenum
            time.sleep(0.2)
            pagenum += 1
        elif click[0] == 1 and action == "opt111":
            optiesmenu()
    else:
        pygame.draw.rect(scherm, ic,(x,y,w,h))

    smallText = pygame.font.Font("pixel.ttf",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scherm.blit(textSurf, textRect)


def Menu():
    introscherm()
Menu()



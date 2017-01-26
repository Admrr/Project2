import pygame
import time
import random
import psycopg2

pygame.init()
fullscreen = pygame.FULLSCREEN
display_height = 720
display_width = int(display_height * 1.77777778)
startx1 = 595
starty1 = 695
startx2 = 772
starty2 = 695
startx3 = 949
starty3 = 695
startx4 = 1126
starty4 = 695
currentplayer = 0
playergodown = 0
players = 0
beurt = 1
steps = 0
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


scherm = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('')
clock = pygame.time.Clock()

bgimg = pygame.image.load('bg3.png')
popup = pygame.image.load('popup.png')
helpmsg1 = pygame.image.load('text1.png')
helpmsg2 = pygame.image.load('text2.png')
helpmsg3 = pygame.image.load('text3.png')
helpmsg4 = pygame.image.load('text4.png')
gamebgimg = pygame.image.load('spelbg.png')

pagetext = helpmsg1

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def background(x,y):
    scherm.blit(pygame.transform.scale(bgimg, (display_width, display_height)), (0, 0))

def gamebg(x,y):
    scherm.blit(pygame.transform.scale(gamebgimg, (display_width, display_height)), (0, 0))

graadnum = 0
graadtext = "makkelijk"
def graad():
    time.sleep(0.3)
    global graadnum
    global graadtext
    graadnum += 1
    if graadnum > 2:
        graadnum = 0
    if graadnum == 0:
        graadtext = "makkelijk"
    elif graadnum == 1:
        graadtext = "gemiddeld"
    elif graadnum == 2:
        graadtext = "moeilijk"

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
        button("Vorige", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue, "opt6")
        button((str(volumetext)+ "%"), buttonposx + (display_width / 6), button2ypos, 130, buttonheight, blue, bright_blue,"opt7")
        button("Volume", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt7")
        button("Scoreboard", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt8")
        button(str(graadtext), buttonposx + (display_width/6), button4ypos, 130, buttonheight, blue, bright_blue, "opt9")
        button("Moeilijkheid", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt9")
        button("{LEEG}", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt10")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapemsg()

        pygame.display.flip()

def highscore():
    global hsmenu
    hsmenu = True
    clock.tick(60)
    # def download_scores():
    #     return interact_with_database("SELECT * FROM highscore")
    #
    # def download_top_score():
    #     result = interact_with_database("SELECT * FROM highscore ORDER BY score DESC")[0]
    #     return result

    while hsmenu:
        for event in pygame.event.get():
        # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background(0,0)
        button("Vorige", buttonposx, display_width/2, 200, buttonheight, blue, bright_blue, "opt666")
        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects("Scorebord", largeText)
        TextRect.center = ((display_width / 2), (100))
        scherm.blit(TextSurf, TextRect)
        pygame.display.flip()
        # topscore = download_top_score()
        # allscore = download_scores()

def newgamescherm():
    global NGmenu
    NGmenu = True
    clock.tick(60)
    while NGmenu:
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
        button("2 spelers", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt45")
        button("3 spelers", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt46")
        button("4 spelers", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt47")
        button("Vorige", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt48")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            escapemsg()

        pygame.display.flip()


def escapemsg():
    global escmenu
    escmenu = True
    clock.tick(60)
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


        button("Nee", buttonposx - 150, (display_height/2) + 100, 150, buttonheight, blue, bright_blue, "opt20")
        button("Ja ", buttonposx + 230, (display_height / 2) + 100, 150, buttonheight, blue, bright_blue, "opt1")
        largeText = pygame.font.Font("pixel.ttf", 50)
        TextSurf, TextRect = text_objects("Wil je stoppen?", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        scherm.blit(TextSurf, TextRect)

        pygame.display.flip()

def pauzemsg():
    global pzmenu
    pzmenu = True
    clock.tick(60)
    while pzmenu:
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


        button("Nee", buttonposx - 150, (display_height/2) + 100, 150, buttonheight, blue, bright_blue, "opt21")
        button("Ja ", buttonposx + 230, (display_height / 2) + 100, 150, buttonheight, blue, bright_blue, "opt22")
        largeText = pygame.font.Font("pixel.ttf", 50)
        TextSurf, TextRect = text_objects("Wil je stoppen?", largeText)
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

        #button  x-pos, y-pos, width, height
        button("Stoppen", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue, "opt1")
        button("Help", buttonposx, button2ypos, buttonwidth, buttonheight, blue, bright_blue, "opt2")
        button("Opties", buttonposx, button3ypos, buttonwidth, buttonheight, blue, bright_blue, "opt3")
        button("Verdergaan", buttonposx, button4ypos, buttonwidth, buttonheight, blue, bright_blue, "opt4")
        button("Nieuwe spel", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt5")

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

        button("<- Pagina", buttonposx - 480, 600, 150, buttonheight, blue, bright_blue, "opt200")
        button("Pagina -> ", buttonposx + 535, 600, 150, buttonheight, blue, bright_blue, "opt201")
        button("Vorige", buttonposx, 600, 150, buttonheight, blue, bright_blue, "opt111")

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
        TextSurf, TextRect = text_objects("Druk spatie om verder te gaan", largeText)
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
            time.sleep(0.3)
            helpmenu()
        elif click[0] == 1 and action == "opt3":
            time.sleep(0.3)
            global Mmenu
            Mmenu = False
            optiesmenu()
        elif click[0] == 1 and action == "opt4":
            print("opt4")
        elif click[0] == 1 and action == "opt5":
            pygame.mixer.music.pause()
            time.sleep(0.3)
            newgamescherm()
            pygame.mixer.music.unpause()
        elif click[0] == 1 and action == "opt6":
            time.sleep(0.3)
            global Omenu
            Omenu = False
            mainmenu()
        elif click[0] == 1 and action == "opt7":
            volumeh()
        elif click[0] == 1 and action == "opt8":
            time.sleep(0.3)
            highscore()
        elif click[0] == 1 and action == "opt9":
            graad()
        elif click[0] == 1 and action == "opt10":
            pass
        elif click[0] == 1 and action == "opt20":
            global escmenu
            escmenu = False
        elif click[0] == 1 and action == "opt21":
            global pzmenu
            pzmenu = False
        elif click[0] == 1 and action == "opt22":
            mainmenu()
        elif click[0] == 1 and action == "opt200":
            global pagenum
            time.sleep(0.2)
            pagenum -= 1
        elif click[0] == 1 and action == "opt201":
            global pagenum
            time.sleep(0.2)
            pagenum += 1
        elif click[0] == 1 and action == "opt111":
            time.sleep(0.3)
            optiesmenu()
        elif click[0] == 1 and action == "opt666":
            time.sleep(0.3)
            optiesmenu()
        elif click[0] == 1 and action == "opt45":
            global players
            players = 2
            global startx1, starty1, startx2, starty2, startx3, starty3, startx4, starty4
            startx1 = 595
            starty1 = 695
            startx2 = 772
            starty2 = 695
            startx3 = 949
            starty3 = 695
            startx4 = 1126
            starty4 = 695
            game_loop()
        elif click[0] == 1 and action == "opt46":
            global players
            players = 3
            global startx1, starty1, startx2, starty2, startx3, starty3, startx4, starty4
            startx1 = 595
            starty1 = 695
            startx2 = 772
            starty2 = 695
            startx3 = 949
            starty3 = 695
            startx4 = 1126
            starty4 = 695
            game_loop()
        elif click[0] == 1 and action == "opt47":
            global players
            players = 4
            global startx1, starty1, startx2, starty2, startx3, starty3, startx4, starty4
            startx1 = 595
            starty1 = 695
            startx2 = 772
            starty2 = 695
            startx3 = 949
            starty3 = 695
            startx4 = 1126
            starty4 = 695
            game_loop()
        elif click[0] == 1 and action == "opt48":
            time.sleep(0.3)
            mainmenu()
    else:
        pygame.draw.rect(scherm, ic,(x,y,w,h))

    smallText = pygame.font.Font("pixel.ttf",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scherm.blit(textSurf, textRect)

def winscreen():
    global winner, playername
    global game_loop
    wsscreen = True
    while wsscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            winner = False
            game_loop = False
            time.sleep(0.3)
            mainmenu()
        elif keys[pygame.K_ESCAPE]:
            winner = False
            game_loop = False
            time.sleep(0.3)
            mainmenu()

        if winner == 1:
            winimg = pygame.image.load('winneryellow.png')
        elif winner == 2:
            winimg = pygame.image.load('winnerred.png')
        elif winner == 3:
            winimg = pygame.image.load('winnerblue.png')
        elif winner == 4:
            winimg = pygame.image.load('winnergreen.png')
        scherm.blit(pygame.transform.scale(winimg, (display_width, display_height)), (0, 0))

        largeText = pygame.font.Font("pixel.ttf", 50)
        TextSurf, TextRect = text_objects(playername + " wins  "+ "  Score:" + "{score-var}", largeText)
        TextSurf2, TextRect2 = text_objects("druk op spatie om verder te gaan", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        TextRect2.center = ((display_width / 2), (650))
        scherm.blit(TextSurf, TextRect)
        scherm.blit(TextSurf2, TextRect2)
        pygame.display.flip()

def game_loop():
    gameExit = False
    global startx1,starty1,startx2,starty2,startx3,starty3,startx4,starty4,beurt
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        gamebg(0,0)
        playername = '.'
        if beurt == 1:
            playername = "Speler 1"
        elif beurt == 2:
            playername = "Speler 2"
        elif beurt == 3:
            playername = "Speler 3"
        elif beurt == 4:
            playername = "Speler 4"
        drawboard()
        if beurt > players:
            beurt = 1
        print(beurt)

        if keys[pygame.K_UP]:
            move("up")
        elif keys[pygame.K_DOWN]:
            move("down")
        elif keys[pygame.K_LEFT]:
            move("left")
        elif keys[pygame.K_RIGHT]:
            move("right")
        elif keys[pygame.K_ESCAPE]:
            pauzemsg()

        smallText = pygame.font.Font("pixel.ttf", 27)
        textSurf, textRect = text_objects("Huidige beurt: " + playername, smallText)
        textRect.center = (190, 30)
        scherm.blit(textSurf, textRect)

        renderplayer()
        pygame.display.flip()
        clock.tick(30)
player1img = pygame.image.load('player1.png')
player2img = pygame.image.load('player2.png')
player3img = pygame.image.load('player3.png')
player4img = pygame.image.load('player4.png')

def player1(x,y):
    scherm.blit( pygame.transform.scale(player1img, (40,40)), (x-25,y-25))
def player2(x,y):
    scherm.blit(pygame.transform.scale(player2img, (40, 40)), (x - 25, y - 25))
def player3(x,y):
    scherm.blit(pygame.transform.scale(player3img, (40, 40)), (x - 25, y - 25))
def player4(x,y):
    scherm.blit(pygame.transform.scale(player4img, (40, 40)), (x - 25, y - 25))

def renderplayer():
    if players == 2:
        player1(startx1, starty1)
        player2(startx2, starty2)
    elif players == 3:
        player1(startx1, starty1)
        player2(startx2, starty2)
        player3(startx3, starty3)
    elif players == 4:
        player1(startx1, starty1)
        player2(startx2, starty2)
        player3(startx3, starty3)
        player4(startx4, starty4)


def collisioncheck(player):
    global beurt,steps,currentplayer, playergodown
    collision = False
    dead = 0
    if player == 1:
        currentplayer = 1
        if starty1 == 695:
            pass
        else:
            if (startx1,starty1) == (startx2, starty2):
                print("bots1-2")
                collision = True
                dead = 2
            elif (startx1,starty1) == (startx3, starty3):
                print("bots1-3")
                collision = True
                dead = 3
            elif (startx1,starty1) == (startx4, starty4):
                print("bots1-4")
                collision = True
                dead = 4
    elif player == 2:
        currentplayer = 2
        if starty2 == 695:
            pass
        else:
            if (startx2, starty2) == (startx1, starty1):
                print("bots2-1")
                collision = True
                dead = 1
            elif (startx2, starty2) == (startx3, starty3):
                print("bots2-3")
                collision = True
                dead = 3
            elif (startx2, starty2) == (startx4, starty4):
                print("bots2-4")
                collision = True
                dead = 4
    elif player == 3:
        currentplayer = 3
        if starty3 == 695:
            pass
        else:
            if (startx3, starty3) == (startx1, starty1):
                print("bots3-1")
                collision = True
                dead = 1
            elif (startx3, starty3) == (startx2, starty2):
                print("bots3-2")
                collision = True
                dead = 2
            elif (startx3, starty3) == (startx4, starty4):
                print("bots3-4")
                collision = True
                dead = 4
    elif player == 4:
        currentplayer = 4
        if starty4 == 695:
            pass
        else:
            if (startx4, starty4) == (startx1, starty1):
                print("bots4-1")
                collision = True
                dead = 1
            elif (startx4, starty4) == (startx2, starty2):
                print("bots4-2")
                collision = True
                dead = 2
            elif (startx4, starty4) == (startx3, starty3):
                print("bots4-3")
                collision = True
                dead = 3

    if collision == True:
        global collision
        playergodown = dead
        rolldice()
        while steps != 0:
            godown("down")
    beurt += 1



def rolldice():
    end = 0
    dd1 = pygame.image.load('dice1.png')
    dd2 = pygame.image.load('dice2.png')
    dd3 = pygame.image.load('dice3.png')
    dd4 = pygame.image.load('dice4.png')
    dd5 = pygame.image.load('dice5.png')
    dd6 = pygame.image.load('dice6.png')
    def diceimg(img):
        scherm.blit(pygame.transform.scale(img, (100, 100)), (20, 20))
    for d in range(0, 12):
        global steps
        n = random.randint(1, 6)
        if n == 1:
            diceimg(dd1)
            end = 1
        elif n == 2:
            diceimg(dd1)
            end = 1
        elif n == 3:
            diceimg(dd2)
            end = 2
        elif n == 4:
            diceimg(dd2)
            end = 2
        elif n == 5:
            diceimg(dd3)
            end = 3
        elif n == 6:
            diceimg(dd3)
            end = 3
        time.sleep(0.1)
        renderplayer()
        pygame.display.flip()
    steps = end
    time.sleep(1.5)

def godown(direction):
    global startx1, starty1, startx2, starty2, startx3, starty3, startx4, starty4
    global steps
    clock.tick(30)
    if direction == "down":
        rolldice()
        print(steps)
        while steps != 0:
            time.sleep(0.2)
            if playergodown == 1:
                starty1 += 45
                if starty1 > display_height:
                    starty1 = 695
            elif playergodown == 2:
                starty2 += 45
                if starty2 > display_height:
                    starty2 = 695
            elif playergodown == 3:
                starty3 += 45
                if starty3 > display_height:
                    starty3 = 695
            elif playergodown == 4:
                starty4 += 45
                if starty4 > display_height:
                    starty4 = 695
            steps -= 1
            drawboard()
            renderplayer()
            pygame.display.flip()
def move(x):
    global startx1, starty1, startx2, starty2, startx3, starty3, startx4, starty4
    global steps, winner, playername
    clock.tick(30)
    if x == "left":
        rolldice()
        print(steps)
        while steps != 0:
            time.sleep(0.2)
            if beurt == 1:
                startx1 -= 177
                if startx1 < 560:
                    startx1 = (1126)
            elif beurt == 2:
                startx2 -= 177
                if startx2 < 560:
                    startx2 = (1126)
            elif beurt == 3:
                startx3 -= 177
                if startx3 < 560:
                    startx3 = (1126)
            elif beurt == 4:
                startx4 -= 177
                if startx4 < 560:
                    startx4 = (1126)
            steps -= 1
            drawboard()
            renderplayer()
            pygame.display.flip()
    elif x == "right":
        rolldice()
        print(steps)
        while steps != 0:
            time.sleep(0.2)
            if beurt == 1:
                startx1 += 177
                if startx1 > 1200:
                    startx1 = 595
            elif beurt == 2:
                startx2 += 177
                if startx2 > 1200:
                    startx2 = 595
            elif beurt == 3:
                startx3 += 177
                if startx3 > 1200:
                    startx3 = 595
            elif beurt == 4:
                startx4 += 177
                if startx4 > 1200:
                    startx4 = 595
            steps -= 1
            drawboard()
            renderplayer()
            pygame.display.flip()
    elif x == "up":
        rolldice()
        print(steps)
        while steps != 0:
            time.sleep(0.2)
            if beurt == 1:
                starty1 -= 45
                if starty1 < 0:
                    winner = 1
                    playername = 'Player One'
                    winscreen()
            elif beurt == 2:
                starty2 -= 45
                if starty2 < 0:
                    winner = 2
                    playername = 'Player Two'
                    winscreen()
            elif beurt == 3:
                starty3 -= 45
                if starty3 < 0:
                    winner = 3
                    playername = 'Player Three'
                    winscreen()
            elif beurt == 4:
                starty4 -= 45
                if starty4 < 0:
                    winner = 4
                    playername = 'Player Four'
                    winscreen()
            steps -= 1
            drawboard()
            renderplayer()
            pygame.display.flip()
    elif x == "down":
        rolldice()
        print(steps)
        while steps != 0:
            time.sleep(0.2)
            if beurt == 1:
                starty1 += 45
                if starty1 > display_height:
                    starty1 = 695
            elif beurt == 2:
                starty2 += 45
                if starty2 > display_height:
                    starty2 = 695
            elif beurt == 3:
                starty3 += 45
                if starty3 > display_height:
                    starty3 = 695
            elif beurt == 4:
                starty4 += 45
                if starty4 > display_height:
                    starty4 = 695
            steps -= 1
            drawboard()
            renderplayer()
            pygame.display.flip()
    collisioncheck(beurt)
    print(beurt)


def drawboard():
    for yas in range(0, 16):
        for xas in range(0, 8):
            if xas > 2 and xas < 7:
                pygame.draw.rect(scherm, (86, 73, 67), [(xas * 177) + 45, yas * 45, 35, 35])

def Menu():
    introscherm()
Menu()
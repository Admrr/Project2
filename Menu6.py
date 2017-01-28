import pygame
import time
import random
import psycopg2

pygame.init()
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
catplr1 = 1
catplr2 = 2
catplr3 = 3
catplr4 = 4
catplr1naam = 'entertainment'
catplr2naam = 'sport'
catplr3naam = 'geschiedenis'
catplr4naam = 'geografie'
antwoord = False
qbuttonwidth = display_height / 1.5
qbuttonheight = 60
qbuttonposx = ((display_width / 2) - (qbuttonwidth / 2))
qbutton1ypos = display_height - (qbuttonheight * 2)
qbutton2ypos = display_height - (qbuttonheight * 3.5)
qbutton3ypos = display_height - (qbuttonheight * 5)


naamvdgame = "naam van de game"

black = (0, 0, 0)
white = (255, 255, 255)
blue = (80,80,140)
bright_blue = (130,130,255)
qred = (255, 102, 102)
qblue = (102, 178, 255)
qyellow = (255, 255, 102)
qgreen = (102, 255, 102)


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

def fout():
    img = pygame.image.load("fout.png")
    scherm.blit(img, (display_width / 2.5, display_height / 2.6))

def juist():
    while True:
        img = pygame.image.load("juist.png")
        scherm.blit(img, (display_width / 2.5, display_height / 2.6))
        return False

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
        button("Categorie ", buttonposx, button5ypos, buttonwidth, buttonheight, blue, bright_blue, "opt10")

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
        TextSurf, TextRect = text_objects("Wil je afsluiten?", largeText)
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

def catcheck():
    global catplr1naam, catplr2naam, catplr3naam, catplr4naam
    if catplr1 == 1:
        catplr1naam = "entertainment"
    elif catplr1 == 2:
        catplr1naam = "sport"
    elif catplr1 == 3:
        catplr1naam = "geschiedenis"
    elif catplr1 == 4:
        catplr1naam = "geografie"
    if catplr2 == 1:
        catplr2naam = "entertainment"
    elif catplr2 == 2:
        catplr2naam = "sport"
    elif catplr2 == 3:
        catplr2naam = "geschiedenis"
    elif catplr2 == 4:
        catplr2naam = "geografie"
    if catplr3 == 1:
        catplr3naam = "entertainment"
    elif catplr3 == 2:
        catplr3naam = "sport"
    elif catplr3 == 3:
        catplr3naam = "geschiedenis"
    elif catplr3 == 4:
        catplr3naam = "geografie"
    if catplr4 == 1:
        catplr4naam = "entertainment"
    elif catplr4 == 2:
        catplr4naam = "sport"
    elif catplr4 == 3:
        catplr4naam = "geschiedenis"
    elif catplr4 == 4:
        catplr4naam = "geografie"

def catmenu():
    global CAmenu
    CAmenu = True
    clock.tick(60)
    while CAmenu:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background(0, 0)
        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects(naamvdgame, largeText)
        TextRect.center = ((display_width / 2), (button5ypos/2))
        scherm.blit(TextSurf, TextRect)

        catcheck()
        button("categorie speler1: " + catplr1naam, buttonposx-120, button5ypos, 450, buttonheight, blue, bright_blue, "opt711")
        button("categorie speler2: " + catplr2naam, buttonposx-120, button4ypos, 450, buttonheight, blue, bright_blue, "opt712")
        button("categorie speler3: " + catplr3naam, buttonposx-120, button3ypos, 450, buttonheight, blue, bright_blue, "opt713")
        button("categorie speler4: " + catplr4naam, buttonposx - 120, button2ypos, 450, buttonheight, blue, bright_blue,"opt714")
        button("terug", buttonposx, button1ypos, buttonwidth, buttonheight, blue, bright_blue,"opt3")

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
            time.sleep(0.3)
            catmenu()
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
        elif click[0] == 1 and action == "opt450":
            time.sleep(0.3)
            fout()
        elif click[0] == 1 and action == "opt451":
            time.sleep(0.3)
            juist()
        elif click[0] == 1 and action == "opt666":
            time.sleep(0.3)
            optiesmenu()
        elif click[0] == 1 and action == "opt600":
            move("up")
        elif click[0] == 1 and action == "opt601":
            move("down")
        elif click[0] == 1 and action == "opt602":
            move("left")
        elif click[0] == 1 and action == "opt603":
            move("right")
        elif click[0] == 1 and action == "opt711":
            time.sleep(0.15)
            global catplr1
            catplr1 += 1
            if catplr1 > 4:
                catplr1 = 1
        elif click[0] == 1 and action == "opt712":
            time.sleep(0.15)
            global catplr2
            catplr2 += 1
            if catplr2 > 4:
                catplr2 = 1
        elif click[0] == 1 and action == "opt713":
            time.sleep(0.15)
            global catplr3
            catplr3 += 1
            if catplr3 > 4:
                catplr3 = 1
        elif click[0] == 1 and action == "opt714":
            time.sleep(0.15)
            global catplr4
            catplr4 += 1
            if catplr4 > 4:
                catplr4 = 1
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

        a = button("Boven", buttonposx - 380, 530, 110, buttonheight, blue, bright_blue, "opt600")
        u = button("Beneden", buttonposx - 380, 600, 110, buttonheight, blue, bright_blue, "opt601")
        l = button("Links", buttonposx - 500, 600, 110, buttonheight, blue, bright_blue, "opt602")
        r = button("Rechts", buttonposx - 260, 600, 110, buttonheight, blue, bright_blue, "opt603")

        smallText = pygame.font.Font("pixel.ttf", 27)
        textSurf, textRect = text_objects("Huidige beurt: " + playername, smallText)
        textRect.center = (190, 30)
        scherm.blit(textSurf, textRect)
        if keys[pygame.K_ESCAPE]:
            pauzemsg()
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
        button("Boven", buttonposx - 380, 530, 110, buttonheight, blue, bright_blue, "")
        button("Beneden", buttonposx - 380, 600, 110, buttonheight, blue, bright_blue, "")
        button("Links", buttonposx - 500, 600, 110, buttonheight, blue, bright_blue, "")
        button("Rechts", buttonposx - 260, 600, 110, buttonheight, blue, bright_blue, "")
        pygame.display.flip()
    steps = end
    imagesq()
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

def imagesq():

    eq1 = pygame.image.load('entertainment1.png')
    eq2 = pygame.image.load('entertainment2.png')
    eq3 = pygame.image.load('entertainment3.png')
    eq4 = pygame.image.load('entertainment4.png')
    eq5 = pygame.image.load('entertainment5.png')
    eq6 = pygame.image.load('entertainment6.png')
    eq7 = pygame.image.load('entertainment7.png')
    eq8 = pygame.image.load('entertainment8.png')
    eq9 = pygame.image.load('entertainment9.png')
    eq10 = pygame.image.load('entertainment10.png')
    eq11 = pygame.image.load('entertainment11.png')
    eq12 = pygame.image.load('entertainment12.png')
    eq13 = pygame.image.load('entertainment13.png')
    eq14 = pygame.image.load('entertainment14.png')
    eq15 = pygame.image.load('entertainment15.png')
    eq16 = pygame.image.load('entertainment16.png')
    eq17 = pygame.image.load('entertainment17.png')
    eq18 = pygame.image.load('entertainment18.png')
    eq19 = pygame.image.load('entertainment19.png')
    eq20 = pygame.image.load('entertainment20.png')
    eq21 = pygame.image.load('entertainment21.png')
    eq22 = pygame.image.load('entertainment22.png')
    eq23 = pygame.image.load('entertainment23.png')
    eq24 = pygame.image.load('entertainment24.png')
    gq1 = pygame.image.load('geografie1.png')
    gq2 = pygame.image.load('geografie2.png')
    gq3 = pygame.image.load('geografie3.png')
    gq4 = pygame.image.load('geografie4.png')
    gq5 = pygame.image.load('geografie5.png')
    gq6 = pygame.image.load('geografie6.png')
    gq7 = pygame.image.load('geografie7.png')
    gq8 = pygame.image.load('geografie8.png')
    gq9 = pygame.image.load('geografie9.png')
    gq10 = pygame.image.load('geografie10.png')
    gq11 = pygame.image.load('geografie11.png')
    gq12 = pygame.image.load('geografie12.png')
    gq13 = pygame.image.load('geografie13.png')
    gq14 = pygame.image.load('geografie14.png')
    gq15 = pygame.image.load('geografie15.png')
    gq16 = pygame.image.load('geografie16.png')
    gq17 = pygame.image.load('geografie17.png')
    gq18 = pygame.image.load('geografie18.png')
    gq19 = pygame.image.load('geografie19.png')
    gq20 = pygame.image.load('geografie20.png')
    gq21 = pygame.image.load('geografie21.png')
    gq22 = pygame.image.load('geografie22.png')
    gq23 = pygame.image.load('geografie23.png')
    gq24 = pygame.image.load('geografie24.png')
    hq1 = pygame.image.load('historie1.png')
    hq2 = pygame.image.load('historie2.png')
    hq3 = pygame.image.load('historie3.png')
    hq4 = pygame.image.load('historie4.png')
    hq5 = pygame.image.load('historie5.png')
    hq6 = pygame.image.load('historie6.png')
    hq7 = pygame.image.load('historie7.png')
    hq8 = pygame.image.load('historie8.png')
    hq9 = pygame.image.load('historie9.png')
    hq10 = pygame.image.load('historie10.png')
    hq11 = pygame.image.load('historie11.png')
    hq12 = pygame.image.load('historie12.png')
    hq13 = pygame.image.load('historie13.png')
    hq14 = pygame.image.load('historie14.png')
    hq15 = pygame.image.load('historie15.png')
    hq16 = pygame.image.load('historie16.png')
    hq17 = pygame.image.load('historie17.png')
    hq18 = pygame.image.load('historie18.png')
    hq19 = pygame.image.load('historie19.png')
    hq20 = pygame.image.load('historie20.png')
    hq21 = pygame.image.load('historie21.png')
    hq22 = pygame.image.load('historie22.png')
    hq23 = pygame.image.load('historie23.png')
    hq24 = pygame.image.load('historie24.png')
    sq1 = pygame.image.load('sport1.png')
    sq2 = pygame.image.load('sport2.png')
    sq3 = pygame.image.load('sport3.png')
    sq4 = pygame.image.load('sport4.png')
    sq5 = pygame.image.load('sport5.png')
    sq6 = pygame.image.load('sport6.png')
    sq7 = pygame.image.load('sport7.png')
    sq8 = pygame.image.load('sport8.png')
    sq9 = pygame.image.load('sport9.png')
    sq10 = pygame.image.load('sport10.png')
    sq11 = pygame.image.load('sport11.png')
    sq12 = pygame.image.load('sport12.png')
    sq13 = pygame.image.load('sport13.png')
    sq14 = pygame.image.load('sport14.png')
    sq15 = pygame.image.load('sport15.png')
    sq16 = pygame.image.load('sport16.png')
    sq17 = pygame.image.load('sport17.png')
    sq18 = pygame.image.load('sport18.png')
    sq19 = pygame.image.load('sport19.png')
    sq20 = pygame.image.load('sport20.png')
    sq21 = pygame.image.load('sport21.png')
    sq22 = pygame.image.load('sport22.png')
    sq23 = pygame.image.load('sport23.png')
    sq24 = pygame.image.load('sport24.png')

    def qmusic():
        pygame.mixer.music.load('8bitquestion.mp3')
        pygame.mixer.music.play(loops=1, start=0.0)

    def qimg(img):
        scherm.blit(img, (display_width / 2.78, display_height / 2.6))

    while True:
       n = random.randint(1, 24)
       if n == 1:
            qimg(eq1)
            #A is juist
            vragen("A. De Witte Aap","B. Het NRC","C. Café de Beurs","opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 2:
           qimg(eq2)
           #B is juist
           vragen("A. R'dam Escape","B. Escape010","C. Room Escape","opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           #C is juist
           qimg(eq3)
           vragen("A. Segway","B. Boot","C. Auto","opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           #B is juist
           qimg(eq4)
           vragen("A. H&M","B. Mediamarkt","C. The Sting","opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           #A is juist
           qimg(eq5)
           vragen("A. Cinerama","B. Pathe De Kuip","C. Pathe Schouwburgplein","opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           #C is juist
           qimg(eq6)
           vragen("A. Havenmuseum","B. Mariniersmuseum","C. Maritiemmuseum","opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           #C is juist
           qimg(eq7)
           vragen("A. De Euromast","B. Museumplein","C. De Markthal","opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           #B is juist
           qimg(eq8)
           vragen("A. Pathe de Kuip","B. Pathe de Kroon","C. Pathe Schouwburgplein","opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           #A is juist
           qimg(eq9)
           vragen("A. 925000 bezoekers","B. 675000 bezoekers","C. 830000 bezoekers","opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(eq10)
           #B is juist
           vragen("A. Hoek van Holland","B. Euromast Park","C. Plaswijckpark","opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           #A is juist
           qimg(eq11)
           vragen("A. Luxemburg en België","B. Duitsland en België","C. Duitsland en Frankrijk","opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(eq12)
           #C is juist
           vragen("A. Drive & Eat","B. Bicycle Diner","C. Bike & Bite","opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           #A is juist
           qimg(eq13)
           vragen("A. De Zwanenboot", "B. De Pannenkoekenboot", "C. De Berenboot", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           #C is juist
           qimg(eq14)
           vragen("A. Cinerama", "B. Pathe de Kuip", "C. LantarenVenster", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(eq15)
           #A is juist
           vragen("A. Mullerpier", "B. Pier 80", "C. Schouwburgplein", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           #A is juist
           qimg(eq16)
           vragen("A. De Witte de Withstraat", "B. Kruiskade", "C. Doedesstraat", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           #C is juist
           qimg(eq17)
           vragen("A. Willemsbrug", "B. Spaansebrug", "C. Erasmusbrug", "opt450", "opt450",  "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           #C is juist
           qimg(eq18)
           vragen("A. Noordelijk Film Festival", "B. Vlier Film Festival", "C. Internationaal Film Festival", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           #A is juist
           qimg(eq19)
           vragen("A. Diergaarde Blijdorp", "B. Plaswijckpark", "C. Utropia", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           #A is juist
           qimg(eq20)
           vragen("A. De Markthal", "B. De Verwoeste Stad", "C. De Boeg", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           #B is juist
           qimg(eq21)
           vragen("A. Wijnhaven", "B. Rijnhaven", "C. Parkhaven", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           #B is juist
           qimg(eq22)
           vragen("A. Rotterdam Creeper Walk", "B. Rotterdam Zombie Walk", "C. Rotterdam Undead Walk", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           #C is juist
           qimg(eq23)
           vragen("A. Rotterdam Gaypride", "B. Rotterdam LGBT Parade", "C. Rotterdam Pride", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           #B is juist
           qimg(eq24)
           vragen("A. Januari","B. September","C. Mei","opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 1:
            qimg(hq1)
            vragen("A. Kooplieden hadden dit vroeger bedacht", "B. Aan de rivier de rotte", "C. Er was een dam aangelegd in de maas", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 2:
            qimg(hq2)
            vragen("A. De oude haven", "B. VOC magazijn", "St. Laurenskerk", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 3:
            qimg(hq3)
            vragen("A. Ahmed Aboutaleb", "B. Jules Deelder", "C. Willem Alexander", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 4:
            qimg(hq4)
            vragen("A. Waar", "B. Niet Waar", "C. Weet ik niet", "opt451", "opt450", "op450")
            qmusic()
            pygame.display.flip()
       elif n == 5:
            qimg(hq5)
            vragen("A. De beste bakker van de stad was daar gevestigd", "B. De prostituees", "C. De oudste beschermde boom van de stad staat daar", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 6:
            qimg(hq6)
            vragen("A. 1855", "B. 1975", "C. 1915", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 8:
            qimg(hq8)
            vragen("A. De Bijenkorf", "B. De Kubuswoningen", "C. The Red Apple", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 7:
            qimg(hq7)
            vragen("A. De ondergrondse winkelstraat", "B. Beurstraverse", "C. Gewoon de koopgoot", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 10:
            qimg(hq10)
            vragen("A. De nieuwe Binnenweg", "B. Maasbrug", "C. Koninginnenbrug", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 9:
            qimg(hq9)
            vragen("A. 5000", "B. 8000", "C. 12000", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 11:
            qimg(hq11)
            vragen("A. Suiker", "B. Wol", "C. Cacao", "opt451", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 12:
            qimg(hq12)
            vragen("A. De Nieuwe Waterweg", "B. De Maas zeeverbinding", "C. Het Nieuwe Water kanaal", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 13:
            qimg(hq13)
            vragen("A. Maaskant", "B. Brinkman en van der Vlugt", "C. Koolhaas", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 14:
            qimg(hq14)
            vragen("A. 1250", "B. 1340", "C. 1590", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 15:
            qimg(hq15)
            vragen("A. Waalhaven", "B. De Maashaven", "C. Europoort", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 16:
            qimg(hq16)
            vragen("A. GroenLinks", "B. DENK", "C. Leefbaar Rotterdam", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 17:
            qimg(hq17)
            vragen("A. Loods 21", "B. Loods 5", "C. Loods 24", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 18:
            qimg(hq18)
            vragen("A. Nederland-Amerika Lijn", "B. Holland-Amerika Lijn", "C. Rotterdam-Amerika Lijn", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 19:
            qimg(hq19)
            vragen("A. NRC", "B. De Telegraaf", "C. Metro", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 20:
            qimg(hq20)
            vragen("A. Nieuwe Roddel Courant", "B. Nieuwe Rotterdamsche Courant", "Nieuwe Reactie Courant", "opt450", "opt451", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 21:
            qimg(hq21)
            vragen("A. Blaak 6", "B. Markthal", "C. Het witte Huis", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 22:
            qimg(hq22)
            vragen("A. 1939-1946", "B. 1935-1940", "C. 1940-1945", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 23:
            qimg(hq23)
            vragen("A. De verwoeste Stad", "B. Kabouter Buttplug", "C. Erasmusbeeld", "opt451", "opt450", "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 24:
            qimg(hq24)
            vragen("A. Nederland-Amerika lijn", "B. Rotterdam-Amerika Lijn", "C. Holland-Amerika lijn", "opt450", "opt450", "opt451")
            qmusic()
            pygame.display.flip()
       elif n == 1:
           qimg(gq1)
           vragen("A. Kerktoren hillegondakerk", "B. St. Laurenskerk.", "C. Stadhuis van Rotterdam", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 2:
           qimg(gq2)
           vragen("A. 800.000", "B. 900.000", "C. 1.000.000", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           qimg(gq3)
           vragen("A. De Willemsbrug", "B. De Koninginnebrug", "C. De van Briennenoordbrug", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           qimg(gq4)
           vragen("A. Stad der Wonderen", "B. Stad der Steden", "C. Havenstad", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           qimg(gq5)
           vragen("A. Noord-Holland", "B. Zuid-Holland", "C. Noord-Brabant", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           qimg(gq6)
           vragen("A. De Maas", "B. De Rijn", "C. De Waal", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           qimg(gq7)
           vragen("A. 50 tot 60km", "B. 60 tot 70km", "C. 70 tot 80km", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(gq10)
           vragen("A. Waar", "B. Niet Waar", "C. Weet Niet", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           qimg(gq8)
           vragen("A. De Willemsbrug", "B. De Erasmusbrug", "C. De van Briennenoordbrug", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           qimg(gq9)
           button("A. Waar", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Niet waar", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           qimg(gq11)
           vragen("A. Waar", "B. Niet Waar", "C. Weet Niet", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(gq12)
           vragen("A. Waar", "B. Niet waar", "C. Weet Niet", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           qimg(gq13)
           vragen("A. Metro", "B. Auto", "C. Fiets", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           qimg(gq14)
           vragen("A. 760 tot 780mm", "B. 780 tot 800mm", "C. 800 tot 820mm", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(gq15)
           vragen("A. 150.000", "B. 300.000", "C. 450.000", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           qimg(gq16)
           vragen("A. 327,6 km2", "B. 319,4 km2", "C. 352,8 km2", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           qimg(gq17)
           vragen("A. 180 meter", "B. 195 meter", "C. 185 meter", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           qimg(gq18)
           vragen("A. De Maastoren", "B. De Boeg", "C. Euromast", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           qimg(gq19)
           vragen("A. Markthalwoningen", "B. Blaakwoningen", "C. De Kubuswoningen", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           qimg(gq20)
           vragen("A. De Rotterdamse berg", "B. De Courantse berg", "C. Rotterdam heeft geen bergen", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           qimg(gq21)
           vragen("A. Koopgoot kerstboom", "B. Kabouter Buttplug", "C. Erasmus kerstboom", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           qimg(gq22)
           vragen("A. Rotterdam is de grootste stad van Nederland", "B. Den Haag", "C. Amsterdam", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           qimg(gq23)
           vragen("A. Tropisch klimaat", "B. Droog klimaat", "C. Gematigd klimaat", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           qimg(gq24)
           vragen("A. De Willemsbrug", "B. De Erasmusbrug", "C. De Hef", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 1:
           qimg(sq1)
           vragen("A. 2000", "B. 2005", "C. 2010", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 2:
           qimg(sq2)
           vragen("A. ABN AMRO World Tennis Tournament", "B. Ahoy Open", "C. Heineken Open", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           qimg(sq3)
           vragen("A. HVGR", "B. Focus", "C. HC Rotterdam", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           qimg(sq4)
           vragen("A. Fitness", "B. Voetbal", "C. Basketbal", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           qimg(sq5)
           vragen("A. Dorian van Rijsselberghe", "B. Marhinde Verkerk", "C. Edith Bosch", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           qimg(sq6)
           vragen("A. Willem Alexander baan", "B. Beatrix baan", "C. Juliana baan", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           qimg(sq7)
           vragen("A. Watersporten, Wielrennen en hardlopen", "B. Voetbal, Hockey en basketbal", "C. Fitness, hardlopen en basketbal", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           qimg(sq8)
           vragen("A. Rechtsback", "B. Linksback", "C. Linksbuiten", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           qimg(sq11)
           vragen("A. 42,125 km", "B. 42,450 km", "C. 42,680 km", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           qimg(sq9)
           vragen("A. Zich verder van het doel bevindt dan de keeper.", "B. Zich dichter bij de doellijn van de tegenstander bevindt dan de bal en de vóórlaatste tegenstander.", "C. Zich buiten de lijn van het veld bevindt en de bal in het spel is.", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(sq10)
           vragen("A. De Toren", "B. Het Kasteel", "C. De Arena", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(sq12)
           vragen("A. 9", "B. 10", "C. 11", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           qimg(sq13)
           vragen("A. 1850", "B. 1875", "C. 1900", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           qimg(sq14)
           vragen("A. Waar", "B. Niet waar", "C. Even groot", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(sq15)
           vragen("A. 1", "B. 2", "C. 3", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           qimg(sq16)
           vragen("A. 1", "B. 3", "C. 2", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           qimg(sq17)
           vragen("A. Sparta Rotterdam", "B. Excelsior", "C. Feyenoord", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           qimg(sq18)
           vragen("A. Alley-oop", "B. Dunk", "C. Smash", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           qimg(sq19)
           vragen("A. Eenpuntlijn", "B. Tweepuntslijn", "C. Driepuntslijn", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           qimg(sq20)
           vragen("A. Honkbal", "B. Softbal", "C. Voetbal", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           qimg(sq21)
           vragen("A. Pathe Schouwburgplein", "B. KFC", "C. Topsportcentrum Rotterdam", "opt450", "opt450", "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           qimg(sq22)
           vragen("A. City Racing Rotterdam", "B. Rotterdam Racing through the City", "C. F1: Rotterdam", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           qimg(sq23)
           vragen("A. Dutch Basketball League", "B. NBA", "C. Basketball League A1", "opt451", "opt450", "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           qimg(sq24)
           vragen("A. Trabzonspor", "B. Forward Lease Rotterdam", "C. Fenerbahce", "opt450", "opt451", "opt450")
           qmusic()
           pygame.display.flip()
       else:
           print("it no work mayne.")
       return False


def vragen(a,b,c,Aant,Bant,Cant):
    vragenmenu = True
    clock.tick(60)
    while vragenmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(a, qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, white, Aant)
        button(b, qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, white, Bant)
        button(c, qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, white, Cant)
        pygame.display.flip()


Menu()

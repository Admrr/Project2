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
starthetspelnoueens = True
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
player1score = 0
player2score = 0
player3score = 0
player4score = 0
catplr1naam = 'entertainment'
catplr2naam = 'sport'
catplr3naam = 'geschiedenis'
catplr4naam = 'geografie'
tijd = 50
naamvdgame = "naam van de game"
qbuttonwidth = display_height / 1.5
qbuttonheight = 60
qbuttonposx = ((display_width / 2) - (qbuttonwidth / 2))
qbutton1ypos = display_height - (qbuttonheight * 2)
qbutton2ypos = display_height - (qbuttonheight * 3.5)
qbutton3ypos = display_height - (qbuttonheight * 5)
qred = (255, 102, 102)
qlred = (215, 72, 72)
qblue = (102, 178, 255)
qlblue = (71, 145, 220)
qyellow = (235, 235, 32)
qlyellow = (195,195,5)
qgreen = (102, 255, 102)
qlgreen = (60,215,60)
currentcat = 0
black = (0, 0, 0)
white = (255, 255, 255)
blue = (80,80,140)
bright_blue = (130,130,255)
buttonnormal = black
buttonhover = black

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

eq1 = pygame.image.load('Questions/entertainment1.png')
eq2 = pygame.image.load('Questions/entertainment2.png')
eq3 = pygame.image.load('Questions/entertainment3.png')
eq4 = pygame.image.load('Questions/entertainment4.png')
eq5 = pygame.image.load('Questions/entertainment5.png')
eq6 = pygame.image.load('Questions/entertainment6.png')
eq7 = pygame.image.load('Questions/entertainment7.png')
eq8 = pygame.image.load('Questions/entertainment8.png')
eq9 = pygame.image.load('Questions/entertainment9.png')
eq10 = pygame.image.load('Questions/entertainment10.png')
eq11 = pygame.image.load('Questions/entertainment11.png')
eq12 = pygame.image.load('Questions/entertainment12.png')
eq13 = pygame.image.load('Questions/entertainment13.png')
eq14 = pygame.image.load('Questions/entertainment14.png')
eq15 = pygame.image.load('Questions/entertainment15.png')
eq16 = pygame.image.load('Questions/entertainment16.png')
eq17 = pygame.image.load('Questions/entertainment17.png')
eq18 = pygame.image.load('Questions/entertainment18.png')
eq19 = pygame.image.load('Questions/entertainment19.png')
eq20 = pygame.image.load('Questions/entertainment20.png')
eq21 = pygame.image.load('Questions/entertainment21.png')
eq22 = pygame.image.load('Questions/entertainment22.png')
eq23 = pygame.image.load('Questions/entertainment23.png')
eq24 = pygame.image.load('Questions/entertainment24.png')
gq1 = pygame.image.load('Questions/geografie1.png')
gq2 = pygame.image.load('Questions/geografie2.png')
gq3 = pygame.image.load('Questions/geografie3.png')
gq4 = pygame.image.load('Questions/geografie4.png')
gq5 = pygame.image.load('Questions/geografie5.png')
gq6 = pygame.image.load('Questions/geografie6.png')
gq7 = pygame.image.load('Questions/geografie7.png')
gq8 = pygame.image.load('Questions/geografie8.png')
gq9 = pygame.image.load('Questions/geografie9.png')
gq10 = pygame.image.load('Questions/geografie10.png')
gq11 = pygame.image.load('Questions/geografie11.png')
gq12 = pygame.image.load('Questions/geografie12.png')
gq13 = pygame.image.load('Questions/geografie13.png')
gq14 = pygame.image.load('Questions/geografie14.png')
gq15 = pygame.image.load('Questions/geografie15.png')
gq16 = pygame.image.load('Questions/geografie16.png')
gq17 = pygame.image.load('Questions/geografie17.png')
gq18 = pygame.image.load('Questions/geografie18.png')
gq19 = pygame.image.load('Questions/geografie19.png')
gq20 = pygame.image.load('Questions/geografie20.png')
gq21 = pygame.image.load('Questions/geografie21.png')
gq22 = pygame.image.load('Questions/geografie22.png')
gq23 = pygame.image.load('Questions/geografie23.png')
gq24 = pygame.image.load('Questions/geografie24.png')
hq1 = pygame.image.load('Questions/historie1.png')
hq2 = pygame.image.load('Questions/historie2.png')
hq3 = pygame.image.load('Questions/historie3.png')
hq4 = pygame.image.load('Questions/historie4.png')
hq5 = pygame.image.load('Questions/historie5.png')
hq6 = pygame.image.load('Questions/historie6.png')
hq7 = pygame.image.load('Questions/historie7.png')
hq8 = pygame.image.load('Questions/historie8.png')
hq9 = pygame.image.load('Questions/historie9.png')
hq10 = pygame.image.load('Questions/historie10.png')
hq11 = pygame.image.load('Questions/historie11.png')
hq12 = pygame.image.load('Questions/historie12.png')
hq13 = pygame.image.load('Questions/historie13.png')
hq14 = pygame.image.load('Questions/historie14.png')
hq15 = pygame.image.load('Questions/historie15.png')
hq16 = pygame.image.load('Questions/historie16.png')
hq17 = pygame.image.load('Questions/historie17.png')
hq18 = pygame.image.load('Questions/historie18.png')
hq19 = pygame.image.load('Questions/historie19.png')
hq20 = pygame.image.load('Questions/historie20.png')
hq21 = pygame.image.load('Questions/historie21.png')
hq22 = pygame.image.load('Questions/historie22.png')
hq23 = pygame.image.load('Questions/historie23.png')
hq24 = pygame.image.load('Questions/historie24.png')
sq1 = pygame.image.load('Questions/sport1.png')
sq2 = pygame.image.load('Questions/sport2.png')
sq3 = pygame.image.load('Questions/sport3.png')
sq4 = pygame.image.load('Questions/sport4.png')
sq5 = pygame.image.load('Questions/sport5.png')
sq6 = pygame.image.load('Questions/sport6.png')
sq7 = pygame.image.load('Questions/sport7.png')
sq8 = pygame.image.load('Questions/sport8.png')
sq9 = pygame.image.load('Questions/sport9.png')
sq10 = pygame.image.load('Questions/sport10.png')
sq11 = pygame.image.load('Questions/sport11.png')
sq12 = pygame.image.load('Questions/sport12.png')
sq13 = pygame.image.load('Questions/sport13.png')
sq14 = pygame.image.load('Questions/sport14.png')
sq15 = pygame.image.load('Questions/sport15.png')
sq16 = pygame.image.load('Questions/sport16.png')
sq17 = pygame.image.load('Questions/sport17.png')
sq18 = pygame.image.load('Questions/sport18.png')
sq19 = pygame.image.load('Questions/sport19.png')
sq20 = pygame.image.load('Questions/sport20.png')
sq21 = pygame.image.load('Questions/sport21.png')
sq22 = pygame.image.load('Questions/sport22.png')
sq23 = pygame.image.load('Questions/sport23.png')
sq24 = pygame.image.load('Questions/sport24.png')


pagetext = helpmsg1

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def background(x,y):
    scherm.blit(pygame.transform.scale(bgimg, (display_width, display_height)), (0, 0))

def gamebg(x,y):
    scherm.blit(pygame.transform.scale(gamebgimg, (display_width, display_height)), (0, 0))

graadnum = 1
graadtext = "gemiddeld"
def graad():
    time.sleep(0.3)
    global graadnum
    global graadtext, tijd
    graadnum += 1
    if graadnum > 2:
        graadnum = 0
    if graadnum == 0:
        graadtext = "makkelijk"
        tijd = 60
    elif graadnum == 1:
        graadtext = "gemiddeld"
        tijd = 45
    elif graadnum == 2:
        graadtext = "moeilijk"
        tijd = 25

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
    def interact_with_database(command):

        connection = psycopg2.connect('dbname = euromast user=postgres password=123456!qQ')

        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()

        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:

            pass

        cursor.close()
        connection.close()

        return results
    def upload_score(playername, score):
        interact_with_database("UPDATE highscore SET score = {} WHERE playername = '{}'".format(score, playername))
    def download_top_score():
        result = interact_with_database("SELECT * FROM highscore ORDER BY score DESC")
        return result
    topscore = download_top_score()
    iets = topscore
    print(topscore)
    while hsmenu:
        for event in pygame.event.get():
        # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background(0,0)
        button("Vorige", buttonposx, display_width/2, 200, buttonheight, blue, bright_blue, "opt666")
        largeText = pygame.font.Font("pixel.ttf", 80)
        TextSurf, TextRect = text_objects("Scorebord top 5", largeText)
        TextSurf2, TextRect2 = text_objects(str(topscore[0]), largeText)
        TextSurf3, TextRect3 = text_objects(str(topscore[1]), largeText)
        TextSurf4, TextRect4 = text_objects(str(topscore[2]), largeText)
        TextSurf5, TextRect5 = text_objects(str(topscore[3]), largeText)
        TextSurf6, TextRect6 = text_objects(str(topscore[4]), largeText)
        TextRect.center = ((display_width / 2), (100))
        TextRect2.center = ((display_width / 2), 200)
        TextRect3.center = ((display_width / 2), 300)
        TextRect4.center = ((display_width / 2), 400)
        TextRect5.center = ((display_width / 2), 500)
        TextRect6.center = ((display_width / 2), 600)
        scherm.blit(TextSurf, TextRect)
        scherm.blit( TextSurf2, TextRect2)
        scherm.blit( TextSurf3, TextRect3)
        scherm.blit( TextSurf4, TextRect4)
        scherm.blit( TextSurf5, TextRect5)
        scherm.blit( TextSurf6, TextRect6)
        pygame.display.flip()

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
    pygame.mixer.music.unpause()
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
            time.sleep(0.3)
            newgamescherm()
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
        elif click[0] == 1 and action == "opt666":
            time.sleep(0.3)
            optiesmenu()
        elif click[0] == 1 and action == "opt600":
            global movemenu
            movemenu = False
            move("up")
        elif click[0] == 1 and action == "opt601":
            global movemenu
            movemenu = False
            move("down")
        elif click[0] == 1 and action == "opt602":
            global movemenu
            movemenu = False
            move("left")
        elif click[0] == 1 and action == "opt603":
            global movemenu
            movemenu = False
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
            player1score = 0
            player2score = 0
            player3score = 0
            player4score = 0
            pygame.mixer.music.pause()
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
            player1score = 0
            player2score = 0
            player3score = 0
            player4score = 0
            pygame.mixer.music.pause()
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
            player1score = 0
            player2score = 0
            player3score = 0
            player4score = 0
            pygame.mixer.music.pause()
            game_loop()
        elif click[0] == 1 and action == "opt48":
            time.sleep(0.3)
            mainmenu()
        elif click[0] == 1 and action == "opt450":
            print("FOUT")
            global vragenmenu, beurt
            vragenmenu = False
            gamebg(0,0)
            drawboard()
            renderplayer()
            pygame.display.flip()
            largeText = pygame.font.Font("pixel.ttf", 45)
            TextSurf, TextRect = text_objects("vraag fout, beurt gaat naar de volgende", largeText)
            TextRect.center = ((display_width / 2), (200))
            scherm.blit(TextSurf, TextRect)
            pygame.display.flip()
            time.sleep(3.5)
            beurt += 1
        elif click[0] == 1 and action == "opt451":
            print("GOED")
            global vragenmenu, player1score, player2score, player3score, player4score
            vragenmenu = False
            if beurt == 1:
                player1score += 10
            elif beurt == 2:
                player2score += 10
            elif beurt == 3:
                player3score += 10
            elif beurt == 4:
                player4score += 10
            drawboard()
            renderplayer()
            pygame.display.flip()
            time.sleep(0.3)
            playermove()
    else:
        pygame.draw.rect(scherm, ic,(x,y,w,h))

    smallText = pygame.font.Font("pixel.ttf",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scherm.blit(textSurf, textRect)

def winscreen():
    global winner, playername
    global game_loop

    def interact_with_database(command):

        connection = psycopg2.connect('dbname = euromast user=postgres password=123456!qQ')

        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()

        results = None
        try:
            results = cursor.fetchall()
        except psycopg2.ProgrammingError:

            pass

        cursor.close()
        connection.close()

        return results
    def upload_score(playername, score):
        interact_with_database("UPDATE highscore SET score = {} WHERE playername = '{}'".format(score, playername))
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
        score = 0
        if winner == 1:
            winimg = pygame.image.load('winneryellow.png')
            score = player1score
            playername = input("enter your name: ")
            largeText = pygame.font.Font("pixel.ttf", 80)
            TextSurf, TextRect = text_objects( str(playername), largeText)
            TextRect.center = ((display_width / 2), (200))
            scherm.blit(TextSurf, TextRect)
            pygame.display.flip()
            upload_score(playername,player1score)
        elif winner == 2:
            winimg = pygame.image.load('winnerred.png')
            score = player2score
            playername = input("enter your name: ")
            upload_score(playername, player2score)
        elif winner == 3:
            winimg = pygame.image.load('winnerblue.png')
            score = player3score
            playername = input("enter your name: ")
            upload_score(playername, player3score)
        elif winner == 4:
            winimg = pygame.image.load('winnergreen.png')
            score = player4score
            playername = input("enter your name: ")
            upload_score(playername, player4score)


        scherm.blit(pygame.transform.scale(winimg, (display_width, display_height)), (0, 0))

        largeText = pygame.font.Font("pixel.ttf", 50)
        TextSurf, TextRect = text_objects(playername + " wins  "+ "  Score:" + str(score), largeText)
        TextSurf2, TextRect2 = text_objects("druk op spatie om verder te gaan", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        TextRect2.center = ((display_width / 2), (650))
        scherm.blit(TextSurf, TextRect)
        scherm.blit(TextSurf2, TextRect2)
        pygame.display.flip()

def setcat():
    global currentcat, buttonnormal, buttonhover
    if beurt == 1:
        currentcat = catplr1
    elif beurt == 2:
        currentcat = catplr2
    elif beurt == 3:
        currentcat = catplr3
    elif beurt == 4:
        currentcat = catplr4
    if currentcat == 1:
        buttonnormal = qred
        buttonhover = qlred
    if currentcat == 2:
        buttonnormal = qyellow
        buttonhover = qlyellow
    if currentcat == 3:
        buttonnormal = qgreen
        buttonhover = qlgreen
    if currentcat == 4:
        buttonnormal = qblue
        buttonhover = qlblue

def playermove():
    movemenu = True
    while movemenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamebg(0,0)
        drawboard()
        renderplayer()
        huidigebeurt()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pauzemsg()
        button("Boven", buttonposx - 380, 530, 110, buttonheight, blue, bright_blue, "opt600")
        button("Beneden", buttonposx - 380, 600, 110, buttonheight, blue, bright_blue, "opt601")
        button("Links", buttonposx - 500, 600, 110, buttonheight, blue, bright_blue, "opt602")
        button("Rechts", buttonposx - 260, 600, 110, buttonheight, blue, bright_blue, "opt603")
        pygame.display.flip()

def huidigebeurt():
    playername = '.'
    if beurt == 1:
        playername = "Speler geel"
    elif beurt == 2:
        playername = "Speler rood"
    elif beurt == 3:
        playername = "Speler blauw"
    elif beurt == 4:
        playername = "Speler groen"
    smallText = pygame.font.Font("pixel.ttf", 27)
    textSurf, textRect = text_objects("Huidige beurt: " + playername, smallText)
    textRect = (30, 120)
    scherm.blit(textSurf, textRect)

def game_loop():
    gameExit = False
    global startx1,starty1,startx2,starty2,startx3,starty3,startx4,starty4,beurt, starthetspelnoueens
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        gamebg(0,0)
        drawboard()
        if beurt > players:
            beurt = 1
        setcat()
        print(currentcat)
        print(beurt)
        if currentcat == 1:
            imagesq(1,24)
        elif currentcat == 2:
            imagesq(101,124)
        elif currentcat == 3:
           imagesq(201,224)
        elif currentcat == 4:
            imagesq(301,324)

        huidigebeurt()

        renderplayer()
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
    smallText = pygame.font.Font("pixel.ttf", 25)
    if players == 2:
        player1(startx1, starty1)
        player2(startx2, starty2)
        textSurf1, textRect1 = text_objects("score geel: " + str(player1score), smallText)
        textSurf2, textRect2 = text_objects("score rood: " + str(player2score), smallText)
        textRect1 = (30, 160)
        textRect2 = (30, 200)
        scherm.blit(textSurf1, textRect1)
        scherm.blit(textSurf2, textRect2)
    elif players == 3:
        player1(startx1, starty1)
        player2(startx2, starty2)
        player3(startx3, starty3)
        textSurf1, textRect1 = text_objects("score geel: " + str(player1score), smallText)
        textSurf2, textRect2 = text_objects("score rood: " + str(player2score), smallText)
        textSurf3, textRect3 = text_objects("score blauw: " + str(player3score), smallText)
        textRect1 = (30, 160)
        textRect2 = (30, 200)
        textRect3 = (30, 240)
        scherm.blit(textSurf1, textRect1)
        scherm.blit(textSurf2, textRect2)
        scherm.blit(textSurf3, textRect3)
    elif players == 4:
        player1(startx1, starty1)
        player2(startx2, starty2)
        player3(startx3, starty3)
        player4(startx4, starty4)
        textSurf1, textRect1 = text_objects("score geel: " + str(player1score), smallText)
        textSurf2, textRect2 = text_objects("score rood: " + str(player2score), smallText)
        textSurf3, textRect3 = text_objects("score blauw: " + str(player3score), smallText)
        textSurf4, textRect4 = text_objects("score groen: " + str(player4score), smallText)
        textRect1 = (30, 160)
        textRect2 = (30, 200)
        textRect3 = (30, 240)
        textRect4 = (30, 280)
        scherm.blit(textSurf1, textRect1)
        scherm.blit(textSurf2, textRect2)
        scherm.blit(textSurf3, textRect3)
        scherm.blit(textSurf4, textRect4)

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
    time.sleep(1)
    game_loop()

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


def qimg(img):
    scherm.blit(img, (display_width / 2.78, display_height / 3.6))

def imagesq(min,max):
    global buttonnormal, buttonhover, questmenu, questimg
    questmenu = True
    while questmenu:
        def qmusic():
            pass
            #pygame.mixer.music.load('8bitquestion.mp3')
            #pygame.mixer.music.play(loops=1, start=0.0)


        n = random.randint(min, max)
        for abc in range(0,1):
            if n == 1:
                questimg = eq1
                # A is juist
                vragen("A. De Witte Aap", "B. Het NRC", "C. Café de Beurs", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 2:
                questimg = eq2
                # B is juist
                vragen("A. R'dam Escape", "B. Escape010", "C. Room Escape", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 3:
                # C is juist
                questimg = eq3
                vragen("A. Segway", "B. Boot", "C. Auto", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 4:
                # B is juist
                questimg = eq4
                vragen("A. H&M", "B. Mediamarkt", "C. The Sting", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 5:
                # A is juist
                questimg = eq5
                vragen("A. Cinerama", "B. Pathe De Kuip", "C. Pathe Schouwburgplein", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 6:
                # C is juist
                questimg = eq6
                vragen("A. Havenmuseum", "B. Mariniersmuseum", "C. Maritiemmuseum", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 7:
                # C is juist
                questimg = eq7
                vragen("A. De Euromast", "B. Museumplein", "C. De Markthal", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 8:
                # B is juist
                questimg = eq8
                vragen("A. Pathe de Kuip", "B. Pathe de Kroon", "C. Pathe Schouwburgplein", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 9:
                # A is juist
                questimg = eq9
                vragen("A. 925000 bezoekers", "B. 675000 bezoekers", "C. 830000 bezoekers", "opt451", "opt450",
                       "opt450")
                qmusic()

            elif n == 10:
                questimg = eq10
                # B is juist
                vragen("A. Hoek van Holland", "B. Euromast Park", "C. Plaswijckpark", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 11:
                # A is juist
                questimg = eq11
                vragen("A. Luxemburg en België", "B. Duitsland en België", "C. Duitsland en Frankrijk", "opt451",
                       "opt450",
                       "opt450")
                qmusic()

            elif n == 12:
                questimg = eq12
                # C is juist
                vragen("A. Drive & Eat", "B. Bicycle Diner", "C. Bike & Bite", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 13:
                # A is juist
                questimg = eq13
                vragen("A. De Zwanenboot", "B. De Pannenkoekenboot", "C. De Berenboot", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 14:
                # C is juist
                questimg = eq14
                vragen("A. Cinerama", "B. Pathe de Kuip", "C. LantarenVenster", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 15:
                questimg = eq15
                # A is juist
                vragen("A. Mullerpier", "B. Pier 80", "C. Schouwburgplein", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 16:
                # A is juist
                questimg = eq16
                vragen("A. De Witte de Withstraat", "B. Kruiskade", "C. Doedesstraat", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 17:
                # C is juist
                questimg = eq17
                vragen("A. Willemsbrug", "B. Spaansebrug", "C. Erasmusbrug", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 18:
                # C is juist
                questimg = eq18
                vragen("A. Noordelijk Film Festival", "B. Vlier Film Festival", "C. Internationaal Film Festival",
                       "opt450",
                       "opt450", "opt451")
                qmusic()

            elif n == 19:
                # A is juist
                questimg = eq19
                vragen("A. Diergaarde Blijdorp", "B. Plaswijckpark", "C. Utropia", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 20:
                # A is juist
                questimg = eq20
                vragen("A. De Markthal", "B. De Verwoeste Stad", "C. De Boeg", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 21:
                # B is juist
                questimg = eq21
                vragen("A. Wijnhaven", "B. Rijnhaven", "C. Parkhaven", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 22:
                # B is juist
                questimg = eq22
                vragen("A. Rotterdam Creeper Walk", "B. Rotterdam Zombie Walk", "C. Rotterdam Undead Walk", "opt450",
                       "opt451", "opt450")
                qmusic()

            elif n == 23:
                # C is juist
                questimg = eq23
                vragen("A. Rotterdam Gaypride", "B. Rotterdam LGBT Parade", "C. Rotterdam Pride", "opt450", "opt450",
                       "opt451")
                qmusic()

            elif n == 24:
                # B is juist
                questimg = eq24
                vragen("A. Januari", "B. September", "C. Mei", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 101:
                questimg = hq1
                vragen("A. Kooplieden hadden dit vroeger bedacht", "B. Aan de rivier de rotte",
                       "C. Er was een dam aangelegd in de maas", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 102:
                questimg = hq2
                vragen("A. De oude haven", "B. VOC magazijn", "St. Laurenskerk", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 103:
                questimg = hq3
                vragen("A. Ahmed Aboutaleb", "B. Jules Deelder", "C. Willem Alexander", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 104:
                questimg = hq4
                vragen("A. Waar", "B. Niet Waar", "C. Weet ik niet", "opt451", "opt450", "op450")
                qmusic()

            elif n == 105:
                questimg = hq5
                vragen("A. De beste bakker van de stad was daar gevestigd", "B. De prostituees",
                       "C. De oudste beschermde boom van de stad staat daar", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 106:
                questimg = hq6
                vragen("A. 1855", "B. 1975", "C. 1915", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 107:
                questimg = hq7
                vragen("A. De ondergrondse winkelstraat", "B. Beurstraverse", "C. Gewoon de koopgoot", "opt450",
                       "opt451",
                       "opt450")
                qmusic()

            elif n == 108:
                questimg = hq8
                vragen("A. De Bijenkorf", "B. De Kubuswoningen", "C. The Red Apple", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 109:
                questimg = hq9
                vragen("A. 5000", "B. 8000", "C. 12000", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 110:
                questimg = hq10
                vragen("A. De nieuwe Binnenweg", "B. Maasbrug", "C. Koninginnenbrug", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 111:
                questimg = hq11
                vragen("A. Suiker", "B. Wol", "C. Cacao", "opt451", "opt451", "opt450")
                qmusic()

            elif n == 112:
                questimg = hq12
                vragen("A. De Nieuwe Waterweg", "B. De Maas zeeverbinding", "C. Het Nieuwe Water kanaal", "opt451",
                       "opt450",
                       "opt450")
                qmusic()

            elif n == 113:
                questimg = hq13
                vragen("A. Maaskant", "B. Brinkman en van der Vlugt", "C. Koolhaas", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 114:
                questimg = hq14
                vragen("A. 1250", "B. 1340", "C. 1590", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 115:
                questimg = hq15
                vragen("A. Waalhaven", "B. De Maashaven", "C. Europoort", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 116:
                questimg = hq16
                vragen("A. GroenLinks", "B. DENK", "C. Leefbaar Rotterdam", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 117:
                questimg = hq17
                vragen("A. Loods 21", "B. Loods 5", "C. Loods 24", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 118:
                questimg = hq18
                vragen("A. Nederland-Amerika Lijn", "B. Holland-Amerika Lijn", "C. Rotterdam-Amerika Lijn", "opt450",
                       "opt451", "opt450")
                qmusic()

            elif n == 119:
                questimg = hq19
                vragen("A. NRC", "B. De Telegraaf", "C. Metro", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 120:
                questimg = hq20
                vragen("A. Nieuwe Roddel Courant", "B. Nieuwe Rotterdamsche Courant", "Nieuwe Reactie Courant",
                       "opt450",
                       "opt451", "opt450")
                qmusic()

            elif n == 121:
                questimg = hq21
                vragen("A. Blaak 6", "B. Markthal", "C. Het witte Huis", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 122:
                questimg = hq22
                vragen("A. 1939-1946", "B. 1935-1940", "C. 1940-1945", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 123:
                questimg = hq23
                vragen("A. De verwoeste Stad", "B. Kabouter Buttplug", "C. Erasmusbeeld", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 124:
                questimg = hq24
                vragen("A. Nederland-Amerika lijn", "B. Rotterdam-Amerika Lijn", "C. Holland-Amerika lijn", "opt450",
                       "opt450", "opt451")
                qmusic()

            elif n == 201:
                questimg = gq1
                vragen("A. Kerktoren hillegondakerk", "B. St. Laurenskerk.", "C. Stadhuis van Rotterdam", "opt451",
                       "opt450",
                       "opt450")
                qmusic()

            elif n == 202:
                questimg = gq2
                vragen("A. 800.000", "B. 900.000", "C. 1.000.000", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 203:
                questimg = gq3
                vragen("A. De Willemsbrug", "B. De Koninginnebrug", "C. De van Briennenoordbrug", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 204:
                questimg = gq4
                vragen("A. Stad der Wonderen", "B. Stad der Steden", "C. Havenstad", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 205:
                questimg = gq5
                vragen("A. Noord-Holland", "B. Zuid-Holland", "C. Noord-Brabant", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 206:
                questimg = gq6
                vragen("A. De Maas", "B. De Rijn", "C. De Waal", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 207:
                questimg = gq7
                vragen("A. 50 tot 60km", "B. 60 tot 70km", "C. 70 tot 80km", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 210:
                questimg = gq10
                vragen("A. Waar", "B. Niet Waar", "C. Weet Niet", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 208:
                questimg = gq8
                vragen("A. De Willemsbrug", "B. De Erasmusbrug", "C. De van Briennenoordbrug", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 209:
                questimg = gq9
                vragen("A. waar", "B. niet waar", "C. weet ik niet", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 211:
                questimg = gq11
                vragen("A. Waar", "B. Niet Waar", "C. Weet Niet", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 212:
                questimg = gq12
                vragen("A. Waar", "B. Niet waar", "C. Weet Niet", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 213:
                questimg = gq13
                vragen("A. Metro", "B. Auto", "C. Fiets", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 214:
                questimg = gq14
                vragen("A. 760 tot 780mm", "B. 780 tot 800mm", "C. 800 tot 820mm", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 215:
                questimg = gq15
                vragen("A. 150.000", "B. 300.000", "C. 450.000", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 216:
                questimg = gq16
                vragen("A. 327,6 km2", "B. 319,4 km2", "C. 352,8 km2", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 217:
                questimg = gq17
                vragen("A. 180 meter", "B. 195 meter", "C. 185 meter", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 218:
                questimg = gq18
                vragen("A. De Maastoren", "B. De Boeg", "C. Euromast", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 219:
                questimg = gq19
                vragen("A. Markthalwoningen", "B. Blaakwoningen", "C. De Kubuswoningen", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 220:
                questimg = gq20
                vragen("A. De Rotterdamse berg", "B. De Courantse berg", "C. Rotterdam heeft geen bergen", "opt450",
                       "opt450", "opt451")
                qmusic()

            elif n == 221:
                questimg = gq21
                vragen("A. Koopgoot kerstboom", "B. Kabouter Buttplug", "C. Erasmus kerstboom", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 222:
                questimg = gq22
                vragen("A. Rotterdam is de grootste stad van Nederland", "B. Den Haag", "C. Amsterdam", "opt451",
                       "opt450",
                       "opt450")
                qmusic()

            elif n == 223:
                questimg = gq23
                vragen("A. Tropisch klimaat", "B. Droog klimaat", "C. Gematigd klimaat", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 224:
                questimg = gq24
                vragen("A. De Willemsbrug", "B. De Erasmusbrug", "C. De Hef", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 301:
                questimg = sq1
                vragen("A. 2000", "B. 2005", "C. 2010", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 302:
                questimg = sq2
                vragen("A. ABN AMRO World Tennis Tournament", "B. Ahoy Open", "C. Heineken Open", "opt451", "opt450",
                       "opt450")
                qmusic()

            elif n == 303:
                questimg = sq3
                vragen("A. HVGR", "B. Focus", "C. HC Rotterdam", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 304:
                questimg = sq4
                vragen("A. Fitness", "B. Voetbal", "C. Basketbal", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 305:
                questimg = sq5
                vragen("A. Dorian van Rijsselberghe", "B. Marhinde Verkerk", "C. Edith Bosch", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 306:
                questimg = sq6
                vragen("A. Willem Alexander baan", "B. Beatrix baan", "C. Juliana baan", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 307:
                questimg = sq7
                vragen("A. Watersporten, Wielrennen en hardlopen", "B. Voetbal, Hockey en basketbal",
                       "C. Fitness, hardlopen en basketbal", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 308:
                questimg = sq8
                vragen("A. Rechtsback", "B. Linksback", "C. Linksbuiten", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 311:
                questimg = sq11
                vragen("A. 42,125 km", "B. 42,450 km", "C. 42,680 km", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 309:
                questimg = sq9
                vragen("A. Zich verder van het doel bevindt dan de keeper.",
                       "B. Zich dichter bij de doellijn van de tegenstander bevindt dan de bal en de vóórlaatste tegenstander.",
                       "C. Zich buiten de lijn van het veld bevindt en de bal in het spel is.", "opt450", "opt451",
                       "opt450")
                qmusic()

            elif n == 310:
                questimg = sq10
                vragen("A. De Toren", "B. Het Kasteel", "C. De Arena", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 312:
                questimg = sq12
                vragen("A. 9", "B. 10", "C. 11", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 313:
                questimg = sq13
                vragen("A. 1850", "B. 1875", "C. 1900", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 314:
                questimg = sq14
                vragen("A. Waar", "B. Niet waar", "C. Even groot", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 315:
                questimg = sq15
                vragen("A. 1", "B. 2", "C. 3", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 316:
                questimg = sq16
                vragen("A. 1", "B. 3", "C. 2", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 317:
                questimg = sq17
                vragen("A. Sparta Rotterdam", "B. Excelsior", "C. Feyenoord", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 318:
                questimg = sq18
                vragen("A. Alley-oop", "B. Dunk", "C. Smash", "opt450", "opt451", "opt450")
                qmusic()

            elif n == 319:
                questimg = sq19
                vragen("A. Eenpuntlijn", "B. Tweepuntslijn", "C. Driepuntslijn", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 320:
                questimg = sq20
                vragen("A. Honkbal", "B. Softbal", "C. Voetbal", "opt450", "opt450", "opt451")
                qmusic()

            elif n == 321:
                questimg = sq21
                vragen("A. Pathe Schouwburgplein", "B. KFC", "C. Topsportcentrum Rotterdam", "opt450", "opt450",
                       "opt451")
                qmusic()

            elif n == 322:
                questimg = sq22
                vragen("A. City Racing Rotterdam", "B. Rotterdam Racing through the City", "C. F1: Rotterdam", "opt451",
                       "opt450", "opt450")
                qmusic()

            elif n == 323:
                questimg = sq23
                vragen("A. Dutch Basketball League", "B. NBA", "C. Basketball League A1", "opt451", "opt450", "opt450")
                qmusic()

            elif n == 324:
                questimg = sq24
                vragen("A. Trabzonspor", "B. Forward Lease Rotterdam", "C. Fenerbahce", "opt450", "opt451", "opt450")
                qmusic()

        questmenu = False



def vragen(a,b,c,Aant,Bant,Cant):
    global questmenu, vragenmenu, questimg, beurt
    vragenmenu = True
    counter, text = tijd, str(tijd).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 100)
    font = pygame.font.Font('pixel.ttf', 35)
    clock.tick(60)
    while vragenmenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.USEREVENT:
                counter -= 0.1
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pauzemsg()
                gamebg(0, 0)
                drawboard()
                huidigebeurt()
                renderplayer()
                qimg(questimg)
                button(a, qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, buttonnormal, buttonhover, Aant)
                button(b, qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, buttonnormal, buttonhover, Bant)
                button(c, qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, buttonnormal, buttonhover, Cant)
                text = str(round(counter,1)).rjust(3) if counter > 0 else "0".rjust(3)
                pygame.display.flip()
            if counter < 1:
                questmenu = False
                vragenmenu = False
                gamebg(0,0)
                drawboard()
                renderplayer()
                huidigebeurt()
                largeText = pygame.font.Font("pixel.ttf", 45)
                TextSurf, TextRect = text_objects("tijd is op!, beurt gaat naar de volgende", largeText)
                TextRect.center = ((display_width / 2), (200))
                scherm.blit(TextSurf, TextRect)
                pygame.display.flip()
                time.sleep(3.5)
                beurt += 1
            if event.type == pygame.QUIT: break
        else:
            pygame.draw.rect(scherm, (255/((counter/20)+1), 215, 20), [30, 25, counter * 10, 75])
            scherm.blit(font.render(text, True, (0, 0, 0)), (32, 48))
            pygame.display.flip()
            clock.tick(60)
            continue



def Menu():
    introscherm()
Menu()


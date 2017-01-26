import pygame, random, time


pygame.init()

display_height = 720
display_width = int(display_height * 1.77777778)
scherm = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
white = (205,205,205)
intro = True
antwoord = False
qbuttonwidth = display_height / 1.5
qbuttonheight = 60
qbuttonposx = ((display_width / 2) - (qbuttonwidth / 2))
qbutton1ypos = display_height - (qbuttonheight * 2)
qbutton2ypos = display_height - (qbuttonheight * 3.5)
qbutton3ypos = display_height - (qbuttonheight * 5)
qred = (255, 102, 102)
qblue = (102, 178, 255)
qyellow = (255, 255, 102)
qgreen = (102, 255, 102)

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(scherm, ac,(x,y,w,h))

        #Code is niet functioneel maar met de hulp van jullie zullen we dit functioneel maken.
        if click[0] == 1 and action == "opt450":
            print("FOUT")
            #Foute antwoord
        elif click[0] == 1 and action == "opt451":
            print("GOED")
            #Goede antwoord

    else:
        pygame.draw.rect(scherm, ic,(x,y,w,h))

    smallText = pygame.font.Font(None ,25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scherm.blit(textSurf, textRect)

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
       n = 24
       if n == 1:
            qimg(eq1)
            #A is juist
            button("A. De Witte Aap", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred , qred, "opt451")
            button("B. Het NRC", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
            button("C. Café de Beurs", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
            qmusic()
            pygame.display.flip()
       elif n == 2:
           qimg(eq2)
           #B is juist
           button("A. R'dam Escape", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Escape010", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. Room Escape", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           #C is juist
           qimg(eq3)
           button("A. Segway", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Boot", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Auto", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           #B is juist
           qimg(eq4)
           button("A. H&M", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Mediamarkt", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. The Sting", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           #A is juist
           qimg(eq5)
           button("A. Cinerama", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. Pathe De Kuip", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Pathe Schouwburgplein", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           #C is juist
           qimg(eq6)
           button("A. Havenmuseum", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Mariniersmuseum", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Maritiemmuseum", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           #C is juist
           qimg(eq7)
           button("A. De Euromast", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Museumplein", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. De Markthal", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           #B is juist
           qimg(eq8)
           button("A. Pathe de Kuip", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Pathe de Kroon", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. Pathe Schouwburgplein", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           #A is juist
           qimg(eq9)
           button("A. 925000 bezoekers", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. 675000 bezoekers", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. 830000 bezoekers", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(eq10)
           #B is juist
           button("A. Hoek van Holland", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Euromast Park", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. Plaswijckpark", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           #A is juist
           qimg(eq11)
           button("A. Luxemburg en België", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. Duitsland en België", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Duitsland en Frankrijk", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(eq12)
           #C is juist
           button("A. Drive & Eat", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Bicycle Diner", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Bike & Bite", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           #A is juist
           qimg(eq13)
           button("A. De Zwanenboot", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. De Pannenkoekenboot", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. De Berenboot", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           #C is juist
           qimg(eq14)
           button("A. Cinerama", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Pathe de Kuip", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. LantarenVenster", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(eq15)
           #A is juist
           button("A. Mullerpier", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. Pier 80", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Schouwburgplein", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           #A is juist
           qimg(eq16)
           button("A. De Witte de Withstraat", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. Kruiskade", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Doedesstraat", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           #C is juist
           qimg(eq17)
           button("A. Willemsbrug", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Spaansebrug", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Erasmusbrug", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           #C is juist
           qimg(eq18)
           button("A. Noordelijk Film Festival", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Vlier Film Festival", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Internationaal Film Festival", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           #A is juist
           qimg(eq19)
           button("A. Diergaarde Blijdorp", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. Plaswijckpark", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Utropia", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           #A is juist
           qimg(eq20)
           button("A. De Markthal", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("B. De Verwoeste Stad", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. De Boeg", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           #B is juist
           qimg(eq21)
           button("A. Wijnhaven", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Rijnhaven", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. Parkhaven", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           #B is juist
           qimg(eq22)
           button("A. Rotterdam Creeper Walk", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Rotterdam Zombie Walk", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           button("C. Rotterdam Undead Walk", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           #C is juist
           qimg(eq23)
           button("A. Rotterdam Gaypride", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("B. Rotterdam LGBT parade", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt450")
           button("C. Rotterdam Pride", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qred, qred, "opt451")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           #B is juist
           qimg(eq24)
           vragen("A. Januari","B. September","C. Mei","opt450", "opt451", "opt450")
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


def timer():
    while antwoord == False:
        pass


def loop():
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scherm.fill(white)
        clock.tick(30)
        while True:

            imagesq()
            timer()
            return False
        pygame.display.flip()

loop()
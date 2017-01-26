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

def cat():

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
           button("A. Kerktoren hillegondakerk", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. St. Laurenskerk.", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Stadhuis van Rotterdam", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 2:
           qimg(gq2)
           button("A. 800.000", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 900.000", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. 1.000.000", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           qimg(gq3)
           button("A. De Willemsbrug", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. De Koninginnebrug", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. De van Briennenoordbrug", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           qimg(gq4)
           button("A. Stad der Wonderen", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Stad der Steden", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Havenstad", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           qimg(gq5)
           button("A. Noord-Holland", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Zuid-Holland", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. Noord-Brabant", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           qimg(gq6)
           button("A. De Maas", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. De Rijn", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. De Waal", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           qimg(gq7)
           button("A. 50 tot 60km", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 60 tot 70km", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. 70 tot 80km", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           qimg(gq8)
           button("A. De Witte Aap", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Het NRC", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. Café de Beurs", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt3")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           qimg(gq9)
           button("A. De Willemsbrug", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. De Erasmusbrug", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. De van Briennenoordbrug", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(gq10)
           button("A. Waar", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Niet waar", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           qimg(gq11)
           button("A. Waar", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Niet Waar", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(gq12)
           button("A. Waar", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Niet waar", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           qimg(gq13)
           button("A. Metro", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Auto", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Fiets", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           qimg(gq14)
           button("A. 760 tot 780mm", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 780 tot 800mm", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. 800 tot 820mm", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(gq15)
           button("A. 150.000", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 300.000", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. 450.000", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           qimg(gq16)
           button("A. 327,6 km2", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 319,4 km2", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. 352,8 km2", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           qimg(gq17)
           button("A. 180 meter", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 195 meter", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. 185 meter", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           qimg(gq18)
           button("A. De Maastoren", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. De Boeg", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Euromast", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           qimg(gq19)
           button("A. Markthalwoningen", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Blaakwoningen", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. De Kubuswoningen", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           qimg(gq20)
           button("A. De Rotterdamse berg", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. De Courantse berg", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Rotterdam heeft geen bergen", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           qimg(gq21)
           button("A. Koopgoot kerstboom", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Kabouter Buttplug", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. Erasmus kerstboom", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           qimg(gq22)
           button("A. Rotterdam is de grootste stad van Nederland", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("B. Den Haag", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Amsterdam", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           qimg(gq23)
           button("A. Tropisch klimaat", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. Droog klimaat", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. Gematigd klimaat", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           qimg(gq24)
           button("A. De Willemsbrug", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. De Erasmusbrug", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           button("C. De Hef", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 1:
           qimg(sq1)
           button("A. 2000", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("B. 2005", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt450")
           button("C. 2010", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qgreen, qgreen, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 2:
           qimg(sq2)
           button("A. ABN AMRO World Tennis Tournament", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. Ahoy Open", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Heineken Open", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 3:
           qimg(sq3)
           button("A. HVGR", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Focus", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. HC Rotterdam", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 4:
           qimg(sq4)
           button("A. Fitness", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. Voetbal", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Basketbal", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 5:
           qimg(sq5)
           button("A. Dorian van Rijsselberghe", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Marhinde Verkerk", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. Edith Bosch", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 6:
           qimg(sq6)
           button("A. Willem Alexander baan", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. Beatrix baan", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Juliana baan", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 7:
           qimg(sq7)
           button("A. Watersporten, Wielrennen en hardlopen", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. Voetbal, Hockey en basketbal", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Fitness, hardlopen en basketbal", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 8:
           qimg(sq8)
           button("A. Rechtsback", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Linksback", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Linksbuiten", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 11:
           qimg(sq11)
           button("A. 42,125 km", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. 42,450 km", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. 42,680 km", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 9:
           qimg(sq9)
           button("A. Zich verder van het doel bevindt dan de keeper.", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Zich dichter bij de doellijn van de tegenstander bevindt dan de bal en de vóórlaatste tegenstander.", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. Zich buiten de lijn van het veld bevindt en de bal in het spel is.", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 10:
           qimg(sq10)
           button("A. De Toren", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Het Kasteel", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. De Arena", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 12:
           qimg(sq12)
           button("A. 9", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. 10", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. 11", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 13:
           qimg(sq13)
           button("A. 1850", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. 1875 ", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. 1900", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 14:
           qimg(sq14)
           button("A. Waar", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Niet waar", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. Even groot", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 15:
           qimg(sq15)
           button("A. 1", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. 2", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. 3", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 16:
           qimg(sq16)
           button("A. 1", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. 3", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. 2", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 17:
           qimg(sq17)
           button("A. Sparta Rotterdam", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Excelsior", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Feyenoord", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 18:
           qimg(sq18)
           button("A. Alley-oop", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Dunk", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. Smash", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 19:
           qimg(sq19)
           button("A. Eenpuntlijn", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Tweepuntslijn", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Driepuntslijn", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 20:
           qimg(sq20)
           button("A. Honkbal", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Softbal", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Voetbal", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 21:
           qimg(sq21)
           button("A. Pathe Schouwburgplein", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. KFC", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Topsportcentrum Rotterdam", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 22:
           qimg(sq22)
           button("A. City Racing Rotterdam", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. Rotterdam Racing through the City", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. F1: Rotterdam", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 23:
           qimg(sq23)
           button("A. Dutch Basketball League", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("B. NBA", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("C. Basketball League A1", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
           qmusic()
           pygame.display.flip()
       elif n == 24:
           qimg(sq24)
           button("A. Trabzonspor", qbuttonposx, qbutton1ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           button("B. Forward Lease Rotterdam", qbuttonposx, qbutton2ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt451")
           button("C. Fenerbahce", qbuttonposx, qbutton3ypos, qbuttonwidth, qbuttonheight, qblue, qblue, "opt450")
           vragen("", "", "", "", "", "")
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

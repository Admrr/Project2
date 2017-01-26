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
    pass
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

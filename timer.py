v=def mainmenu():
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
        elif keys[pygame.K_1]:
            timer() #call TIMER



        pygame.display.flip()

def timer():
    counter, text = 50,'50'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    var = True
    while var:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else "0".rjust(3)
            if counter < 1:
                var = False
            if e.type == pygame.QUIT: break
        else:
            pygame.draw.rect(scherm, (250, 250, 250), [30, 25, 75, 75])
            scherm.blit(font.render(text, True, (0, 0, 0)), (32, 48))
            pygame.display.flip()
            clock.tick(60)
            continue

    pygame.display.flip()
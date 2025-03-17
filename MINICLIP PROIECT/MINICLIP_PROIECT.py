import tkinter as tk
import pygame
from PIL import Image, ImageTk

def play_rapid_fire_game(screen):
    import pygame
    import random
    import time
    import sys
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    running = True
    tinta=[pygame.image.load("tinta.png"),pygame.image.load("tinta.png"),pygame.image.load("tinta.png"),pygame.image.load("tinta.png")]
    i=0
    for i in range(4):
        tinta[i]=pygame.transform.scale(tinta[i],(100,100))
    pygame.display.set_caption("Joc")
    inaltime=80 / 100 * screen.get_height()
    panel1 = pygame.Surface((screen.get_width(), inaltime))
    panel2 = pygame.Surface((screen.get_width(), 20 / 100 * screen.get_height()))
    inaltimi=[-200,-200,-200,-200]
    latimi=[random.randrange(0,1180),random.randrange(0,1180),random.randrange(0,1180),random.randrange(0,1180)]
    viteze=[-1,-1,1,1]
    punctaj=0
    punctajramas=200
    timp=30
    t=timp*120
    punctajlocal=0
    nivel=1
    punctajramas1=punctajramas
    vitezaprinci=1
    incrementator=0
    cursor=pygame.image.load("crosshair.png")
    cursor=pygame.transform.scale(cursor,(100,100))
    user_text=''
    input_rect=pygame.Rect(350,30,200,32)
    runningclas=True
    img=pygame.image.load("pozameniu.jpg")
    with open("clasament.txt", "r") as file:
        content = file.read()
    lines = content.splitlines()
    nrlinii=len(content)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
  
            if event.type == pygame.KEYDOWN:
  
                if event.key == pygame.K_BACKSPACE:
  
                    user_text = user_text[:-1]
  
                else:
                    user_text += event.unicode  
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if(pos[0]>=550 and pos[0]<=600 and pos[1]>=30 and pos[1]<=62):
                    running=False
      
        screen.blit(img,(0,0))
        mesaj1= font.render("Introduceti numele:",True, "black", "grey")
        screen.blit(mesaj1,(10,30))
        pygame.draw.rect(screen,"grey",input_rect)
        pygame.draw.rect(screen,"red",pygame.Rect(550,30,50,32))
        textulet=font.render("GO!",True, "black", "red")
        text_surface = font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y))
        screen.blit(textulet,(550,30))
        pygame.display.flip() 

    gasit =0
    i=0
    with open('clasament.txt') as f:
        contents = f.readline()
        a=contents.split()
        if(contents!=''and a[0]==user_text):
            gasit=1
            punctajgasit=int(a[1])
            liniegasit=i
        i=i+1

    running=True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if(pos[0]>=20 and pos[0]<=220 and pos[1]>=20 and pos[1]<=70):
                    running=False
                    runningclas=False
                if(pos[0]>=20 and pos[0]<=220 and pos[1]>=80 and pos[1]<=130):
                    running=False
        img=pygame.image.load("pozameniu.jpg")
        screen.blit(img,(0,0))
        pygame.draw.rect(screen, "grey",pygame.Rect(20,20,200,50))
        pygame.draw.rect(screen, "grey",pygame.Rect(20,80,200,50))
        mesaj1= font.render("PLAY",True, "black", "grey")
        font1 = pygame.font.Font('freesansbold.ttf', 28)
        mesaj2= font1.render("Leaderboards",True, "black", "grey")
        screen.blit(mesaj1,(70,30))
        screen.blit(mesaj2,(22,90))
        pygame.display.flip()

    while runningclas:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(img,(0,0))
    
        pygame.draw.rect(screen, "white",pygame.Rect(200,200,880,500))
    
        fontclasament=pygame.font.Font(None, 32)
        for i, line in enumerate(lines):
            mesajclasament=fontclasament.render(lines[i],True,"black","white")
            screen.blit(mesajclasament,(220,220+i*32))
    
        pygame.display.flip()

    pygame.mouse.set_visible(False)
    running=True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pos=pygame.mouse.get_pos()
                    btn=pygame.mouse
                    i=0
                    punctajlocal=0
                    for i in range(4):
                        if pos[0]>=latimi[i] and pos[0]<=latimi[i]+100 and pos[1]>=inaltimi[i] and pos[1]<=inaltimi[i]+100:
                            punctajlocal=punctajlocal+incrementator+1
                            if pos[0]>=latimi[i]+20 and pos[0]<=latimi[i]+80 and pos[1]>=inaltimi[i]+20 and pos[1]<=inaltimi[i]+80:
                                punctajlocal=punctajlocal+incrementator +4
                            if pos[0]>=latimi[i]+40 and pos[0]<=latimi[i]+60 and pos[1]>=inaltimi[i]+40 and pos[1]<=inaltimi[i]+60:
                                punctajlocal=punctajlocal+incrementator+5
                            punctajramas=punctajramas-punctajlocal
                            if(punctajramas<=0):
                                nivel=nivel+1
                                punctajramas=punctajramas1+50
                                punctajramas1=punctajramas
                                timp=timp-5
                                t=timp*120
                                i=0
                                incrementator=incrementator+1
                                vitezaprinci=vitezaprinci+1
                                for i in range(4):
                                    if viteze[i]>0:
                                        viteze[i]=vitezaprinci
                                    else:
                                        viteze[i]=-vitezaprinci
                            punctaj=punctaj+punctajlocal
                            inaltimi[i]=-200
                            latimi[i]=random.randrange(0,1180)
                            panel1.blit(tinta[i],(latimi[i],inaltimi[i]))

        i=0
        for i in range(4):
            if latimi[i]>=screen.get_width()-100:
                viteze[i]=-vitezaprinci
            if latimi[i]<=0:
                viteze[i]=vitezaprinci
            if inaltimi[i] >= panel1.get_height():
                inaltimi[i]=-200
    

        screen.fill("white")
        panel1.fill("red")
        panel2.fill("blue")

        mins= divmod(t, 120)
        mesaj1= font.render("Secunde:{}".format(mins[0]),True, "green", "blue")
        mesaj2= font.render("Punctaj ramas:{}".format(punctajramas),True,"green","blue")
        mesaj3= font.render("Nivel:{}".format(nivel),True, "green", "blue")
        panel2.blit(mesaj1,(0,32))
        panel2.blit(mesaj2,(0,64))
        panel2.blit(mesaj3,(0,96))
        t -= 1

        for i in range(4):
            latimi[i]=latimi[i]+viteze[i]
            inaltimi[i]=inaltimi[i]+1

        for i in range(4):
            panel1.blit(tinta[i],(latimi[i],inaltimi[i]))
    
        mesaj= font.render("Punctaj:{0}".format(punctaj),True, "green", "blue")
        panel2.blit(mesaj,(0,0))
        pozitiemouse=pygame.mouse.get_pos()
        screen.blit(panel1,(0,0))
        screen.blit(panel2,(0,panel1.get_height()))
        screen.blit(cursor,(pozitiemouse[0]-50,pozitiemouse[1]-50))
    
        clock.tick(120)
        if(t<=0):
            running=False
        pygame.display.flip()

    pygame.mouse.set_visible(True)

    running=True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("white")
        mesaj=font.render("Ati acumulat:{0} puncte".format(punctaj),True, "black")
        screen.blit(mesaj,(screen.get_width()/2-200,screen.get_height()/2))
        pygame.display.flip()

    if(gasit==0):
        file1=open("clasament.txt","a")
        file1.write("{} {}\n".format(user_text,punctaj))
        file1.close()
    file1=open("clasament.txt","r")
    fisier=file1.readlines()
    file1.close
    if(gasit==1 and punctaj > punctajgasit):
        linie="{} {}\n".format(user_text,punctaj)
        fisier[liniegasit]=linie
    nrlinii=len(fisier)
    for i in range(nrlinii-1):
        j=i+1
        while j<nrlinii:
            a=fisier[i].split()
            b=fisier[j].split()
            if(int(a[1])<int(b[1])):
                aux=fisier[i]
                fisier[i]=fisier[j]
                fisier[j]=aux
            j=j+1
    file1=open("clasament.txt","w")
    for j in range(nrlinii):
        file1.write(fisier[j])
    file1.close()
    pygame.quit()
    pass

def play_tanks_game(screen):
    import pygame
    import time
    import random
    pygame.init()
    display_width =  800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width, display_height)) 
    background_image = pygame.image.load("joc2.jpg")
    background_image = pygame.transform.scale(background_image, (display_width, display_height))
    #----------------------------------------colors----------------------------------------------
    wheat=(245,222,179)
    power_colour1=(157, 192, 139)
    power_colour2=(96, 153, 102)
    power_colour3=(64, 81, 59)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0,0,255)
    fire_blue=(2, 84, 100)
    orange=(255, 133, 81)
    fire_orange=(229, 124, 35)
    red = (200, 0, 0)
    light_red = (255, 0, 0)
    yellow = (200, 200, 0)
    light_yellow = (255, 255, 0)
    tank_green=(23, 89, 74)
    green = (34, 177, 76)
    light_green = (0, 255, 0)
    pink=(255, 85, 187)

    #--------------------------------for sounds used through the game----------------------
    game_over_sound=pygame.mixer.Sound("game_over.wav")
    #you_win_sound
    fire_sound=pygame.mixer.Sound("fire.mp3")
    explosion_sound=pygame.mixer.Sound("explozie.wav")

    #--------------------------------for picking current time for the frames per second----------------------
    clock = pygame.time.Clock()
    #--------------------------------geometry of tank and its turret------------------------------------------
    tankWidth = 40
    tankHeight = 20
    turretWidth = 5
    wheelWidth = 15
    ground_height = 20
    #--------------------------------------------fonts with size, for text_object function----------------
    smallfont = pygame.font.SysFont("comicsansms", 25)
    medfont = pygame.font.SysFont("comicsansms", 50)
    largefont = pygame.font.SysFont("Yu Mincho Demibold", 85)
    vsmallfont = pygame.font.SysFont("Yu Mincho Demibold", 25)

    #--------------------------------------------defining score function----------------------------------
    #def score(score):
        #text = smallfont.render("Score: " + str(score), True, white)
        #gameDisplay.blit(text, [0, 0])

    #---defining function to get the fonts and sizes assigned with them by size names by default size="small"--
    def text_objects(text, color, size="small"):
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        if size == "medium":
            textSurface = medfont.render(text, True, color)
        if size == "large":
            textSurface = largefont.render(text, True, color)
        if size == "vsmall":
            textSurface = vsmallfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    #---------------------fuction for texts that has to appear over button----------------------------------------
    def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="vsmall"):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
        gameDisplay.blit(textSurf, textRect)

    #--------------------fuction for texts that has to appear over screen----------------------------------------
    def message_to_screen(msg, color, y_displace=0, size="small"):
        textSurf, textRect = text_objects(msg, color, size)
        textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
        gameDisplay.blit(textSurf, textRect)

    #----------------------fuction for players tank , defining turrets positins and wheels dimensions------------
    def tank(x, y, turPos):
        x = int(x)
        y = int(y)
        possibleTurrets = [(x - 27, y - 2),
                           (x - 26, y - 5),
                           (x - 25, y - 8),
                           (x - 23, y - 12),
                           (x - 20, y - 14),
                           (x - 18, y - 15),
                           (x - 15, y - 17),
                           (x - 13, y - 19),
                           (x - 11, y - 21)
                           ]
        pygame.draw.circle(gameDisplay, tank_green, (x, y), int(tankHeight / 2))
        pygame.draw.rect(gameDisplay, tank_green, (x - tankHeight, y, tankWidth, tankHeight))
        pygame.draw.line(gameDisplay,tank_green, (x, y), possibleTurrets[turPos], turretWidth)
        pygame.draw.circle(gameDisplay, tank_green, (x - 15, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x - 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, tank_green, (x - 15, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x - 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x - 5, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x + 5, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x + 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,tank_green, (x + 15, y + 20), wheelWidth)
        return possibleTurrets[turPos]

    #----------------------fuction for computers tank , defining turrets positins and wheels dimensions------------
    def enemy_tank(x, y, turPos):
        x = int(x)
        y = int(y)
        possibleTurrets = [(x + 27, y - 2),
                           (x + 26, y - 5),
                           (x + 25, y - 8),
                           (x + 23, y - 12),
                           (x + 20, y - 14),
                           (x + 18, y - 15),
                           (x + 15, y - 17),
                           (x + 13, y - 19),
                           (x + 11, y - 21)
                           ]
        pygame.draw.circle(gameDisplay,red, (x, y), int(tankHeight / 2))
        pygame.draw.rect(gameDisplay, red, (x - tankHeight, y, tankWidth, tankHeight))
        pygame.draw.line(gameDisplay, red, (x, y), possibleTurrets[turPos], turretWidth)
        pygame.draw.circle(gameDisplay, red, (x - 15, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x - 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x - 15, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x - 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x - 5, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,red, (x + 5, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay,red, (x + 10, y + 20), wheelWidth)
        pygame.draw.circle(gameDisplay, red, (x + 15, y + 20), wheelWidth)
        return possibleTurrets[turPos]

    #-----------------------------------------Game control Screen------------------------------------------------
    def game_controls():
        gcont = True
        while gcont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            message_to_screen("Trage: Spacebar", wheat, -30)
            message_to_screen("Muta tureta: sageti: sus,jos" , wheat, 10)
            message_to_screen("Muta tancul: sageti: stânga,dreapta", wheat, 50)
            message_to_screen("Creste puterea: D    Scade Puterea: A", wheat, 140)
            message_to_screen("Pauză: P", wheat, 90)
            button("Joaca", 150, 500, 100, 50, green, light_green, action="play")
            button("Meniu Principal", 325, 500, 150, 50, yellow, light_yellow, action="main")
            button("Ieși", 550, 500, 100, 50, red, light_red, action="quit")
            pygame.display.update()
            clock.tick(15)

    #--------------function for buttons having action calls and text on it callings---------------------------
    def button(text, x, y, width, height, inactive_color, active_color, action=None,size=" "):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "quit":
                    pygame.quit()
                    quit()
                if action == "controls":
                    game_controls()
                if action == "play":
                    gameLoop()
                if action == "main":
                    game_intro()
        else:
            pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
        text_to_button(text, black, x, y, width, height)

    #---function for pause having transparent background, uncommenting fill statement will make it black-----
    def pause():
        paused = True
        message_to_screen("Pauză", black, -100, size="large")
        message_to_screen("Apasă C pentru a continua sau Q pentru a ieși", black, -50)
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            clock.tick(5)

    #---------------------------function for explosion for both tanks---------------------------------------
    def explosion(x, y, size=50):
        explode = True
        while explode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            startPoint = x, y
            colorChoices = [red, light_red, yellow, light_yellow]
            magnitude = 1
            while magnitude < size:
                exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
                exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)
                pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),random.randrange(1, 5))
                magnitude += 1
                pygame.display.update()
                clock.tick(100)
            explode = False
            pygame.mixer.Sound.play(explosion_sound)

    #--------------------------------firing function for players tank-------------------------------------------
    def fireShell(xy, tankx, tanky, turPos, gun_power,  enemyTankX, enemyTankY):
        fire = True
        damage = 0
        startingShell = list(xy)
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.draw.circle(gameDisplay, fire_blue, (startingShell[0], startingShell[1]), 3)
            startingShell[0] -= (12 - turPos) * 2
            startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
            if startingShell[1] > display_height - 50:
                hit_x = int((startingShell[0] * display_height - 20) / startingShell[1])
                hit_y = int(display_height - ground_height)
                if enemyTankX + 10 > hit_x > enemyTankX - 10:
                    print("Critical Hit!")
                    damage = 50
                elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                    print("Hard Hit!")
                    damage = 35
                elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                    print("Medium Hit")
                    damage = 25
                elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                    print("Light Hit")
                    damage = 10
                explosion(hit_x, hit_y)
                fire = False
            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height
            if check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False
            pygame.display.update()
            clock.tick(60)
        return damage

    #--------------------------------firing function for computer's tank-------------------------------------------
    def e_fireShell(xy, tankx, tanky, turPos, gun_power, ptankx, ptanky):
        damage = 0
        currentPower = 1
        power_found = False
        while not power_found:
            currentPower += 1
            if currentPower > 100:
                power_found = True
            fire = True
            startingShell = list(xy)
            while fire:
                pygame.mixer.Sound.play(fire_sound)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                startingShell[0] += (12 - turPos) * 2
                startingShell[1] += int(
                    (((startingShell[0] - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
                if startingShell[1] > display_height - ground_height:
                    hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
                    hit_y = int(display_height - ground_height)
                    if ptankx + 15 > hit_x > ptankx - 15:
                        power_found = True
                    fire = False
                check_y_1 = startingShell[1] <= display_height
                check_y_2 = startingShell[1] >= display_height
                if  check_y_1 and check_y_2:
                    hit_x = int((startingShell[0]))
                    hit_y = int(startingShell[1])
                    fire = False
        fire = True
        startingShell = list(xy)
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.draw.circle(gameDisplay, fire_orange, (startingShell[0], startingShell[1]), 3)
            startingShell[0] += (12 - turPos) * 2
            gun_power = random.randrange(int(currentPower * 0.90), int(currentPower * 1.10))
            startingShell[1] += int(
                (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))
            if startingShell[1] > display_height - ground_height:
                hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
                hit_y = int(display_height - ground_height)
                if ptankx + 10 > hit_x > ptankx - 10:
                    print("Enemy Critical Hit!")
                    damage = 50
                elif ptankx + 15 > hit_x > ptankx - 15:
                    print("Enemy Hard Hit!")
                    damage = 35
                elif ptankx + 25 > hit_x > ptankx - 25:
                    print("Enemy Medium Hit")
                    damage = 25
                elif ptankx + 35 > hit_x > ptankx - 35:
                    print("Enemy Light Hit")
                    damage = 15
                explosion(hit_x, hit_y)
                fire = False
            
            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height
            if  check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False
            pygame.display.update()
            clock.tick(60)
        return damage
    #--------------------------- function for angle of turret-------------------------------------
    def angle_change(level):
        text1 = smallfont.render("Unghi:", True, wheat)
        gameDisplay.blit(text1, [display_width / 2, 50])
        text2 = smallfont.render(str(level) + "°", True, wheat)
        gameDisplay.blit(text2, [display_width / 2, 75])

    #--------------------------- function for power level of players tank-------------------------------------
    def power(level):
        text1 = smallfont.render("Putere:", True, wheat)
        gameDisplay.blit(text1, [display_width / 2, 0])
        text2 = smallfont.render(str(level) + "%", True, wheat)
        gameDisplay.blit(text2, [display_width / 2, 25])

    #----------------------------------- function for power bar ------------------------------------------
    def power_bars(fire_power):
        if fire_power > 75:
            power_bar = power_colour1
        elif fire_power > 50:
            power_bar = power_colour2
        else:
            power_bar = power_colour3
        pygame.draw.rect(gameDisplay, power_bar, (400  , 30, fire_power, 25))

    #---------------------------function for intro screen------------------------------------------------------
    def game_intro():
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            gameDisplay.fill(black)
            message_to_screen("Bun venit!", white, -100, size="large")
            message_to_screen("TANKS", white, -170, size="large")
            message_to_screen("Trage: Spacebar", wheat, -30)
            message_to_screen("Mută tureta: săgeți: sus,jos" , wheat, 10)
            message_to_screen("Mută tancul: săgeți: stânga,dreapta", wheat, 50)
            message_to_screen("Crește puterea: D    Scade puterea: A", wheat, 140)
            message_to_screen("Pauză: P", wheat, 90)
            message_to_screen("By Buculei Călin-Alexandru", wheat, 280)
            button("Joacă", 250, 500, 100, 50, wheat, light_green, action="play",size="vsmall")
            button("Ieși", 450, 500, 100, 50, wheat, light_red, action="quit",size="vsmall")
            pygame.display.update()
            clock.tick(15)

    #---------------------------function for game Over screen------------------------------------------------------
    def game_over():
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            message_to_screen("Ai pierdut!", white, -50, size="large")
            button("Joacă încă odată", 225, 500, 150, 50, wheat, light_green, action="play")
            button("Ieși", 425, 500, 150, 50, wheat, light_red, action="quit")
            pygame.display.update()
            clock.tick(15)


    #---------------------------function for players win screen--------------------------------------------------
    def you_win():
        win = True
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            message_to_screen("Ai câștigat!", white, -100, size="large")
            message_to_screen("Felicitări!", wheat, -30)
            button("Joacă încă odată", 225, 500, 150, 50, wheat, light_green, action="play")
            button("Ieși", 425, 500, 150, 50, wheat, light_red, action="quit")
            pygame.display.update()
            clock.tick(15)

    #---------------------------function for move bar of player tank---------------------------------------
    #def move_bars(fuel):
        #move_bars_colour=pink
        #pygame.draw.rect(gameDisplay, move_bars_colour, (680, 100, fuel, 25))
    def move_fuel(level):
        text = smallfont.render("Combustibil:" + str(level), True, wheat)
        gameDisplay.blit(text, [600, 50])

    #---------------------------function for health bars of both tanks---------------------------------------
    def health_bars(player_health, enemy_health):
        player_health_color = tank_green
        enemy_health_color = red
        pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
        pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))

    #---------------------------function for main gameloop----------------------------------------------------
    def gameLoop():
        gameExit = False
        gameOver = False
        FPS = 15
        player_health = 100
        enemy_health = 100
        fuel=75
        new_fuel=0
        gameDisplay.blit(background_image, (0, 0))
        mainTankX = display_width * 0.9
        mainTankY = display_height * 0.9
        tankMove = 0
        currentTurPos = 0
        changeTur = 0
        angle = 0
        new_angle=0
        enemyTankX = display_width * 0.1
        enemyTankY = display_height * 0.9
        fire_power = 50
        power_change = 0
        while not gameExit:
            if gameOver == True:
                message_to_screen("Ai pierdut!", red, -50, size="large")
                pygame.display.update()
                while gameOver == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameOver = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_c:
                                gameLoop()
                            elif event.key == pygame.K_q:
                                gameExit = True
                                gameOver = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause()
                    elif event.key == pygame.K_SPACE:
                        pygame.mixer.Sound.play(fire_sound)
                        fuel=50
                        damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, enemyTankX, enemyTankY)
                        enemy_health -= damage
                        possibleMovement = ['f', 'r']
                        moveIndex = random.randrange(0, 2)
                        for x in range(random.randrange(0, 10)):
                            if display_width * 0.3 > enemyTankX > display_width * 0.03:
                                if possibleMovement[moveIndex] == "f":
                                    enemyTankX += 5
                                    if enemyTankX<=105:
                                        enemyTankY -=1
                                    if enemyTankX>140:
                                        enemyTankY +=1
                                elif possibleMovement[moveIndex] == "r":
                                    enemyTankX -= 1
                                    if enemyTankX <=105:
                                        enemyTankY +=0.2
                                    if enemyTankX>140:
                                        enemyTankY -=0.2
                            
                                if enemy_health < 1:
                                    you_win()
                               #gameDisplay.fill(black)
                                gameDisplay.blit(background_image, (0, 0))
                                health_bars(player_health, enemy_health)
                                gun = tank(mainTankX, mainTankY, currentTurPos)
                                enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                                fire_power += power_change
                                angle += new_angle
                                fuel+= new_fuel
                                power_bars(fire_power)
                                power(fire_power)
                                angle_change(angle)
                                move_fuel(fuel)
                                pygame.display.update()
                                clock.tick(FPS)
                        damage = e_fireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, mainTankX, mainTankY)
                        player_health -= damage
                    elif event.key == pygame.K_LEFT and fuel>0 :
                        tankMove = -5
                        new_fuel = -5
                        if mainTankY>0:
                            if mainTankX>710:
                                mainTankY -=1
                            if mainTankX<=710 and mainTankX>620:
                                mainTankY+= 1    
                            if mainTankX<=570:
                                mainTankY-=1
                            if mainTankX<=450 and mainTankX>405:
                                mainTankY+=5
                    elif event.key == pygame.K_RIGHT and fuel>0:
                        tankMove = 5  
                        new_fuel = -5  
                        if mainTankX>710:
                            mainTankY+=1
                        if mainTankX<=710 and mainTankX>620:
                            mainTankY-=1
                        if mainTankX<=570:
                            mainTankY+=1
                        if mainTankX<=450 and mainTankX>405:
                            mainTankY-=5
                    elif event.key == pygame.K_a:
                        power_change = -1
                    elif event.key == pygame.K_d:
                        power_change = 1  
                    elif event.key == pygame.K_UP:
                        changeTur = 1
                        new_angle = new_angle+10
                    elif event.key == pygame.K_DOWN:
                        changeTur = -1
                        new_angle =new_angle -10
                    #print(mainTankX)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                        tankMove = 0
                        new_fuel=0
                        #nu se opreste la 0 daca tin apasat pe sageti
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        changeTur = 0
                        new_angle=0
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        power_change = 0
            mainTankX += tankMove
            currentTurPos += changeTur
            if currentTurPos > 8:
                currentTurPos = 8
            elif currentTurPos < 0:
                currentTurPos = 0
            #gameDisplay.fill(black)
            gameDisplay.blit(background_image, (0, 0))
            health_bars(player_health, enemy_health)
            power_bars(fire_power)
            gun = tank(mainTankX, mainTankY, currentTurPos)
            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 7)
            fire_power += power_change
            if fire_power > 100:
                fire_power = 100
            elif fire_power < 1:
                fire_power = 1
            power(fire_power)
            #move_bars(fuel)
            angle+=new_angle
            if angle>80:
                angle=80
            elif angle<0:
                angle=0
            angle_change(angle)
            fuel+=new_fuel
            if fuel<0:
                fuel=0
            move_fuel(fuel)
            pygame.display.update()
            if player_health < 1 and enemy_health >= 1:
                game_over()
                #pygame.mixer.Sound.play(game_over_sound)
            elif enemy_health < 1 and player_health >= 1:
                you_win()
            clock.tick(FPS)
        pygame.quit()
        quit()
    game_intro()
    gameLoop()
    pass


def play_tetris_game(screen):
    import pygame
    import random
    import copy

    pygame.init()

    pygame.display.set_caption("Tetris") 

    window_width = 550
    window_height = 620
    screen = pygame.display.set_mode((window_width, window_height))

    background_image = pygame.image.load('background.jpg').convert()
    background_image = pygame.transform.scale(background_image, (window_width, window_height))

    color_list = ["black","red", "purple", "green", "yellow", "orange", "cyan", "blue"]

    font = pygame.font.Font(None, 36)
    font_big = pygame.font.Font(None, 52)
    font_color = "white"

    text_surface_next = font.render("Next", True, font_color)
    text_rect_next = text_surface_next.get_rect()
    text_surface_score = font.render("Score",True, font_color)
    text_rect_score = text_surface_score.get_rect()
    text_surface_over = font_big.render("Game Over", True, font_color)
    text_rect_over = text_surface_over.get_rect()
    text_surface_pause = font_big.render("Paused", True, font_color)
    text_rect_pause = text_surface_pause.get_rect()
    text_surface_difficulty = font.render("Difficulty", True, font_color)
    text_rect_difficulty = text_surface_difficulty.get_rect()
    text_surface_reset = font.render("Press Enter to reset", True, font_color)
    text_rect_reset = text_surface_reset.get_rect()

    nr_rows = 20
    nr_columns = 10

    clock = pygame.time.Clock()
    fall_time = 300
    last_fall = pygame.time.get_ticks()

    matrix = [[0 for _ in range(nr_columns)] for _ in range(nr_rows)]

    fix_block_sfx = pygame.mixer.Sound("fix_block.wav")
    game_over_sfx = pygame.mixer.Sound("game_over.wav")
    change_difficulty_sfx = pygame.mixer.Sound("change_difficulty.wav")
    completed_line_sfx = pygame.mixer.Sound("completed_line.wav")
    pause_sfx = pygame.mixer.Sound("pause.wav")

    def display_grid():
        for i in range(nr_rows):
            for j in range(nr_columns):
                pygame.draw.rect(screen,color_list[matrix[i][j]],(j*30+10, i*30+10, 29,29))

    def display_difficulty(time):
        if time == 100:
            diff_text = "hard"
        if time == 300:
            diff_text = "medium"
        if time == 500:
            diff_text = "easy"
        text_surface_choice = font.render(diff_text, True, font_color)
        text_rect_choice = text_surface_difficulty.get_rect()
        screen.blit(text_surface_choice,(370,250),text_rect_choice)

    def display_next_piece(piece):
        pygame.draw.rect(screen,color_list[0],(350,400,150,150))
        for i in range(4):
                for j in range(4):
                    if piece.shape_matrices[piece.position][i][j] == 1:
                        pygame.draw.rect(screen,piece.color,(380 + j*30, 420 + i*30, piece.width, piece.height))
        
    class JBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 1
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0]],
                        
                                    [[1, 0, 0, 0],
                                    [1, 1, 1, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]],

                                    [[0, 1, 1, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]],

                                    [[0, 0, 0, 0],
                                    [1, 1, 1, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 0]]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30
    
        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class LBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 2
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 1, 0],
                                    [0, 0, 0, 0]],
                
                                    [
                                    [0, 0, 0, 0],
                                    [1, 1, 1, 0],
                                    [1, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [1, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 0, 1, 0],
                                    [1, 1, 1, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class OBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 3
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[1, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]],
                
                                    [
                                    [1, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [1, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [1, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class ZBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 4
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[1, 1, 0, 0],
                                    [0, 1, 1, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]],
                
                                    [
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [1, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [1, 1, 0, 0],
                                    [0, 1, 1, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [1, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class SBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 5
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[0, 1, 1, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]],
                
                                    [
                                    [1, 0, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 1, 1, 0],
                                    [1, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [1, 0, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class TBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 6
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[1, 1, 1, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]],
                
                                    [
                                    [0, 1, 0, 0],
                                    [1, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 1, 0, 0],
                                    [1, 1, 1, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 1, 0, 0],
                                    [0, 1, 1, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))
    class IBlock:
        def __init__(self):
            self.width = 29
            self.height = 29
            self.position = 0
            self.x = 130
            self.y = 10
            self.color_id = 7
            self.color = color_list[self.color_id]
            self.shape_matrices = [[[0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0]],
                
                                    [
                                    [0, 0, 0, 0],
                                    [1, 1, 1, 1],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ],

                                    [
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 1, 0, 0]
                                    ],

                                    [
                                    [0, 0, 0, 0],
                                    [1, 1, 1, 1],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]
                                    ]
                                ]
        def rotate(self):
             self.position += 1
             if self.position > 3:
                self.position = 0

        def move_down(self):
            self.y += 30

        def move_left(self):
            self.x -=30

        def move_right(self):
            self.x +=30

        def draw(self,screen):
            for i in range(4):
                for j in range(4):
                    if self.shape_matrices[self.position][i][j] == 1:
                        pygame.draw.rect(screen,self.color,(self.x + j*30,self.y + i*30, self.width, self.height))

    block_list = [LBlock(),JBlock(),ZBlock(),SBlock(),OBlock(),TBlock(),IBlock()]
    test_block = random.choice(block_list)
    next_test_block = test_block
    while next_test_block.color_id == test_block.color_id:
            next_test_block = random.choice(block_list)

    def can_move_down():
        for i in range(4):
            for j in range(4):
                if (test_block.shape_matrices[test_block.position][i][j] and 
                (test_block.y//30 + i > 18 or matrix[test_block.y//30+i+1][test_block.x//30+j])):
                    return False
        return True

    def fix_block():
        for i in range(4):
                    for j in range(4):
                        if test_block.shape_matrices[test_block.position][i][j]:
                            matrix[test_block.y//30 + i][test_block.x//30 + j] = test_block.color_id

    def can_move_left():
        for i in range(4):
            for j in range(4):
                if(test_block.shape_matrices[test_block.position][i][j] and
                    (test_block.x//30 + j < 1 or matrix[test_block.y//30 + i][test_block.x//30 + j - 1])):
                        return False
        return True

    def can_move_right():
        for i in range(4):
            for j in range(4):
                if(test_block.shape_matrices[test_block.position][i][j] and
                    (test_block.x//30 + j > 8 or matrix[test_block.y//30 + i][test_block.x//30 + j + 1])):
                        return False
        return True

    def can_rotate():
        aux_piece = copy.deepcopy(test_block)
        aux_piece.rotate()
        for i in range(4):
            for j in range(4):
                if((aux_piece.x//30 + j < 0 or aux_piece.x//30 + j > 9 or aux_piece.y//30 + i > 18) and
                    aux_piece.shape_matrices[aux_piece.position][i][j]):
                        return False
                if aux_piece.y//30 + i <= 18 and aux_piece.x//30 + j >= -1  and aux_piece.x//30 + j <= 9:
                    if matrix[aux_piece.y//30 + i - 1][aux_piece.x//30 + j]:
                        return False
        return True

    def check_completed_lines():
        nr_completed_lines = 0
        for i in range(nr_rows):
            is_completed = 1
            for j in range(nr_columns):
                if matrix[i][j] == 0:
                    is_completed = 0
                    break
            if is_completed:
                nr_completed_lines += 1
                matrix.remove(matrix[i])
                matrix.insert(0,[0 for _ in range(nr_columns)])
        return nr_completed_lines

    def calculate_score(nr_completed_lines):
        add_score = 0
        if nr_completed_lines == 1:
            add_score = 100
        if nr_completed_lines == 2:
            add_score = 300
        if nr_completed_lines == 3:
            add_score = 500
        if nr_completed_lines == 4:
            add_score = 800
        return add_score

    def game_over():
        for j in range(nr_columns):
            if matrix[0][j] != 0:
                return True
        return False

    def clear_column(piece):
        for i in range(4):
            if piece.shape_matrices[piece.position][i][0]:
                return 0
        return 1

    def give_hint(piece):
        is_solution = 0
        for y in range(nr_rows-1,-1,-1):
            for x in range(nr_columns):
                if matrix[y][x] == 0:
                    is_solution = 1
                    for i in range(4):
                        for j in range(4):
                            if piece.shape_matrices[piece.position][i][j]:
                                if y+i<20 and (x+j - clear_column(piece) > -1 and x+j - clear_column(piece)< 10): 
                                    if matrix[y+i][x+j - clear_column(piece)]:
                                        is_solution = 0
                                        break
                                else:
                                    is_solution = 0
                if is_solution:
                    draw_hint(piece,x,y)
                    return

    def draw_hint(piece,x,y):
        for i in range(4):
            for j in range(4):
                if piece.shape_matrices[piece.position][i][j]:
                    pygame.draw.rect(screen,(130, 130, 130),(x*30 + (j- clear_column(piece))*30 + 10, y*30 + i*30 + 10 , piece.width, piece.height))

    def draw_gameui(fall_time, score):
        screen.blit(text_surface_next,(400,370), text_rect_next)
        screen.blit(text_surface_score,(390,100), text_rect_score)
        screen.blit(text_surface_difficulty,(370,220),text_rect_difficulty)
        display_difficulty(fall_time)
        text_surface_number = font.render(str(score),True, font_color)
        text_rect_number = text_surface_number.get_rect()
        screen.blit(text_surface_number,(410,130),text_rect_number)

    running = True
    paused = False
    game_end = False
    want_hint = False
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_h]:
                    want_hint = not want_hint
                if keys[pygame.K_a] and paused:
                    if fall_time <= 300:
                        fall_time += 200
                    change_difficulty_sfx.play()
                if keys[pygame.K_d] and paused:
                    if fall_time >= 300:
                        fall_time -= 200
                    change_difficulty_sfx.play()
                if not paused:
                    if keys[pygame.K_RETURN] and can_rotate():
                        test_block.rotate()
                    if keys[pygame.K_LEFT] and can_move_left():
                        test_block.move_left()
                    if keys[pygame.K_RIGHT] and can_move_right():
                        test_block.move_right()
                    if keys[pygame.K_DOWN] and can_move_down():
                        test_block.move_down()
                if event.key == pygame.K_SPACE:
                    if not paused:
                        pause_sfx.play()
                    paused = not paused
        if not game_end:
            if not paused:
                now = pygame.time.get_ticks()
                if now - last_fall >= fall_time:
                    last_fall = now
                    if can_move_down():
                        test_block.move_down()
                    else:
                        fix_block()
                        fix_block_sfx.play()
                        test_block = next_test_block
    
                block_list = [LBlock(),JBlock(),ZBlock(),SBlock(),OBlock(),TBlock(),IBlock()]
                nr_completed_lines = check_completed_lines()
                if nr_completed_lines > 0:
                    completed_line_sfx.play()
                score += calculate_score(nr_completed_lines)

                screen.blit(background_image, (0, 0))
                display_grid()
                if want_hint:
                    give_hint(test_block)
                display_next_piece(next_test_block)
                draw_gameui(fall_time, score)

                while next_test_block.color_id == test_block.color_id:
                    next_test_block = random.choice(block_list)

                test_block.draw(screen)
                if game_over():
                    game_over_sfx.play()
                    game_end = True

            if paused:
                screen.blit(background_image, (0, 0))
                display_grid()
                if want_hint:
                    give_hint(test_block)
                display_next_piece(next_test_block)
                draw_gameui(fall_time,score)
                test_block.draw(screen)
                screen.blit(text_surface_pause,(nr_columns*30 //2 - 50, nr_rows*30//2), text_rect_pause)
    
        if game_end:
            screen.blit(text_surface_over,(nr_columns*30 //2 - 70, nr_rows*30//2), text_rect_over)
            screen.blit(text_surface_reset,(nr_columns*30 //2 - 90, nr_rows*30//2 + 40),text_rect_reset)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    running = True
                    paused = False
                    game_end = False
                    want_hint = False
                    score = 0
                    matrix = [[0 for _ in range(nr_columns)] for _ in range(nr_rows)]
                    fall_time = 300
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    pass

score=0
delay_enemy=15

def play_pacman_game(screen):
    import pygame
    import pygame.mixer
    import random
    import heapq
    import numpy as np
    from queue import PriorityQueue


    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)

    window_width = 800
    window_height = 600

    maze_width = 27
    maze_height = 30

    cell_dimension = min(window_width // maze_width, window_height // maze_height)

    window_width = maze_width * cell_dimension
    window_height = maze_height * cell_dimension

    BLACK = (5, 10, 15)
    BLUE = (0, 0, 100)
    YELLOW = (200, 200, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pacman")

    pacman_x = cell_dimension
    pacman_y = cell_dimension
    pacman_speed = 5

    ghost_x = [13 * cell_dimension, 14 * cell_dimension, 15 * cell_dimension, 12 * cell_dimension]   #coordonate fantome
    ghost_y = [13 * cell_dimension, 14 * cell_dimension, 12 * cell_dimension, 11 * cell_dimension]
    ghost_speed = 9

    fruit_x = []
    fruit_y = []
    num_fruits = 4

    score = 0

    start_time = pygame.time.get_ticks()

    maze = [
        "111111111111111111111111111",
        "100000000000010000000000001",
        "101111011111010111110111101",
        "101111011111010111110111101",
        "101111011111010111110111101",
        "100000000000000000000000001",
        "101111010001111100010111101",
        "100000010000010000010000001",
        "111110011111010111110011111",
        "110000010000000000010000011",
        "110000010000000000010000011",
        "110000010111000111010000011",
        "111110000100000001000011111",
        "000000000100000001000000000",
        "111110000100000001000011111",
        "110000010111111111010000011",
        "110000010000000000010000011",
        "110000010000010000010000011",
        "111110000000010000000011111",
        "100000000110000011000000001",
        "100111100100000001001111001",
        "100000000100111001000000001",
        "101100000100010001000001101",
        "100100000000010000000001001",
        "110100100000000000001001011",
        "100000100001111100001000001",
        "100000100000010000001000001",
        "101111111110010011111111101",
        "100000000000000000000000001",
        "111111111111111111111111111",
    
    ]

    delay_enemy = 15

    pacman_image = pygame.image.load("pacman.png").convert_alpha()
    fruit_image = pygame.image.load("fruit.png").convert_alpha()
    enemy_image = pygame.image.load("enemy.png").convert_alpha()
    blue_wall_image = pygame.image.load("blue_wall.png").convert_alpha()

    class Cookie(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((cell_dimension // 4, cell_dimension // 4))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.rect.center = (x + cell_dimension // 2, y + cell_dimension // 2)

    cookies_group = pygame.sprite.Group()
    def generate_cookie():
        for i in range(maze_height):
            for j in range(maze_width):
                if maze[i][j] == '0':
                    cookies_group.add(Cookie(j * cell_dimension, i * cell_dimension))

    generate_cookie()

    def draw_maze():
        for i in range(maze_height):
            for j in range(maze_width):
                if maze[i][j] == '1':
                    wall_rect = pygame.Rect(j * cell_dimension, i * cell_dimension, cell_dimension, cell_dimension)
                    screen.blit(blue_wall_image, wall_rect)
                elif maze[i][j] == '0':
                    pygame.draw.rect(screen, BLACK, (j * cell_dimension, i * cell_dimension, cell_dimension, cell_dimension))

        cookies_group.draw(screen)

    def draw_pacman():
        pacman_size = (cell_dimension, cell_dimension)
        pacman_image_resized = pygame.transform.scale(pacman_image, pacman_size)
        screen.blit(pacman_image_resized, (pacman_x, pacman_y))

    def draw_ghosts():
        enemy_size = (cell_dimension, cell_dimension)
        for i in range(4):
            enemy_image_resized = pygame.transform.scale(enemy_image, enemy_size)
            screen.blit(enemy_image_resized, (ghost_x[i], ghost_y[i]))

    def draw_fruits():
        fruit_size = (cell_dimension, cell_dimension)
        for i in range(num_fruits):
            fruit_image_resized = pygame.transform.scale(fruit_image, fruit_size)
            screen.blit(fruit_image_resized, (fruit_x[i], fruit_y[i]))

    def update_score():
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, YELLOW)
        screen.blit(text, (10, 10))

    def update_time():
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        font = pygame.font.Font(None, 36)
        text = font.render(f"Time: {elapsed_time} seconds", True, YELLOW)
        screen.blit(text, (window_width - 200, 10))

    def check_collision():
        global score
        pacman_rect = pygame.Rect(pacman_x, pacman_y, cell_dimension, cell_dimension)

        for i in range(maze_height):
            for j in range(maze_width):
                if maze[i][j] == '1':
                    wall_rect = pygame.Rect(j * cell_dimension, i * cell_dimension, cell_dimension, cell_dimension)
                    if pacman_rect.colliderect(wall_rect):
                        return True

        for cookie in cookies_group.sprites():
            if pacman_rect.colliderect(cookie.rect):
                score += 1
                cookies_group.remove(cookie)
                break

        for i in range(num_fruits):
            fruit_rect = pygame.Rect(fruit_x[i], fruit_y[i], cell_dimension, cell_dimension)
            if pacman_rect.colliderect(fruit_rect):
                score += 10
                fruit_x[i], fruit_y[i] = generate_fruit_position()

        for i in range(4):
            enemy_rect = pygame.Rect(ghost_x[i], ghost_y[i], cell_dimension, cell_dimension)
            if pacman_rect.colliderect(enemy_rect):
                pygame.quit()
                print("Game Over")
                exit()

        return False

    def generate_fruit_position():
        while True:
            x = random.randint(0, maze_width - 1)
            y = random.randint(0, maze_height - 1)
        
            if maze[y][x] != '1' and (x, y) not in zip(fruit_x, fruit_y):
                return x * cell_dimension, y * cell_dimension

    def dijkstra_algorithm(maze, start_x, start_y, target_x, target_y):
        rows = len(maze)
        cols = len(maze[0])
    
        distances = np.full((rows, cols), np.inf)
        distances[start_y][start_x] = 0
   
        pq = PriorityQueue()
        pq.put((0, (start_x, start_y)))
    
        prev = np.zeros((rows, cols), dtype=object)
    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
        while not pq.empty():
            current_distance, (curr_x, curr_y) = pq.get()
        
            if curr_x == target_x and curr_y == target_y:
                path = []
                while curr_x != start_x or curr_y != start_y:
                    path.append((curr_x, curr_y))
                    curr_x, curr_y = prev[curr_y][curr_x]
                path.reverse()
                if len(path) > 1:
                    dx = path[1][0] - start_x
                    dy = path[1][1] - start_y
                    return dx, dy
            
            if current_distance > distances[curr_y][curr_x]:
                continue
        
            for dx, dy in directions:
                next_x = curr_x + dx
                next_y = curr_y + dy
            
                if next_x < 0 or next_x >= cols or next_y < 0 or next_y >= rows:
                    continue
            
                if maze[next_y][next_x] == '1':
                    continue
            
                new_distance = current_distance + 1
            
                if new_distance < distances[next_y][next_x]:
                    distances[next_y][next_x] = new_distance
                    prev[next_y][next_x] = (curr_x, curr_y)
                    pq.put((new_distance, (next_x, next_y)))
    
        return 0, 0

    def check_collision_ghosts(x, y):
        enemy_rect = pygame.Rect(x, y, cell_dimension, cell_dimension)

        for i in range(maze_height):
            for j in range(maze_width):
                if maze[i][j] == '1':
                    wall_rect = pygame.Rect(j * cell_dimension, i * cell_dimension, cell_dimension, cell_dimension)
                    if enemy_rect.colliderect(wall_rect):
                        return True
        return False

    def update_ghosts():
    
        global delay_enemy
        if delay_enemy > 0:
            delay_enemy-=1
            return
        delay_enemy = 15
        for i in range(4):
            curr_x = round(ghost_x[i] / cell_dimension)
            curr_y = round(ghost_y[i] / cell_dimension)
        
            target_x = round(pacman_x / cell_dimension)
            target_y = round(pacman_y / cell_dimension)
        
            dx, dy = dijkstra_algorithm(maze, curr_x, curr_y, target_x, target_y)
        
            new_x = ghost_x[i] + dx * cell_dimension
            new_y = ghost_y[i] + dy * cell_dimension
        
            if not check_collision_ghosts(new_x, new_y):
                ghost_x[i] = new_x
                ghost_y[i] = new_y
        draw_ghosts()

    for _ in range(num_fruits):
        x, y = generate_fruit_position()
        fruit_x.append(x)
        fruit_y.append(y)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT]:
            pacman_x += pacman_speed
        if keys[pygame.K_UP]:
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN]:
            pacman_y += pacman_speed
    
        if check_collision():
            if keys[pygame.K_LEFT]:
                pacman_x += pacman_speed
            if keys[pygame.K_RIGHT]:
                pacman_x -= pacman_speed
            if keys[pygame.K_UP]:
                pacman_y += pacman_speed
            if keys[pygame.K_DOWN]:
                pacman_y -= pacman_speed
    
        update_ghosts()
    
        screen.fill(BLACK)
        draw_maze()
        draw_maze()
        draw_pacman()
        draw_ghosts()
        draw_fruits()
        pygame.display.update()
        update_score()
        update_time()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()    
    pass

def run_game(game_func):
    pygame.init()
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    
    game_func(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.quit()

def game_selection_menu():
    def play_selected_game(game_func):
        root.destroy()
        run_game(game_func)

    root = tk.Tk()
    root.title("Game Selection")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{int(screen_width * 0.8)}x{int(screen_height * 0.8)}")

    background_image = Image.open("fundal_meniu.jpg")
    bg_photo = ImageTk.PhotoImage(background_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_game_button(text, command):
        button = tk.Button(root, text=text, command=command, font=("Arial", 30), bg="blue", fg="white")
        button.pack(side=tk.TOP, pady=20, padx=50)
        return button

    tetris_button = create_game_button("Play Tetris", lambda: play_selected_game(play_tetris_game))
    pacman_button = create_game_button("Play Pacman", lambda: play_selected_game(play_pacman_game))
    rapid_fire_button = create_game_button("Play Rapid Fire", lambda: play_selected_game(play_rapid_fire_game))
    tanks_button = create_game_button("Play Tanks", lambda: play_selected_game(play_tanks_game))

    root.mainloop()

if __name__ == "__main__":
    game_selection_menu()



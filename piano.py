##
##
## importing the needed modules
import pygame
import time
import threading

pygame.init()

## needed colors 
white = (255,255,255)
d_white = (245,245,245)
black = (0,0,0)
gray = (110,110,110)
l_gray = (150,150,150)
d_gray = (40,40,40)
red = (255,0,0)
blue = (20,89,178)
green = (34,177,76)

## needed fonts
smallfont = pygame.font.SysFont('comicsansms',25)
xsmallfont = pygame.font.SysFont('comicsansms',35)
medfont = pygame.font.SysFont('comicsansms',50)
largefont = pygame.font.SysFont('comicsansms',70)

## screen size
screen = pygame.display.set_mode((1080,640))
pygame.display.set_caption('PIANO')


## playing piano sounds
def value(path, n):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(n)

## changing color of pressed button
def press(color1, dim1, color2, dim2):
    pygame.draw.rect(PianoScreen,color1,dim1) 
    pygame.draw.rect(PianoScreen,color2,dim2) 
    pygame.display.update()
    
## getting the original color back when the button get unpressed
def unpress(dim):
    pygame.draw.rect(PianoScreen,d_white,dim)  
    pygame.display.update()
                                        
## keeping texts at the center of the screen                                   
def text_center (text,color, size) :

    if size == 'small':                      
        textSurface = smallfont.render(text, True, color)

    elif size == 'xsmall':                      
        textSurface = xsmallfont.render(text, True, color)

    elif size == 'medium':                      
        textSurface = medfont.render(text, True, color)

    elif size == 'large':                      
        textSurface = largefont.render(text, True, color)                        

    return textSurface, textSurface.get_rect()

## adding texts or messages
def screen_txt (msg,color,y_displace=0,size='small') :
    textSurf, textRect = text_center(msg,color,size)
    textRect.center = (1080/2), (640/2)+y_displace
    screen.blit(textSurf, textRect)

## adding cover music and some instructions about the game  
def game_begin():
    begn = True
    
    # thread for playing a cover music at the beginning
    thread_cover = threading.Thread(target = value, args = ("sounds/cover.mp3", 10))
    thread_cover.run()
    
    while begn :
        screen.fill(black)

        screen_txt('pygame piano :)', green,
                  -140,
                  size ='large')

        screen_txt('Use The Keys   A, S, D, F, G, H, J, K, L, Q, W, E ',
                  red,
                  0,
                  size ='xsmall')

        screen_txt('Press ENTER to Start',
                  red,
                  95,
                  size ='xsmall')        

        screen_txt('Eslam Ghazal', 
                  white,
                  240,
                  size ='small')

        pygame.display.update()
               
        for event in pygame.event.get() : 
            # if the user pressed enter, stop the cover music and exit the beginning loop
            if event.type == pygame.KEYDOWN :
                if event.key == 13:
                    global PianoScreen
                    PianoScreen = pygame.display.set_mode((686,181))
                    pygame.mixer.music.stop()
                    begn = False

            if event.type == pygame.QUIT :
                pygame.quit()
                quit()


## creating the piano shape
def shape():  
    PianoScreen.fill(l_gray)    
    pygame.draw.rect(PianoScreen,d_white,(2,3,55,174))
    pygame.draw.rect(PianoScreen,d_white,(59,3,55,174))  
    pygame.draw.rect(PianoScreen,d_white,(116,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(173,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(230,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(287,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(344,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(401,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(458,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(515,3,55,174))   
    pygame.draw.rect(PianoScreen,d_white,(572,3,55,174))    
    pygame.draw.rect(PianoScreen,d_white,(629,3,55,174))
    pygame.display.update()


game_begin()   
shape()

game_exit = False
while not game_exit :
      
    for event in pygame.event.get() :        

        if event.type == pygame.QUIT :
            game_exit = True

        # for every key press creating two threads, the first for playing the piano sound, 
        # the second for changing color of pressed area
        if event.type == pygame.KEYDOWN :
            
            if event.key == pygame.K_q :
                thread_Q = threading.Thread(target = value, args = ("sounds/sound9.wav", 0))
                thread_Q.run()
                press_Q = threading.Thread(target = press, args = ( gray,(2,3,55,174),d_gray,(4,5,53,172)) )
                press_Q.run()

            if event.key == pygame.K_w :
                thread_W = threading.Thread(target = value, args = ("sounds/sound10.wav", 0))
                thread_W.run()
                press_W = threading.Thread(target = press, args = ( gray,(59,3,55,174),d_gray,(61,5,53,172)) )
                press_W.run()

            if event.key == pygame.K_e :  
                thread_E = threading.Thread(target = value, args = ("sounds/sound12.wav", 0))
                thread_E.run()
                press_E = threading.Thread(target = press, args = ( gray,(116,3,55,174),d_gray,(118,5,53,172)) )
                press_E.run()
                                
            if event.key == pygame.K_a :
                thread_A = threading.Thread(target = value, args = ("sounds/sound1.wav", 0))
                thread_A.run()
                press_A = threading.Thread(target = press, args = ( gray,(173,3,55,174),d_gray,(175,5,53,172)) )
                press_A.run()

            if event.key == pygame.K_s :
                thread_S = threading.Thread(target = value, args = ("sounds/sound2.wav", 0))
                thread_S.run()
                press_S = threading.Thread(target = press, args = ( gray,(230,3,55,174),d_gray,(232,5,53,172)) )
                press_S.run()

            if event.key == pygame.K_d :
                thread_D = threading.Thread(target = value, args = ("sounds/sound3.wav", 0))
                thread_D.run()
                press_D = threading.Thread(target = press, args = ( gray,(287,3,55,174),d_gray,(289,5,53,172)) )
                press_D.run()

            if event.key == pygame.K_f :
                thread_F = threading.Thread(target = value, args = ("sounds/sound4.wav", 0))
                thread_F.run()
                press_F = threading.Thread(target = press, args = ( gray,(344,3,55,174),d_gray,(346,5,53,172)) )
                press_F.run()

            if event.key == pygame.K_g :
                thread_G = threading.Thread(target = value, args = ("sounds/sound5.wav", 0))
                thread_G.run()
                press_G = threading.Thread(target = press, args = ( gray,(401,3,55,174),d_gray,(403,5,53,172)) )
                press_G.run()

            if event.key == pygame.K_h :
                thread_H = threading.Thread(target = value, args = ("sounds/sound6.wav", 0))
                thread_H.run()
                press_H = threading.Thread(target = press, args = ( gray,(458,3,55,174),d_gray,(460,5,53,172)) )
                press_H.run()

            if event.key == pygame.K_j :
                thread_J = threading.Thread(target = value, args = ("sounds/sound7.wav", 0))
                thread_J.run()
                press_J = threading.Thread(target = press, args = ( gray,(515,3,55,174),d_gray,(517,5,53,172)) )
                press_J.run()

            if event.key == pygame.K_k :
                thread_K = threading.Thread(target = value, args = ("sounds/sound8.wav", 0))
                thread_K.run()
                press_K = threading.Thread(target = press, args = ( gray,(572,3,55,174),d_gray,(574,5,53,172)) )
                press_K.run()

            if event.key == pygame.K_l :
                thread_L = threading.Thread(target = value, args = ("sounds/sound11.wav", 0)) 
                thread_L.run()
                press_L = threading.Thread(target = press, args = ( gray,(629,3,55,174),d_gray,(631,5,53,172)) )
                press_L.run()    


        # when the button get unpressed, creating a thread for getting the originalcolor back
        if event.type == pygame.KEYUP :
            
            if event.key == pygame.K_q :
                press_Q = threading.Thread(target = unpress, args = ( (2,3,55,174), ))
                press_Q.run()

            if event.key == pygame.K_w :
                press_W = threading.Thread(target = unpress, args = ( (59,3,55,174), ))
                press_W.run()

            if event.key == pygame.K_e :  
                press_E = threading.Thread(target = unpress, args = ( (116,3,55,174), ))
                press_E.run()
                                
            if event.key == pygame.K_a :
                press_A = threading.Thread(target = unpress, args = ( (173,3,55,174), ))
                press_A.run()

            if event.key == pygame.K_s :
                press_S = threading.Thread(target = unpress, args = ( (230,3,55,174), ))
                press_S.run()

            if event.key == pygame.K_d :
                press_D = threading.Thread(target = unpress, args = ( (287,3,55,174), ))
                press_D.run()

            if event.key == pygame.K_f :
                press_F = threading.Thread(target = unpress, args = ( (344,3,55,174), ))
                press_F.run()

            if event.key == pygame.K_g :
                press_G = threading.Thread(target = unpress, args = ( (401,3,55,174), ))
                press_G.run()

            if event.key == pygame.K_h :
                press_H = threading.Thread(target = unpress, args = ( (458,3,55,174), )) 
                press_H.run()

            if event.key == pygame.K_j :
                press_J = threading.Thread(target = unpress, args = ( (515,3,55,174), ))
                press_J.run()

            if event.key == pygame.K_k :
                press_K = threading.Thread(target = unpress, args = ( (572,3,55,174), ))
                press_K.run()

            if event.key == pygame.K_l :
                press_L = threading.Thread(target = unpress, args = ( (629,3,55,174), ))
                press_L.run()  

pygame.quit()
quit()

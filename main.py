
class main():
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load("images/BG.jpeg").convert_alpha(),(700,600))
        
        self.man_straight = pygame.transform.smoothscale(pygame.image.load("images/man_2.png").convert_alpha(),(90,75))
        
        self.man_tilt_down = pygame.transform.smoothscale(pygame.image.load("images/man_down.png").convert_alpha(),(120,115))
        
        self.pipe = pygame.transform.scale(pygame.image.load("images/pipe.png").convert_alpha(),(290,514))
        self.pipe_rotated = pygame.transform.scale(pygame.image.load("images/pipe_rotated.png").convert_alpha(),(290,514))
        
        self.title = pygame.transform.smoothscale(pygame.image.load("images/title.png").convert_alpha(),(550,400))
        self.space = pygame.transform.smoothscale(pygame.image.load("images/space_text.png").convert_alpha(),(450,150))
        
        self.score_list = []
        self.score_list.append(pygame.image.load("images/0.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/1.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/2.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/3.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/4.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/5.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/6.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/7.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/8.png").convert_alpha())
        self.score_list.append(pygame.image.load("images/9.png").convert_alpha())
        
        self.retry_1 = pygame.transform.smoothscale(pygame.image.load("images/retry_1.png").convert_alpha(),(240,200))
        self.retry_2 = pygame.transform.smoothscale(pygame.image.load("images/retry_2.png").convert_alpha(),(240,200))
        self.exit_1 = pygame.transform.smoothscale(pygame.image.load("images/exit_1.png").convert_alpha(),(240,200))
        self.exit_2 = pygame.transform.smoothscale(pygame.image.load("images/exit_2.png").convert_alpha(),(240,200))
        
        self.score_t = pygame.transform.smoothscale(pygame.image.load("images/score.png").convert_alpha(),(400,300))
        self.wanna = pygame.transform.smoothscale(pygame.image.load("images/wanna.png").convert_alpha(),(530,110))
        
        self.bg_music = pygame.mixer.Sound("sound/BG.mp3")
        self.bg_music.set_volume(0.5)
        self.bg_music.play(-1)
        self.whoosh = pygame.mixer.Sound("sound/whoosh.wav")
        self.point = pygame.mixer.Sound("sound/point.wav") 
        self.transition = pygame.mixer.Sound("sound/transition.wav") 
        self.died = pygame.mixer.Sound("sound/died.wav") 
        self.died.set_volume(1.0)
        
        self.randomize()
        self.random_x_coordinates = 1000
        self.coordinates_pipe = Vector2(self.random_x_coordinates,340+self.random_y_coordinates)
        self.coordinates_pipe_rotated = Vector2(self.random_x_coordinates+4,265+self.random_y_coordinates)
        self.pipe_list = []
        self.pipe_coordinate_list = [self.coordinates_pipe,self.coordinates_pipe_rotated]
        self.pipe_list.append(self.pipe_coordinate_list)
        
        self.man_image = self.man_straight
        self.man_rect = self.man_straight.get_rect(center = (80,210))
        
        
        self.score = 0
        self.point_col =False
        self.man_gravity = 2.5
        
        
    '''PIPE'''
    def pipe_image(self):
        index = 0
        self.pipe_movement()  
        for move in self.pipe_list:
            self.pipe_rect = self.pipe.get_rect(midtop = (move[0]))
            self.pipe_rotated_rect = self.pipe_rotated.get_rect(midbottom = (move[1]))
            index += 1
            screen.blit(self.pipe,self.pipe_rect)
            screen.blit(self.pipe_rotated,self.pipe_rotated_rect)
    
    def pipe_movement(self):
        
        for move in self.pipe_list:
            move[0].x -= 6
            move[1].x -= 6
            
    def new_pipe(self):
        
        self.random_y_coordinates = choice(self.random_nums)
        self.coordinates_pipe = Vector2(self.random_x_coordinates,340+self.random_y_coordinates)
        self.coordinates_pipe_rotated = Vector2(self.random_x_coordinates+4,265+self.random_y_coordinates)
        self.pipe_coordinate_list = [self.coordinates_pipe,self.coordinates_pipe_rotated]
        self.pipe_list.append(self.pipe_coordinate_list)
        
        
    def randomize(self):
        
        self.random_nums = [-125,-100,-90,-75,-50,-10,0,30,40,50,65,90,100,150]
        self.random_y_coordinates = choice(self.random_nums)
    def remove(self):
        
        for pipe in self.pipe_list: 
            if pipe[0].x < -200:
                self.pipe_list.remove(pipe)
            
    '''MAN'''    
    def draw_man(self):
        global keydown
        if keydown == True:
            
            self.man_image = self.man_straight
            screen.blit(self.man_image,self.man_rect)
        else:
            self.man_image = self.man_tilt_down
            screen.blit(self.man_image,self.man_rect)
        
    def gravity(self):
        
        global keydown
        
        # if maingame:
        #     keys = pygame.key.get_pressed()
        #     mouse_buttons  =pygame.mouse.get_pressed()
        #     if keys[pygame.K_SPACE] or mouse_buttons[0] :
        #         keydown = True
        #         self.man_gravity = -8
        #         self.man_rect.y += self.man_gravity
        #     else:
        #         keydown = False
        velocity = self.man_gravity
        self.man_rect.y += velocity
        
        
        
                
    
    def draw_images(self):
        screen.blit(self.bg,(0,0))     
        self.pipe_image()
        self.draw_man()
        self.score_text()
        self.remove()
        # screen.blit(self.plane_tilt_down,(0,0))     
        # screen.blit(self.plane_tilt_up,(200,200))
    def collision(self):
        global maingame
        if self.man_rect.y <= 0 or self.man_rect.y >= 530:
            self.gameover()
        for collide in self.pipe_list:
            pipe_1_rect = self.pipe.get_rect(midtop = (collide[0].x+89,collide[0].y+43))
            pipe_2_rect = self.pipe_rotated.get_rect(midbottom = (collide[1].x+90,collide[1].y-63))
            self.score_detect = self.pipe.get_rect(midtop = (collide[0].x+160,collide[0].y-190))
            pipe_1_rect.width = 100
            pipe_2_rect.width = 100
            
            self.score_detect.width = 5
            self.score_detect.height = 250
            
            # pygame.draw.rect(screen,"red",pipe_1_rect)
            # pygame.draw.rect(screen,"red",self.score_detect)
            # pygame.draw.rect(screen,"red",pipe_2_rect)
            
            if self.man_rect.colliderect(pipe_1_rect) or self.man_rect.colliderect(pipe_2_rect): 
                self.gameover()
             
            if self.score_detect.collidepoint( self.man_rect.x,self.man_rect.y ):
                self.score += 1
                self.point.play()
              
    def startscreen(self):
        self.title_rect = self.title.get_rect( center = (400,230))
        self.space_rect = self.space.get_rect(center = (350,450))
        screen.blit(self.bg,(0,0))          
        screen.blit(self.man_image,self.man_rect)   
        screen.blit(self.title,self.title_rect) 
        screen.blit(self.space,self.space_rect) 
    def starting_page_info(self):
        global maingame
        global pipe_timer
        maingame = True 
        M.transition.play()
        speed = 1350
        pipe_timer = pygame.USEREVENT + 1 
        pygame.time.set_timer(pipe_timer,speed)
    def score_text(self):
        
        myDigits = [int(x) for x in list(str(self.score))]
        width = 0
        for digit in myDigits:
            width += pygame.transform.smoothscale(self.score_list[digit],(60,60)).get_width()- 10
            
        Xoffset = ((screen_width - width)/2) 

        for digit in myDigits:
            screen.blit(pygame.transform.smoothscale(self.score_list[digit],(60,60)), (Xoffset,60))
            Xoffset += pygame.transform.smoothscale(self.score_list[digit],(60,60)).get_width() - 10
            
    def endscreen(self):
        screen.blit(self.bg,(0,0)) 
        myDigits = [int(x) for x in list(str(self.score))]
        width = 0
        for digit in myDigits:
            width += pygame.transform.smoothscale(self.score_list[digit],(75,75)).get_width() - 20
        Xoffset = 480

        for digit in myDigits:
            screen.blit(pygame.transform.smoothscale(self.score_list[digit],(75,75)), (Xoffset,55))
            Xoffset += pygame.transform.smoothscale(self.score_list[digit],(75,75)).get_width() - 20
        
        score_t_rect = self.score_t.get_rect(center = (330,100))
        wanna_rect = self.wanna.get_rect(center = (350,230))
        
        self.retry = self.retry_1
        self.retry_rect_blit = self.retry_1.get_rect(topleft = (140,250))
        self.retry_rect = pygame.Rect(183,308,126,73)
    
        self.exit = self.exit_1
        self.exit_rect_blit = self.exit_1.get_rect(topleft = (322,250))
        self.exit_rect = pygame.Rect(375,307,125,75)
        
        if self.retry_rect.collidepoint(pygame.mouse.get_pos()):
            self.retry = self.retry_2
        if self.exit_rect.collidepoint(pygame.mouse.get_pos()):
            self.exit = self.exit_2
            
        screen.blit(self.score_t,score_t_rect)
        screen.blit(self.wanna,wanna_rect)
        screen.blit(self.retry,self.retry_rect_blit)
        screen.blit(self.exit,self.exit_rect_blit)
        # screen.blit(self.zero,(310,65))
    def restart(self):
        self.transition.play()
        global maingame
        self.score = 0
        maingame = True
        self.man_rect = self.man_straight.get_rect(center = (80,210))
        self.pipe_list.clear() 
    def gameover(self):
        global maingame
        maingame = None    
        self.died.play()
        
          
import pygame,sys,os
from pygame.math import Vector2
from random import choice
pygame.init()

screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
icon = pygame.image.load("images/man_up.png").convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy Man")
clock = pygame.time.Clock()
maingame = False
keydown = False

M = main()

#timers

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if  maingame == False:
            if event.type  == pygame.KEYDOWN :
                
                if event.key == pygame.K_SPACE :
                    M.starting_page_info()
            if event.type  == pygame.MOUSEBUTTONDOWN:
                M.starting_page_info()
             
        if maingame:    
            if event.type == pipe_timer: 
                M.new_pipe()
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    keydown = True
                    M.man_gravity = -12
                    velocity = M.man_gravity
                    M.man_rect.y += velocity
                    M.whoosh.play()
                else:
                    keydown = False
                    M.man_gravity = 5
            if event.type  == pygame.MOUSEBUTTONDOWN:
                M.whoosh.play()
        if maingame == None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if M.retry_rect.collidepoint(pygame.mouse.get_pos()):
                    M.restart()
                elif M.exit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    M.restart()
                
            else:
                keydown = False
                    
                    
    if maingame:
        M.draw_images() 
        M.gravity()   
        M.collision()
    if maingame == False:
        M.startscreen()
    if maingame == None:
        M.endscreen()
    pygame.display.update()
    clock.tick(60)

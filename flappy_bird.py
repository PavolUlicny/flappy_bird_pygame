#imports
import pygame 
import sys
import random
import os

#variables 
global folder, running, start_screen, high_score_set
window_width=550
window_height=650
running=False
folder="flappy_bird"
birdx=110
birdy=150   
bird_width=70
bird_height=54
pipe_width=69   
pipe_height=758
bird_speed=0
gravity=0.5
jump_strength=9.5
pipe1x=650 
pipe1y=random.randint(225,575)
pipe2x=975
pipe2y=random.randint(225,575)
pipe3x=1300
pipe3y=random.randint(225,575)
pipe_space=950
pipe_pause=325
pipe_speed=2.5
start_screen=True
pipe1_counted=False
pipe2_counted=False
pipe3_counted=False
high_score=0
high_score_set=False
high_score_name=[]
high_score_num=[]
low_high_score=0
score=0
name_input=""

#func that checks if a txt file is empty
def is_empty(file):
    if os.stat(file).st_size>0:
        return False
    else:
        return True

#paths
bird_path=os.path.join(folder,"bird.png")
pipe_path=os.path.join(folder,"pipe.png")

#loads high score from file ....................................................................................................................
high_score_file=open(f"{folder}/high_score.txt", "a")
high_score_file.close()
if not is_empty(f"{folder}/high_score.txt"):
    high_score_file=open(f"{folder}/high_score.txt", "r")
    high_score_table=high_score_file.read()
    high_score_list=high_score_table.splitlines()
    high_score_name=[]
    high_score_num=[]
    for i in high_score_list:
        var=i.split("/")
        high_score_name.append(var[0])
        high_score_num.append(var[1])
    high_score=high_score_num[0]
    high_score_file.close()
    high_score_num=[int(s) for s in high_score_num]

#initializing pygame
pygame.init()

#load bird image
bird_img1=pygame.image.load((f"{folder}/bird.png"))
bird_img=pygame.transform.scale(bird_img1,(70,54))

#load pipe image 
pipe_img1=pygame.image.load((f"{folder}/pipe.png"))
down_pipe_img=pygame.transform.scale(pipe_img1,(69,758))

#flip pipe img 
top_pipe_img=pygame.transform.flip(down_pipe_img, False, True)

#fonts and texts
text_color=(0,0,0)
font1=pygame.font.SysFont("Courier",60)
flappy_bird_text=font1.render("Flappy bird",True,text_color)
font2=pygame.font.SysFont("Arial",30)
jump_start_text=font2.render("Press the Jump button to start",True,text_color)
game_over_text=font1.render("Game over",True,text_color)
restart_text=font2.render("Press backspace to retry",True,text_color)
high_score_text=font2.render(f"High score: {high_score}",True,text_color)
score_text=font2.render(f"Score: {score}",True,text_color)
high_scores_text=font2.render(f"Top 5 highest scores:",True,text_color)
you_got_text=font2.render(f"You got one of the top 5 highest scores!",True,text_color)
insert_name_text=font2.render(f"Insert a 3 letter name:",True,text_color)


#create window 
window1=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Flappy bird")
clock=pygame.time.Clock()

#game over function ....................................................................................................................
def game_over():
    global running,score,high_score,high_score_set,low_high_score,high_score_name,high_score_num
    if len(high_score_name)>0:
        low_high_score=high_score_num[-1]
        if score>low_high_score or len(high_score_name)<5 and score>0:
            high_score_set=True
    elif score>0:
        high_score_set=True
    running=False
    
#restart game function ....................................................................................................................
def restart_func():
    
    #reset variables
    global running,birdx,birdy,bird_speed,pipe1x,pipe1y,pipe2x,pipe2y,pipe3x,pipe3y,score,pipe1_counted,pipe2_counted,pipe3_counted
    birdx=110
    birdy=150   
    bird_speed=0
    pipe1x=650 
    pipe1y=random.randint(225,575)
    pipe2x=975
    pipe2y=random.randint(225,575)
    pipe3x=1300
    pipe3y=random.randint(225,575)
    score=0
    pipe1_counted=False
    pipe2_counted=False
    pipe3_counted=False
    
    #run main loop
    running=True

#start screen loop ....................................................................................................................
while start_screen:

    #set fps
    clock.tick(20)
    
    #sets window color
    window1.fill((135,206,235))
    
    #render text
    window1.blit(flappy_bird_text,(70,110))
    window1.blit(jump_start_text,(110,250))
    window1.blit(high_score_text,(190,320))
    
    #checking for events
    for event in pygame.event.get():
        
        #exit the app
        if event.type==pygame.QUIT:
            start_screen=False
            pygame.quit()
            sys.exit()
            
        #binds
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE or event.key==pygame.K_ESCAPE:
                start_screen=False
                running=True
                
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                start_screen=False
                running=True
    
    #update the window
    pygame.display.update()
    
#game loop ....................................................................................................................
while True:
    
    #main game loop
    while running:
        
        #set fps
        clock.tick(60)
        
        #sets window color
        window1.fill((135,206,235))
        
        #check for events
        for event in pygame.event.get():
            
            #check for quit event
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
                
            #check for key presses that trigger a jump
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE or event.key==pygame.K_ESCAPE:
                    bird_speed=-jump_strength
                    
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    bird_speed=-jump_strength
                    
        #moves pipes and bird by adjusting position variables
        bird_speed+=gravity
        birdy+=bird_speed
        pipe1x-=pipe_speed
        pipe2x-=pipe_speed
        pipe3x-=pipe_speed
        
        #hitboxes
        bird_rect=pygame.Rect(birdx+5,birdy+3,bird_width-5,bird_height-3)
        down_pipe1_rect=pygame.Rect(pipe1x,pipe1y,pipe_width,pipe_height)
        top_pipe1_rect=pygame.Rect(pipe1x,pipe1y-pipe_space,pipe_width,pipe_height)
        down_pipe2_rect=pygame.Rect(pipe2x,pipe2y,pipe_width,pipe_height)
        top_pipe2_rect=pygame.Rect(pipe2x,pipe2y-pipe_space,pipe_width,pipe_height)
        down_pipe3_rect=pygame.Rect(pipe3x,pipe3y,pipe_width,pipe_height)
        top_pipe3_rect=pygame.Rect(pipe3x,pipe3y-pipe_space,pipe_width,pipe_height)
        
        #check for collisions or bird getting out of bounds
        if bird_rect.colliderect(down_pipe1_rect) or bird_rect.colliderect(down_pipe2_rect) or bird_rect.colliderect(down_pipe3_rect):
            game_over()
        if bird_rect.colliderect(top_pipe1_rect) or bird_rect.colliderect(top_pipe2_rect) or bird_rect.colliderect(top_pipe3_rect):
            game_over()
        if birdy<-3 or birdy>653-bird_height:
            game_over()

        #checks if pipes are at the end of the screen and if so, moves them to the start
        if pipe1x<-100:
            pipe1x=pipe3x+pipe_pause
            pipe1y=random.randint(225,575)
            pipe1_counted=False
        if pipe2x<-100:
            pipe2x=pipe1x+pipe_pause
            pipe2y=random.randint(225,575)
            pipe2_counted=False
        if pipe3x<-100:
            pipe3x=pipe2x+pipe_pause
            pipe3y=random.randint(225,575)
            pipe3_counted=False
        
        #places all images at their desired spot 
        window1.blit(bird_img,(birdx,birdy))
        window1.blit(down_pipe_img,(pipe1x,pipe1y))
        window1.blit(top_pipe_img,(pipe1x,pipe1y-pipe_space))
        window1.blit(down_pipe_img,(pipe2x,pipe2y))
        window1.blit(top_pipe_img,(pipe2x,pipe2y-pipe_space))
        window1.blit(down_pipe_img,(pipe3x,pipe3y))
        window1.blit(top_pipe_img,(pipe3x,pipe3y-pipe_space))
        
        if pipe1x<birdx and not pipe1_counted:
            score+=1
            pipe1_counted=True
        
        if pipe2x<birdx and not pipe2_counted:
            score+=1
            pipe2_counted=True
        
        if pipe3x<birdx and not pipe3_counted:
            score+=1
            pipe3_counted=True
        
        #score text 
        score_text=font2.render(f"Score: {score}",True,text_color)
        window1.blit(score_text,(220,600))
        
        #displays all updates that happened
        pygame.display.update()
        
    #high score window (set name screen) ....................................................................................................................
    while not running and high_score_set:
        
        #set fps
        clock.tick(20)
        
        #sets window color
        window1.fill((135,206,235))
        
        #text
        name_display=font2.render(name_input + "|",True,text_color)
        window1.blit(name_display,(255-(len(name_input)*6.3),240))
        window1.blit(you_got_text,(60,100))
        score_text=font2.render(f"Score: {score}",True,text_color)
        window1.blit(score_text,(220,150))
        window1.blit(insert_name_text,(145,200))
        
        #checking for events
        for event in pygame.event.get():
            
            #exit the app
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            #binds
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_ESCAPE:
                    high_score_set=False
                    name_input=""
                    num=0
                    
                if event.key==pygame.K_RETURN and len(name_input)>0 and name_input not in high_score_name:
                    
                    #process scores
                    num=0
                    for i in high_score_num:
                        if score>i:
                            num+=1
                            
                    if num>0:
                        high_score_name.insert(-num,name_input)
                        high_score_num.insert(-num,score)
                    else:
                        high_score_name.append(name_input)
                        high_score_num.append(score)

                    #make the high score lists 5 items long
                    high_score_name = high_score_name[:5]
                    high_score_num = high_score_num[:5]
                    
                    #write the scores into a txt file
                    high_score_file=open(f"{folder}/high_score.txt","w")
                    for idx,i in enumerate(high_score_name):
                        high_score_file.write(f"{i}/{high_score_num[idx]}\n")
                    high_score_file.close()
                    
                    #reset some variables
                    high_score_set=False
                    name_input=""
                    num=0
                    
                    #load the high scores 
                    high_score_file=open(f"{folder}/high_score.txt", "a")
                    high_score_file.close()
                    if not is_empty(f"{folder}/high_score.txt"):
                        high_score_file=open(f"{folder}/high_score.txt", "r")
                        high_score_table=high_score_file.read()
                        high_score_list=high_score_table.splitlines()
                        high_score_name=[]
                        high_score_num=[]
                        for i in high_score_list:
                            var=i.split("/")
                            high_score_name.append(var[0])
                            high_score_num.append(var[1])
                        high_score=high_score_num[0]
                        high_score_file.close()
                        high_score_num=[int(s) for s in high_score_num]

                elif event.key==pygame.K_BACKSPACE:
                    name_input=name_input[:-1]
                    
                else:
                    if len(name_input)<3 and event.unicode.isalpha():
                        name_input+=event.unicode
                        name_input=name_input.upper()
                    
        #update the window
        pygame.display.update()
        
    #game over/restart screen ....................................................................................................................
    while not running and not high_score_set:
        
        #set fps
        clock.tick(20)
        
        #sets window color
        window1.fill((135,206,235))
        
        #render text
        window1.blit(game_over_text,(100,5))
        window1.blit(restart_text,(130,70))
        score_text=font2.render(f"Score: {score}",True,text_color)
        window1.blit(score_text,(220,115))
        if len(high_score_name)>0:
            high_scores_text=font2.render(f"Top 5 highest scores:",True,text_color)
        else:
            high_scores_text=font2.render("",True,text_color)
        window1.blit(high_scores_text,(140,160))
        high_score_y=240
        for idx,i in enumerate(high_score_name):
            high_score_text=font2.render(i,True,text_color)
            high_score_text2=font2.render(str(high_score_num[idx]),True,text_color)
            window1.blit(high_score_text,(100,high_score_y))
            window1.blit(high_score_text2,(390-(10*len(str(high_score_num[idx]))),high_score_y))
            high_score_y+=70
        
        #checking for events
        for event in pygame.event.get():
            
            #exit the app
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            #binds
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    restart_func()
        
        #update the window
        pygame.display.update()

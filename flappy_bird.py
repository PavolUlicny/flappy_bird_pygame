#imports
import tkinter as tk 
from PIL import Image, ImageTk
import random
import os

#variables
global birdx,birdy,gravity,bird_speed,jump_strength,pipe_speed,game_started,bottom_pipe1x,bottom_pipe1y,bottom_pipe2x,bottom_pipe2y,bottom_pipe3x,bottom_pipe3y,pipe_pause,game_over,bird_height,bird_width,pipe_heigth,pipe_width,score,global_score,pipe1_counted,pipe2_counted,pipe3_counted
game_started=False
game_over=False
birdx=110
birdy=150
gravity=0.002
bird_speed=0
pipe_speed=0.3
jump_strength=0.57
bottom_pipe1x=650
bottom_pipe1y=random.randint(225,575)
bottom_pipe2x=975
bottom_pipe2y=random.randint(225,575)
bottom_pipe3x=1300
bottom_pipe3y=random.randint(225,575)
pipe_pause=325
pipe_space=935
bird_width=70
bird_height=54
pipe_width=69
pipe_height=758
score=0
high_score=0
pipe1_counted=False
pipe2_counted=False
pipe3_counted=False
folder1="flappy_bird"

#func that checks if a txt file is empty
def is_empty(file):
    if os.stat(file).st_size>0:
        return False
    else:
        return True

#paths
bird_path=os.path.join(folder1,"bird.png")
pipe_path=os.path.join(folder1,"pipe.png")

high_score_file=open(f"{folder1}/high_score.txt", "a")
high_score_file.close()
if not is_empty(f"{folder1}/high_score.txt"):
    high_score_file=open(f"{folder1}/high_score.txt", "r")
    high_score=int(high_score_file.read())
    high_score_file.close()

#pipe and bird movement func
def scene_movement():
    global birdx,birdy,gravity,bird_speed,bottom_pipe1x,bottom_pipe1y,bottom_pipe2x,bottom_pipe2y,bottom_pipe3x,bottom_pipe3y,pipe_pause,game_started,pipe_speed,game_over,pipe1_counted,pipe2_counted,pipe3_counted,score,high_score,score_label
    if game_started and not game_over:
        score_label.config(text=f"Score: {score}")
        bird_label.place(x=birdx,y=birdy)
        bird_speed+=gravity
        birdy+=bird_speed
        bottom_pipe1x-=pipe_speed
        bottom_pipe_label1.place(x=bottom_pipe1x,y=bottom_pipe1y)
        top_pipe_label1.place(x=bottom_pipe1x,y=bottom_pipe1y-pipe_space)
        bottom_pipe2x-=pipe_speed
        bottom_pipe_label2.place(x=bottom_pipe2x,y=bottom_pipe2y)
        top_pipe_label2.place(x=bottom_pipe2x,y=bottom_pipe2y-pipe_space)
        bottom_pipe3x-=pipe_speed
        bottom_pipe_label3.place(x=bottom_pipe3x,y=bottom_pipe3y)
        top_pipe_label3.place(x=bottom_pipe3x,y=bottom_pipe3y-pipe_space)
        if bottom_pipe1x<-100:
            bottom_pipe1x=bottom_pipe3x+pipe_pause
            bottom_pipe1y=random.randint(225,575)
            pipe1_counted=False
        if bottom_pipe2x<-100:
            bottom_pipe2x=bottom_pipe1x+pipe_pause
            bottom_pipe2y=random.randint(225,575)
            pipe2_counted=False
        if bottom_pipe3x<-100:
            bottom_pipe3x=bottom_pipe2x+pipe_pause
            bottom_pipe3y=random.randint(225,575)
            pipe3_counted=False
        if bottom_pipe1x<birdx and not pipe1_counted:
            score+=1
            pipe1_counted=True
        if bottom_pipe2x<birdx and not pipe2_counted:
            score+=1
            pipe2_counted=True
        if bottom_pipe3x<birdx and not pipe3_counted:
            score+=1
            pipe3_counted=True
        if birdy<=-5 or birdy>=591:
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe1x,bottom_pipe1y,pipe_width,pipe_height):
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe1x,bottom_pipe1y-pipe_space,pipe_width,pipe_height):
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe2x,bottom_pipe2y,pipe_width,pipe_height):
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe2x,bottom_pipe2y-pipe_space,pipe_width,pipe_height):
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe3x,bottom_pipe3y,pipe_width,pipe_height):
            game_over=True
            game_over_func()
        if collision(birdx+5,birdy+5,bird_width-5,bird_height-5,bottom_pipe3x,bottom_pipe3y-pipe_space,pipe_width,pipe_height):
            game_over=True
            game_over_func()
    window1.after(1,scene_movement)

#bird jump func
def bird_jump(event):
    global bird_speed,jump_strength,game_started,score_label,flappy_bird_label,start_label
    if game_started and not game_over:
        bird_speed=-jump_strength
    elif not game_over:
        game_started=True
        high_score_label.place(x=1000,y=1000,anchor="center")
        score_label.place(x=265,y=625,anchor="center")
        start_label.destroy()
        flappy_bird_label.destroy()

#function that checks for collisions
def collision(x1,y1,width1,height1,x2,y2,width2,height2):
    return (x1<x2+width2 and x1+width1>x2 and y1<y2+height2 and y1+height1>y2)

#game over screen
def game_over_func():
    global over_label,score_label,high_score_label,score,high_score
    for widget in window1.winfo_children():
        if widget!=high_score_label and widget!=score_label:
            widget.destroy()
    over_label=tk.Label(window1,text="Game Over",font=("Courier", 44))
    over_label.place(x=265,y=285,anchor="center")
    score_label.place(x=265,y=350,anchor="center")
    if score>high_score:
        high_score=score
    high_score_label.config(text=f"High score: {high_score}")
    high_score_label.place(x=265,y=200,anchor="center")
    high_score_file=open(f"{folder1}/high_score.txt","w")
    high_score_file.write(str(high_score))
    high_score_file.close()

#window
window1=tk.Tk()
window1.title("Flappy Bird")
window1.geometry("550x650")

#bird (5:4)
bird_img=Image.open(bird_path).convert("RGBA")
bird_img_resized=bird_img.resize((bird_width,bird_height))
bird1=ImageTk.PhotoImage(bird_img_resized)
bird_label=tk.Label(window1,image=bird1)
bird_label.place(x=birdx,y=birdy)

#bottom pipe 1
bottom_pipe_img=Image.open(pipe_path).convert("RGBA")
bottom_pipe_img_resized=bottom_pipe_img.resize((pipe_width,pipe_height))
bottom_pipe=ImageTk.PhotoImage(bottom_pipe_img_resized)
bottom_pipe_label1=tk.Label(window1,image=bottom_pipe)
bottom_pipe_label1.place(x=1000,y=1000)

#top pipe 1
top_pipe_img=bottom_pipe_img_resized.transpose(Image.FLIP_TOP_BOTTOM)
top_pipe=ImageTk.PhotoImage(top_pipe_img)
top_pipe_label1=tk.Label(window1,image=top_pipe)
top_pipe_label1.place(x=1000,y=1000)

#bottom pipe 2
bottom_pipe_label2=tk.Label(window1,image=bottom_pipe)
bottom_pipe_label2.place(x=1000,y=1000)

#top pipe 2
top_pipe_label2=tk.Label(window1,image=top_pipe)
top_pipe_label2.place(x=1000,y=1000)

#bottom pipe 3
bottom_pipe_label3=tk.Label(window1,image=bottom_pipe)
bottom_pipe_label3.place(x=1000,y=1000)

#top pipe 3
top_pipe_label3=tk.Label(window1,image=top_pipe)
top_pipe_label3.place(x=1000,y=1000)

#high score label
high_score_label=tk.Label(window1,text=f"High score: {high_score}",font=("Courier", 26))
high_score_label.place(x=265,y=500,anchor="center")

#score label
score_label=tk.Label(window1,text=f"Score: {score}",font=("Courier", 20))

#sarting screen labels
global flappy_bird_label,start_label
flappy_bird_label=tk.Label(window1,text="Flappy bird",font=("Courier", 43))
flappy_bird_label.place(x=265,y=285,anchor="center")
start_label=tk.Label(window1,text="Press Jump to start",font=("Courier", 20))
start_label.place(x=265,y=325,anchor="center")

#binds 
window1.bind("<space>",bird_jump)   
window1.bind("<Return>",bird_jump)  
window1.bind("<Button-1>",bird_jump)
window1.bind("<Button-2>",bird_jump)
window1.bind("<Button-3>",bird_jump)

#runs the scene_movement function
scene_movement()

#loop
window1.mainloop()

#imports
import tkinter as tk 
from PIL import Image, ImageTk
import random

#variables
global birdx,birdy,gravity,bird_speed,jump_strength,pipe_speed,game_started,bottom_pipe1x,bottom_pipe1y,bottom_pipe2x,bottom_pipe2y,bottom_pipe3x,bottom_pipe3y,pipe_pause
game_started=False
birdx=110
birdy=150
gravity=0.002
bird_speed=0
pipe_speed=0.3
jump_strength=0.57
bottom_pipe1x=650
bottom_pipe1y=random.randint(225,575)
bottom_pipe2x=1000
bottom_pipe2y=random.randint(225,575)
bottom_pipe3x=1350
bottom_pipe3y=random.randint(225,575)
pipe_pause=0
pipe_space=935

#pipe and bird movement func
def scene_movement():
    global birdx,birdy,gravity,bird_speed,bottom_pipe1x,bottom_pipe1y,bottom_pipe2x,bottom_pipe2y,bottom_pipe3x,bottom_pipe3y,pipe_pause,game_started,pipe_speed
    if game_started:
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

    
    window1.after(1,scene_movement)

#bird jump func
def bird_jump(event):
    global bird_speed,jump_strength,game_started
    if game_started:
        bird_speed=-jump_strength
    else:
        game_started=True

#window
window1=tk.Tk()
window1.title("Flappy Bird")
window1.geometry("550x650")

#bottom pipe 1
bottom_pipe_img=Image.open("flappy_bird/pipe.png")
bottom_pipe_img_resized=bottom_pipe_img.resize((69,758))
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

#bird (5:4)
global bird_label
bird_img=Image.open("flappy_bird/bird.png")
bird_img_resized=bird_img.resize((70,54))
bird1=ImageTk.PhotoImage(bird_img_resized)
bird_label=tk.Label(window1,image=bird1)
bird_label.place(x=birdx,y=birdy)

#binds 
window1.bind("<space>", bird_jump)   
window1.bind("<Return>", bird_jump)  
window1.bind("<Button-1>", bird_jump)
window1.bind("<Button-2>", bird_jump)
window1.bind("<Button-3>", bird_jump)

scene_movement()

#loop
window1.mainloop()



#imports
import tkinter as tk 
from PIL import Image, ImageTk
import time

#variables
global birdx,birdy,gravity,speed,jump_strength
birdx=100
birdy=150
gravity=0.00086
speed=0
jump_strength=0.4

#pipe and bird movement func
def scene_movement():
    global birdx,birdy,gravity,speed
    bird_label.place(x=birdx,y=birdy)
    speed+=gravity
    birdy+=speed
    window1.after(1,scene_movement)

#bird jump func
def bird_jump(event):
    global speed,jump_strength
    speed=-jump_strength

#window
window1=tk.Tk()
window1.title("Flappy Bird")
window1.geometry("500x650")

#bird image (5:4)
global bird_label
bird_img=Image.open("flappy_bird/bird.png")
bird_img_resized=bird_img.resize((70,54))
bird1=ImageTk.PhotoImage(bird_img_resized)
bird_label=tk.Label(window1,image=bird1)
bird_label.place(x=birdx,y=birdy)


#bottom pipe 2
bottom_pipe_img=Image.open("flappy_bird/pipe.png")
bottom_pipe_img_resized=bottom_pipe_img.resize((75,700))
bottom_pipe1=ImageTk.PhotoImage(bottom_pipe_img_resized)
bottom_pipe_label=tk.Label(window1,image=bottom_pipe1)
bottom_pipe_label.place(x=500,y=0)

#top pipe 1
top_pipe_img=bottom_pipe_img.transpose(Image.FLIP_TOP_BOTTOM)
top_pipe_img_resized=top_pipe_img.resize((75,700))
top_pipe1=ImageTk.PhotoImage(top_pipe_img_resized)
top_pipe_label=tk.Label(window1,image=top_pipe1)
top_pipe_label.place(x=500,y=-700)

#binds 
window1.bind("<space>", bird_jump)   
window1.bind("<Return>", bird_jump)  
window1.bind("<Button-1>", bird_jump)
window1.bind("<Button-2>", bird_jump)
window1.bind("<Button-3>", bird_jump)

scene_movement()

#loop
window1.mainloop()



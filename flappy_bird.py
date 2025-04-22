#imports
import tkinter as tk 
from PIL import Image, ImageTk

#variables
global birdx,birdy
birdx=100
birdy=150

#pipe and bird movement func
def scene_movement():
    global birdx,birdy
    canvas.coords(bird,birdx,birdy)
    birdy+=2
    window1.after(10,scene_movement)

#bird jump func
def bird_jump(event):
    global birdx, birdy
    birdy-=50

#window
window1=tk.Tk()
window1.title("Flappy Bird")
window1.geometry("500x650")

#canvas
canvas=tk.Canvas(window1, width=500, height=650)
canvas.pack()

#bird image (5:4)
global bird_label
bird_img=Image.open("flappy_bird/bird.png")
bird_img_resized=bird_img.resize((70,54))
bird1=ImageTk.PhotoImage(bird_img_resized)
bird=canvas.create_image(birdx,birdy,image=bird1)


#bottom pipe image
bottom_pipe_img=Image.open("flappy_bird/pipe.png")
bottom_pipe_img_resized=bottom_pipe_img.resize((75,700))
bottom_pipe1=ImageTk.PhotoImage(bottom_pipe_img_resized)
bottom_pipe=canvas.create_image(0,0,image=bottom_pipe1)

#top pipe image
top_pipe_img=bottom_pipe_img.transpose(Image.FLIP_TOP_BOTTOM)
top_pipe_img_resized=top_pipe_img.resize((75,700))
top_pipe1=ImageTk.PhotoImage(top_pipe_img_resized)
top_pipe=canvas.create_image(0,0,image=top_pipe1)

#binds 
window1.bind("<space>", bird_jump)   
window1.bind("<Return>", bird_jump)  
window1.bind("<Button-1>", bird_jump)
window1.bind("<Button-2>", bird_jump)
window1.bind("<Button-3>", bird_jump)

scene_movement()

#loop
window1.mainloop()



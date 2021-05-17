#starting here
from tkinter import *
import pygame

root = Tk()
root.title('Test')
root.iconbitmap('C:\\Users\\AKSHAY JOSEPH\\Desktop\\Temp\\BFH\\sample.ico')
root.geometry("500x400")
pygame.mixer.init()

def play():
	pygame.mixer.music.load("C:\\Users\\AKSHAY JOSEPH\\Desktop\\Temp\\BFH\\auth_mono_large.wav")
	pygame.mixer.music.play(loops=0)

def stop():
	pygame.mixer.music.stop()
my_button= Button(root, text="Play", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)
my_button1=Button(root, text="Stop", font=("Helvetica", 32), command=stop)
my_button1.pack(pady=20)

root.mainloop()

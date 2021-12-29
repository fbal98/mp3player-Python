import tkinter as tk
import pygame



# ---- Root and window settings
HEIGHT = 300
WIDTH = 500
root = tk.Tk()
root.title("mp3 player")
root.resizable(False, False)
# ------

canvas = tk.Canvas(width=WIDTH, height=HEIGHT).pack()


def playMp3():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load('sample.wav')
        pygame.mixer.music.play()
        volSlider.set(50)
    except:
        print("There was an error playing mp3")

def stopPlay():
    pygame.mixer.music.fadeout(200)

def vol(self):
    volume = float(volSlider.get())
    volLabel.config(text="volume is " + str(volume))
    pygame.mixer.music.set_volume(volume/100)

def getVol():
    return pygame.mixer.music.get_volume()

playBtn = tk.Button(root, command=playMp3, text="playMp3")
playBtn.pack()

stopBtn = tk.Button(root, command=stopPlay, text="stopPlay")
stopBtn.pack()


volSlider = tk.Scale(root, command=vol, orient="horizontal", resolution=0.1, showvalue=0, length=300)
volSlider.pack()

volLabel = tk.Label(root)
volLabel.pack()

timeLabel = tk.Label(root, text="--:--")
timeLabel.pack()

root.mainloop()


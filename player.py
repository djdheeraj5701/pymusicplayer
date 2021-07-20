import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *

root=Tk(className='Music Player')
root.minsize(400,400)
songs=[]
index=0
pause=True
stop=False
f0=Frame(root)
f0.pack(side='top')
songLabel=Label(f0,text="Now Playing ...")
songLabel.grid(row=0,column=0)
v=StringVar()
nowPlaying = Label(f0, textvariable=v)
nowPlaying.grid(row=1, column=0)
def updateSongLabel():
    global index
    global nowPlaying
    v.set(songs[index][1])

def directoryChooser(songs):
    directory=askdirectory()
    if directory!='':
        while songs!=[]:
            songs.pop()
        SongList = Listbox(f1)
        SongList.grid(row=1, column=0)
        for files in os.listdir(directory):
            if files.endswith(".mp3"):
                songs.append([directory+"/"+files,files])
        for i in songs[::-1]:
            SongList.insert(0, i[1])
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(songs[0][0])
            updateSongLabel()
            pygame.mixer.music.play()
            pygame.mixer.music.pause()
        except:
            pass
        pause = True
        stop = False
def nextSong():
    global index
    index+=1
    if index>=len(songs):
        index=0
    pygame.mixer.music.load(songs[index][0])
    pygame.mixer.music.play()
    updateSongLabel()
def prevSong():
    global index
    index -= 1
    if index < 0 :
        index = len(songs)-1
    pygame.mixer.music.load(songs[index][0])
    pygame.mixer.music.play()
    updateSongLabel()
def playSong():
    global pause
    global stop
    if pause and not stop:
        pygame.mixer.music.unpause()
    if stop and not pause:
        pygame.mixer.music.play()
    pause = True
    stop = False
def pauseSong():
    global pause
    global stop
    pygame.mixer.music.pause()
    pause = True
    stop = False
def stopSong():
    global pause
    global stop
    pygame.mixer.music.stop()
    pause = False
    stop = True

f1=Frame(root)
f1.pack(side='top')
f2=Frame(root)
f2.pack(side='top')
# under f1
chooseDir=Button(f1,text="Choose Folder",bg="light green", command=lambda:directoryChooser(songs))
chooseDir.grid(row=0,column=0)

SongList=Listbox(f1)
SongList.grid(row=1,column=0)

# under f2
prev=Button(f2,text="<<",bg="light green", command=lambda:prevSong())
prev.grid(row=0,column=0)
play=Button(f2,text="i>",bg="light green", command=lambda:playSong())
play.grid(row=0,column=1)
pause1=Button(f2,text="||",bg="light green", command=lambda:pauseSong())
pause1.grid(row=0,column=2)
stop1=Button(f2,text="[]",bg="light green", command=lambda:stopSong())
stop1.grid(row=0,column=3)
next=Button(f2,text=">>",bg="light green", command=lambda:nextSong())
next.grid(row=0,column=4)



root.mainloop()
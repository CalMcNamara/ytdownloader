from __future__ import unicode_literals
import youtube_dl
import pyautogui as pya
import pyperclip
import time 
import keyboard


list_of_links = []

def copy_clipboard():
    # This method would be called to return the highlighted and copyed link from the browser.
    pya.hotkey('ctrl','c')
    time.sleep(1)
    return pyperclip.paste()
def download_video():
    opts = {'noplaylist' : True,        
    'format': 'bestaudio/best', }
    i = 0
    with youtube_dl.YoutubeDL(opts) as ydl:
        for video in list_of_links:
            ydl.download([list_of_links[i]])
            i += 1
def add_link():
    var = copy_clipboard()
    list_of_links.append(var)

while True:
    try:
        if(keyboard.is_pressed('e')):
            while True:
                    
                    try:
                        if(keyboard.is_pressed('ctrl+c')):                                
                            add_link()
                            print('Pressed Ctrl + C')
                            break   
                    except:
                        break
        if(keyboard.is_pressed(';')):
            download_video()
            break
    except:
        break

print(list_of_links)
#opts = {'noplaylist' : True,        c
 #   'format': 'bestaudio/best', }

#with youtube_dl.YoutubeDL(opts) as ydl:
 #   ydl.download(['https://www.youtube.com/watch?v=dP15zlyra3c'])
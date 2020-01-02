import tkinter as tk
from tkinter import ttk
import pyautogui, time

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from pynput import mouse
import pyautogui, sys
import logging

from pynput import keyboard
import sys #to avoid terminal window freeze
import os

from PIL import Image, ImageGrab, ImageDraw
import imageio as io
import keyboard as Keyboard

import uuid #for unique ID generator

class Display:
        capturesize = [50,20] #icon screen capture size x,y in pixels

        def __init__(self):
            self.root = tk.Tk()
            self.root.title("GUI Tabs")
            self.tabControl = ttk.Notebook(self.root)

            self.tab1 = tk.Frame(self.tabControl, bg="green")
            self.tabControl.add(self.tab1, text = "Tab 1")

            self.tab2 = tk.Frame(self.tabControl)
            self.tabControl.add(self.tab2, text = "Tab 2")

            self.tabControl.pack()
            # self.subFrame = tk.Frame(self.tabControl, bg="blue")
            # self.subFrame.pack(side= BOTTOM,expand = 1, fill = "both")

            self.ent1t2 = tk.Entry(self.tab2)
            self.ent1t2.bind("<Return>", self.returnHit)
            self.ent1t2.pack()

            self.btn1t1Text = "Start logging"
            self.btn1t1 = tk.Button(self.tab1, text = self.btn1t1Text, command = self.start_logging)
            self.btn1t1.pack(side= TOP)

            #text pane
            self.framelist = []
            self.timer = tk.StringVar()
            self.ID = []
            self.photo = [] #images container
            self.MouseClicks = [] #text variable in pane - empty at start
            self.panelA = None
            self.buttonA()
            self.viewingPanel()
            self.photos=[]
            self.root.mainloop()
# Changed the method to be executed on button press to 'self.updatePanel()'.
        def buttonA(self):
            # Creating a photoimage object to use image
            im = pyautogui.screenshot(region=(50,50, 100, 100)) #screnshot at spot 50x50. Captures gif. but does not work in listener.
            self.photo = ImageTk.PhotoImage(im)
            self.firstPage = tk.Button(self.tab1, text="Print Text", bd=1, image = self.photo, anchor=tk.CENTER,  command=lambda: self.run_autoclicker())
            self.firstPage.image = self.photo #image inst. attached to button.
            self.firstPage.place(x=0, y=0)
            self.firstPage.pack()

            self.photos = []

        # Changed text string to be empty.
        def viewingPanel(self):
            self.panelA = tk.Label(self.tab2, bg='white', width=65, height=13, padx=3, pady=3, anchor=tk.CENTER, text="")
            self.panelA.place(x=100, y=0)
            self.panelA.pack(side= TOP)

        # Added 'updatePanel' method which updates the label in every button press.
        def updatePanel(self):
            self.panelA.config(text=self.MouseClicks)

#enter text to field - print, and remove text
        def returnHit(self,event):
            self.value = self.ent1t2.get();
            print(self.value)
            self.ent1t2.delete(0,"end")

            self.MouseClicks.append(self.value)
            self.updatePanel
        def update_btn1t1_text(self):
            self.btn1t1.config(text=self.btn1t1Text)


        def create_icon(self,i):
            io.imsave('AAAAAAAAAA.gif', self.photos[i]) #self.photos -is bmp. tkinter accepts only gif, so save to gif
            im2 =tk.PhotoImage(file ='AAAAAAAAAA.gif') #then reopen with Tkinter
            os.remove('AAAAAAAAAA.gif') #remove gif
            return(im2)

#generate buttons, which click at position
        def createGameURLs(self, frameid):
            # self.IMGbutton = []

            # # del self.ID[0]
            for i in range(len(self.photos)):
                if len(self.framelist) < 1: #color first subframe
                    id = uuid.uuid1().int
                    self.ID.append(int(str(id)[-6:]))
                    # print(id)
                else:
                    id = uuid.uuid1().int
                    # print(id)
                    self.ID.append(int(str(id)[-6:]))
                print(self.ID)

                width, height = self.photos[i].size   # Get dimensions of the icon
                draw = ImageDraw.Draw(self.photos[i]) #
                draw.ellipse((width/2-height/20, height/2-height/20, width/2+height/20, height/2+height/20), fill=(255,0,0,255)) #put red dot in the click spot

                self.addDaughterFrame() #-1 is last frame

                # create timer selector
                timerOPTIONS = ["0.1 s","0.1 s","0.5 s"," 1 s"," 1.5 s"] #etc
                self.timer.set(timerOPTIONS[-1]) # default value
                self.timerDropDown = ttk.OptionMenu(self.framelist[frameid], self.timer, *timerOPTIONS)
                self.timerDropDown.pack( side=LEFT)

                icon = self.create_icon(i)
                self.IMGbutton = tk.Button(self.framelist[frameid],image = icon)
                self.IMGbutton['command'] =lambda idx=self.ID[-1]: self.open_this(idx)
                self.IMGbutton.image = icon #image inst. attached to button.
                self.IMGbutton.pack(side=LEFT)

                # # create the buttons to edti and remove clickers
                # self.editbutton = tk.Button(self.framelist[frameid], text="Edit", width=10, height=2)
                # self.editbutton['command'] = lambda idx=self.ID[-1], binst=self.editbutton: self.editaction(idx)
                # self.editbutton.pack( side=LEFT)
                #
                self.clearbutton = tk.Button(self.framelist[frameid], text="Clear", width=10, height=2)
                self.clearbutton['command'] = lambda idx=self.ID[-1], binst=self.clearbutton: self.clearaction(idx)
                self.clearbutton.pack( side=LEFT)


            print(self.ID)
            # self.run_autoclicker() #testing auto clicking

        def addDaughterFrame (self):
            if len(self.framelist) < 1: #color first subframe
                self.framelist.append(tk.Frame(self.tab1,bg='red'))
            else:
                self.framelist.append(tk.Frame(self.tab1,bg='blue'))
            # self.framelist[-1].place(anchor = "center", relx = 0.5, rely = 0.5, relwidth = 0.96, relheight = 0.96)
            self.framelist[-1].pack(side= TOP,fill=BOTH, expand=1)


        def editaction(self,idx):
            # self.photos = []
            # self.start_logging()
            # print(idx)
            # print("edit ", self.framelist)
            # print("edit ", self.photos)
            # self.clearaction(idx)
            # self.createGameURLs(idx)

            pass
        def clearaction(self, idx):
            # print(self.framelist)
            id = self.ID.index(idx)
            print('self ID', self.ID)
            print('id', id)

            self.framelist[id].pack_forget()
            self.framelist[id].destroy()
            del self.framelist[id]
            del self.photos[id]
            del self.ID[id]
            del self.MouseClicks[id]
            self.updatePanel()
            print("clear", self.framelist)
            print("clear", self.photos)

            print('self ID after', self.ID)

#each button is enabled to click the mouse at position - so you can test where it clicks.
        def open_this(self, myNum):
            # print(self.ID.index(myNum))
            id = self.ID.index(myNum)
            print(self.MouseClicks[id])
            CurserPos = pyautogui.position()
            pyautogui.click(self.MouseClicks[id]) #execute click
            time.sleep(0.1)
            pyautogui.moveTo(CurserPos) #return mouse

        def run_autoclicker(self):
            CurserPos = pyautogui.position()
            for i in range(len(self.MouseClicks)):
                print(self.timer.get())
                delay = float(self.timer.get().strip(' s'))
                time.sleep(delay)

                pyautogui.click(self.MouseClicks[i]) #execute clikc
                if Keyboard.is_pressed('esc'):
                    print("\nyou pressed Esc, so exiting...")
                    sys.exit(0)
            pyautogui.moveTo(CurserPos) #return mouse

# keyboard logger - quits logging if esc pressed
        def on_press(self,key):
            print(key)
            if key == keyboard.Key.esc:
                return False # Stop listener
            else:
                    pass

# mouse click capture - any mouse button
        def on_click(self,*args):
            # MousePos = args[0]+10,args[1]
            MousePos = args[0],args[1]
            self.MouseClicks.append(MousePos)
            x,y =Display.capturesize
            im = ImageGrab.grab(bbox =(MousePos[0]-x,MousePos[1]-y, MousePos[0]+y,MousePos[1]+y)) #bbox Xmin, Ymmax, Xmax, Ymin
            self.photos.append(im)

# mouse scroll capture - just scroll, not press. Press goes to mouse click
        def on_scroll(self,x, y, dx, dy):
            sys.stdout.write('Scrolled {0}'.format((x, y)))

#logger starting - listen for clicks
        def start_logging(self):
            print("Start logging")
            self.btn1t1Text = "press ESC to stop"
            self.update_btn1t1_text()
            self.root.update() #to show text "ESC to stop"

            self.MouseClicks = [] #text variable in pane - empty at start
            self.updatePanel()
            self.click_logging()
            self.createGameURLs(-1)

        def click_logging(self):
            with mouse.Listener(
                        on_click = self.on_click,
                        on_scroll = self.on_scroll) as L:
                        with keyboard.Listener(
                                on_press=self.on_press) as L:
                                L.join()
            self.MouseClicks = self.MouseClicks[::2] #drop out every second line, as it two listeners double the output.
            self.photos = self.photos[::2] #drop out every second line, as it two listeners double the output.
            self.updatePanel()
            self.btn1t1Text = "Start logging"
            self.update_btn1t1_text()

display1 = Display()

from tkinter import *
from PIL import ImageTk, Image  
import webbrowser

DATA=0
NOTIFY_DURATION = 5000
url="http://rehabcall.in/mrergo/MrErgo.php?id="

def notification():
    root = Tk()

    NOTIFY_MSG = StringVar()
    global DATA

    if (DATA<=4):
        if(DATA==0):
            NOTIFY_MSG.set('Welcome Reminders')
        elif (DATA==1):
            NOTIFY_MSG.set('Take a Refreshing Break')
        elif (DATA==2):
            NOTIFY_MSG.set('Screen brightness and contrast')
        elif (DATA==3):
            NOTIFY_MSG.set('Have a Healthy Meal')
        elif (DATA==4):
            NOTIFY_MSG.set('Posture and Neck Exercise')
            DATA=0
    else:
        DATA=0



    #removes title bar and the minimize, maximize, close buttons
    root.overrideredirect(True)
    root.wm_overrideredirect(True)

    root.call("wm", "attributes", ".", "-topmost", "true") # Always keep window on top of others
    # root.call("wm", "attributes", ".", "-alpha", "1.0") # Window Opacity 0.0-1.0
    root.wm_attributes("-transparentcolor", "white") #makes white color transparent
 
    # background image
    bgimage = Image.open("blue-cloud.png")
    bg=ImageTk.PhotoImage(bgimage)
    bglabel = Label(root, image=bg, bg='white')
    bglabel.image=bg
    bglabel.place(x=0,y=0,relwidth=1,relheight=1)
    frame=Frame(root, bg="#6797E9")
    frame.pack(side=RIGHT,padx=(0,70), pady=(30,0))

    bottomframe=Frame(root, bg="#6797E9")
    bottomframe.pack(side=LEFT,padx=(30,0), pady=(40,0))

    def open_url(event):
        webbrowser.open_new(url+str(DATA-1))
        root.destroy()

    w=305
    h=190
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = ws-w
    y = hs-h-50
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    image1 = Image.open("ergo-final.png")
    test=ImageTk.PhotoImage(image1)
    label1 = Label(frame,image=test,bg='#6797E9')
    label1.image = test

    ntitle=Label(bottomframe,text="Mr.Ergo Reminders", bg="#6797E9")

    nmsg=Label(bottomframe,textvariable=NOTIFY_MSG, bg="#6797E9")

    label1.pack(side=RIGHT)
    ntitle.pack(side=TOP, anchor='w')
    nmsg.pack(side=BOTTOM, anchor='w')

    root.bind('<Button-1>',open_url)

    root.after(NOTIFY_DURATION, lambda: root.destroy())
    DATA+=1
    root.mainloop()
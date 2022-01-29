import mysql.connector
import time
import tkinter as tk
from tkinter import *
# from tkinter.ttk import *
from random import *
from PIL import ImageTk, Image
import threading



root = Tk()
root.title('Brainnuttr')
root.geometry("960x560")

#setting bg img
image_home = Image.open('main.png')
img_home = ImageTk.PhotoImage(image_home)
label_img = Label(root, image=img_home)
label_img.place(x=0, y=0)
answer_label = None
# streak
with open("streak.txt", "r") as f:
    streak = int(f.read())


db = mysql.connector.connect(
    host="localhost", user="root", db="bntr", passwd="sid2baddy")
cursor = db.cursor()

global sno
streak = 0

with open("sno.txt", "r") as flogin:
    sno = int(flogin.read())


# _________________________CHEMISTRY starts_________________________________________________

# randomizing  function

def random_q():
    global answer_label, cvallist, ckeylist
    answer_label.config(text="")
    # create a list of questions
    global our_questions
    our_questions = {'(n-1)d^5ns^2': "2",
                     '1.51': "1",
                     '1':'1',
                     '2.1 x 10^-28': "3",
                     '10^-33': "4",
                     'Ca':'3',
                     'linkage': "2",
                     'NaCl':'4',
                     'Rb':'3',
                     "Swart's reaction": '2'
                     }
    ckeylist = list(our_questions.keys())
    cvallist = list(our_questions.values())
    # random question generator
    global rando
    rando = randint(0, len(our_questions) - 1)
    chemy = "chem/" + ckeylist[rando] + ".png"

    # create the question images
    global chem_img
    chem_img = ImageTk.PhotoImage(Image.open(chemy))
    show_img.config(image=chem_img)
# sets timer before going to next question


def timer1(sec, func):
    time.sleep(sec)
    func()


# create frames
chem_frame = Frame(root, width=500, height=500)
phy_frame = Frame(root, width=500, height=500)
bio_frame = Frame(root, width=500,height=500) 
login_frame = Frame(root, width=300,height=300)


# answer functions
def chem_answer():
    global answer_label, streak
    answer = answer_input.get()
    if answer == cvallist[rando]:
        response = "Correct!" + " " + ckeylist[rando]
        streak += 1
    else:
        response = "Incorrect!" + " " + ckeylist[rando]
        streak = 0
    answer_label.config(text=response)
    # clear box
    answer_input.delete(0, 'end')

    with open("streak.txt", "w") as f:
        f.write(str(streak))

    t1 = threading.Thread(target=timer1, args=(3, random_q))
    t1.start()

# flashcard functions


def chem():
    hide_all_frames()
    chem_frame.pack(fill="both", expand=1)


    global show_img
    show_img = Label(chem_frame)
    show_img.pack(pady=15)

    # create answer input box
    global answer_input
    answer_input = Entry(chem_frame, font=("Heletica", 18))
    answer_input.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(chem_frame, text="SKIP", command=chem)
    rando_button.pack(pady=10)

    # label to tell if its right answer is
    global answer_label
    answer_label = Label(chem_frame, text="", font=("Heletica", 18))
    answer_label.pack(pady=15)

    random_q()

    # create button to answer the questions
    text_button = Button(chem_frame, text="Answer", command=chem_answer)
    text_button.pack(pady=5)

    # create button to answer the questions
    answer_button = Button(chem_frame, text="Note: Input should be the option as 1,2,3,4")
    answer_button.pack(pady=5)

    #status

    def button_hover(e):
        status_label.config(text=f"Your Current Streak is {streak}")
    def button_hover_leave(e):
        status_label.config(text="")

    status_button = Button(chem_frame, text="Want to know your streak?")
    status_button.pack(pady=2)

    status_label = Label(chem_frame, text='',relief = SUNKEN , anchor =E)
    status_label.pack(fill=X, sid=BOTTOM, ipady=2)

    status_button.bind("<Enter>",button_hover)
    status_button.bind("<Leave>", button_hover_leave)
    


# _________________________CHEMISTRY ends__________________________________________________

# _________________________PHYSICS starts _________________________________________________

answer_label1 = None

def random_q1():
    global answer_label1, pkeylist, pvallist
    answer_label1.config(text="")
    # create a list of questions
    global our_questions1
    our_questions1 = {'1': "1",
                      '3': "2",
                      '6':'3',
                      '55': "2",
                      '100':'3',
                      'converge':'3',
                      'due north': "1",
                      'straight line' :'3',
                      'Three':'3',
                      'X-rays':'3',
                      }
    pkeylist = list(our_questions1.keys())
    pvallist = list(our_questions1.values())

    # random question generator
    global rando1
    rando1 = randint(0, len(our_questions1) - 1)
    phyy = "phy/" + pkeylist[rando1] + ".png"

    # create the question images
    global phy_img
    phy_img = ImageTk.PhotoImage(Image.open(phyy))
    show_img1.config(image=phy_img)
# sets timer before going to next question

def timer(sec, func):
    time.sleep(sec)
    func()


# answer functions
def phy_answer():
    global answer_label1, streak
    answer1 = answer_input1.get()
    if answer1 == pvallist[rando1]:
        response = "Correct!" + " " + pkeylist[rando1]
        streak += 1
    else:
        response = "Incorrect!" + " " + pkeylist[rando1]
        streak = 0
    answer_label1.config(text=response)
    # clear box
    answer_input1.delete(0, 'end')

    with open("streak.txt", "w") as f:
        f.write(str(streak))

    t1 = threading.Thread(target=timer, args=(3, random_q1))
    t1.start()

# flashcard functions


def phy():
    hide_all_frames()
    phy_frame.pack(fill="both", expand=1)
    # my_label = Label(chem_frame, text="Chemistry").pack()

    global show_img1
    show_img1 = Label(phy_frame)
    show_img1.pack(pady=15)

    # create answer input box
    global answer_input1
    answer_input1 = Entry(phy_frame, font=("Heletica", 18))
    answer_input1.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(phy_frame, text="SKIP", command=phy)
    rando_button.pack(pady=5)

    # label to tell if its right answer is
    global answer_label1
    answer_label1 = Label(phy_frame, text="", font=("Heletica", 18))
    answer_label1.pack(pady=5)

    random_q1()

    # create button to answer the questions
    text_button = Button(phy_frame, text="Answer", command=phy_answer)
    text_button.pack(pady=5)

    # create button to answer the questions
    answer_button = Button(
        phy_frame, text="Note: Input should be the option as 1,2,3,4")
    answer_button.pack(pady=5)

    #status

    def button_hover1(e):
        status_label1.config(text=f"Your Current Streak is {streak}")

    def button_hover_leave1(e):
        status_label1.config(text="")

    status_button1 = Button(phy_frame, text="Want to know your streak?")
    status_button1.pack(pady=2)

    status_label1 = Label(phy_frame, text='', relief=SUNKEN, anchor=E)
    status_label1.pack(fill=X, sid=BOTTOM, ipady=2)

    status_button1.bind("<Enter>", button_hover1)
    status_button1.bind("<Leave>", button_hover_leave1)
    
# ----------------------------------------------PHYSICS ends--------------------------------


#-----------------------------------------------BIOLOGY STARTS-----------------------------


answer_label2 = None


def random_q2():
    global answer_label2, bkeylist, bvallist
    answer_label2.config(text="")
    # create a list of questions
    global our_questions2
    our_questions2 = {'acetylcholine': "1",
                      'Dura mater': "1",
                      'Leukovirus': "4",
                      'Limbic system': "2",
                      'Measles': "2",
                      'neuromuscular junction' :'3',
                      'Pro-plastid':'3',
                      'Rhodoplast':'3',
                      'Simple reflex' :'2',
                      'Virus':'3'
                     }
    bkeylist = list(our_questions2.keys())
    bvallist = list(our_questions2.values())

    # random question generator
    global rando2
    rando2 = randint(0, len(our_questions2) - 1)
    bioy = "bio/" + bkeylist[rando2] + ".png"

    # create the question images
    global bio_img
    bio_img = ImageTk.PhotoImage(Image.open(bioy))
    show_img2.config(image=bio_img)
# sets timer before going to next question


def timer(sec, func):
    time.sleep(sec)
    func()


# answer functions
def bio_answer():
    global answer_label2, streak
    answer2 = answer_input2.get()
    if answer2 == bvallist[rando2]:
        response = "Correct!" + " " + bkeylist[rando2]
        streak += 1
    else:
        response = "Incorrect!" + " " + bkeylist[rando2]
        streak = 0
    answer_label2.config(text=response)
    # clear box
    answer_input2.delete(0, 'end')

    with open("streak.txt", "w") as f:
        f.write(str(streak))

    t2 = threading.Thread(target=timer, args=(3, random_q2))
    t2.start()

# flashcard functions


def bio():
    hide_all_frames()
    bio_frame.pack(fill="both", expand=1)
    # my_label = Label(chem_frame, text="Chemistry").pack()

    global show_img2
    show_img2 = Label(bio_frame)
    show_img2.pack(pady=15)

    # create answer input box
    global answer_input2
    answer_input2 = Entry(bio_frame, font=("Heletica", 18))
    answer_input2.pack(pady=15)

    # create button to randomize state images
    rando_button = Button(bio_frame, text="SKIP", command=bio)
    rando_button.pack(pady=5)

    # label to tell if its right answer is
    global answer_label2
    answer_label2 = Label(bio_frame, text="", font=("Heletica", 18))
    answer_label2.pack(pady=5)

    random_q2()

    # create button to answer the questions
    text_button = Button(bio_frame, text="Answer", command=bio_answer)
    text_button.pack(pady=5)

    # create button to answer the questions
    answer_button = Button(bio_frame, text="Note: Input should be the option as 1,2,3,4")
    answer_button.pack(pady=5)

    #status

    def button_hover2(e):
        status_label1.config(text=f"Your Current Streak is {streak}")

    def button_hover_leave2(e):
        status_label1.config(text="")

    status_button1 = Button(bio_frame, text="Want to know your streak?")
    status_button1.pack(pady=2)

    status_label1 = Label(bio_frame, text='', relief=SUNKEN, anchor=E)
    status_label1.pack(fill=X, sid=BOTTOM, ipady=2)

    status_button1.bind("<Enter>", button_hover2)
    status_button1.bind("<Leave>", button_hover_leave2)

#-------------------------------------------BIOLOGY Ends--------------------------------


#---------------------------------LOGIN STUFF------------------------------------------

def login():
    hide_all_frames()
    global user, passw, sno
    sno += 1

    user = Username.get()
    # passw = password.get()
    print(type(Username),dir(Username), sep ='\n')
    
    with open("sno.txt", "w") as flogin:
        flogin.write(str(sno))
    #query = "insert into login(id,name,score,password)values({},'{}',{},'{}')".format(sno, user, streak, passw)

    #cursor.execute(query)
    db.commit()
    

label1 = tk.Label(login_frame, text="Username -", )
label1.place(x=50, y=20)

Username =tk.Entry(login_frame, width=500)
Username.place(x=150, y=20, width=100)

label2 = tk.Label(login_frame, text="Password -")
label2.place(x=50, y=50)

password = tk.Entry(login_frame, width=500)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(login_frame, text="Login", command=login)
submitbtn.place(x=130, y=135, width=55)

home_btn = tk.Button(login_frame, text="Go to Home", command=chem)
home_btn.place(x=130, y=135, width=55)



#------------------------------------------------------------

# hide previous frames
def hide_all_frames():
    # doesnt allow the same thing to come second time
    for widget in chem_frame.winfo_children():
        widget.destroy()
    for widget in phy_frame.winfo_children():
        widget.destroy()
    for widget in bio_frame.winfo_children():
        widget.destroy()
    for widget in login_frame.winfo_children():
        widget.destroy()

    chem_frame.pack_forget()
    phy_frame.pack_forget()
    bio_frame.pack_forget()
    login_frame.pack_forget()


# menu
my_menu = Menu(root)
root.config(menu=my_menu)

# menu items
sub_menu = Menu(my_menu)
my_menu.add_cascade(label="Subject", menu=sub_menu)
sub_menu.add_command(label="Chemistry", command=chem)
sub_menu.add_command(label="Physics", command=phy)
sub_menu.add_command(label="Biology", command=bio)
sub_menu.add_command(label="Login", command=login)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=root.quit)

root.mainloop()

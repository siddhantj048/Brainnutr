import time
from tkinter import *
from tkinter.ttk import *
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


# _________________________CHEMISTRY starts_________________________________________________

# randomizing  function

def random_q():
    global answer_label
    answer_label.config(text="")
    # create a list of questions
    global our_questions
    our_questions = ['(n-1)d^5ns^2', '1.51', '2.1 x 10^-28', '10^-33','linkage']

    # random question generator
    global rando
    rando = randint(0, len(our_questions) - 1)
    chemy = "chem/" + our_questions[rando] + ".png"

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


# answer functions
def chem_answer():
    global answer_label, streak
    answer = answer_input.get()
    if answer.lower() == our_questions[rando]:
        response = "Correct!" + " " + our_questions[rando]
        streak += 1
    else:
        response = "Incorrect!" + " " + our_questions[rando]
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
    # my_label = Label(chem_frame, text="Chemistry").pack()

    # create a list of questions
    '''
    global our_questions
    our_questions = ['a','b','c','d']
    #random question generator
    global rando
    rando = randint(0,len(our_questions)-1)
    chemy = "chem/" + our_questions[rando] + ".png"
    #create the question images
    global chem_img
    chem_img = ImageTk.PhotoImage(Image.open(chemy))
    '''
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
    answer_button = Button(chem_frame, text="Note : Answer options as numeric numbers not option. For powers use ^")
    answer_button.pack(pady=5)

    #status

    def button_hover(e):
        status_label.config(text=f"Your Current Streak is {streak}")
    def button_hover_leave(e):
        status_label.config(text="")

    status_button = Button(chem_frame, text="Wnt to know your streak?")
    status_button.pack(pady=2)

    status_label = Label(chem_frame, text='',relief = SUNKEN , anchor =E)
    status_label.pack(fill=X, sid=BOTTOM, ipady=2)

    status_button.bind("<Enter>",button_hover)
    status_button.bind("<Leave>", button_hover_leave)
    


# _________________________CHEMISTRY ends__________________________________________________

# _________________________PHYSICS starts _________________________________________________

answer_label1 = None

def random_q1():
    global answer_label1
    answer_label1.config(text="")
    # create a list of questions
    global our_questions1
    our_questions1 = ['3', '10^-12','16.5', '55', 'due north']

    # random question generator
    global rando1
    rando1 = randint(0, len(our_questions1) - 1)
    phyy = "phy/" + our_questions1[rando1] + ".png"

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
    if answer1.lower() == our_questions1[rando1]:
        response = "Correct!" + " " + our_questions1[rando1]
        streak += 1
    else:
        response = "Incorrect!" + " " + our_questions1[rando1]
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
        phy_frame, text="Note : Answer options as numeric numbers not option. For powers use ^")
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
    
# ----------------------------------------------physics ends-----------------------

# hide previous frames
def hide_all_frames():
    # doesnt allow the same thing to come second time
    for widget in chem_frame.winfo_children():
        widget.destroy()
    for widget in phy_frame.winfo_children():
        widget.destroy()

    chem_frame.pack_forget()
    phy_frame.pack_forget()


# menu
my_menu = Menu(root)
root.config(menu=my_menu)

# menu items
sub_menu = Menu(my_menu)
my_menu.add_cascade(label="Subject", menu=sub_menu)
sub_menu.add_command(label="Chem", command=chem)
sub_menu.add_command(label="Phy", command=phy)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=root.quit)

root.mainloop()

import time
from tkinter import *
from tkinter.ttk import *
from random import *
from PIL import ImageTk, Image
import threading
root = Tk()
root.title('Brainnuttr')
root.geometry("950x500")

answer_label = None
# streak
with open("streak.txt", "r") as f:
    streak = int(f.read())


# _________________________CHEMISTRY starts_________________________________________________

# randomizing  function

def random_q():
    print (1)
    global answer_label
    answer_label.config(text="")
    # create a list of questions
    global our_questions
    our_questions = ['(n-1)d^5ns^2', '1.51', '2.1 x 10^-28', '10^-33']

    # random question generator
    global rando
    rando = randint(0, len(our_questions) - 1)
    chemy = "chem/" + our_questions[rando] + ".png"

    # create the question images
    global chem_img
    chem_img = ImageTk.PhotoImage(Image.open(chemy))
    show_img.config(image=chem_img)
# sets timer before going to next question
def timer(sec,func):
    time.sleep(sec)
    func()

# create frames
chem_frame = Frame(root, width=500, height=500)
phy_frame = Frame(root, width=500, height=500)


# answer functions
def chem_answer():
    global answer_label,streak
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

    t1= threading.Thread(target=timer, args=(3,random_q))
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


# _________________________CHEMISTRY ends__________________________________________________


# _________________________PHYSICS starts _________________________________________________

def phy():
    hide_all_frames()
    phy_frame.pack(fill="both", expand=1)
    # my_label = Label(phy_frame, text="Physics").pack()


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

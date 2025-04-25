import tkinter as tk
import random

bot_choice = random.randint(1,3)

def rock():

def paper():

def scissors():

main = tk.Tk()
main.title("Guess the Number!")

label_guess = tk.Label(main, text="Which one?")
label_guess.pack()

rock1 = PhotoImage("rock.png")
paper1 = PhotoImage("paper.png")
scissors1 = PhotoImage("scissors.png")

button_rock = tk.Button(main, image=rock1, command=rock)
button_rock.pack()

button_paper = tk.Button(main, image=paper1, command=paper)
button_paper.pack()

button_scissors = tk.Button(main, image=scissors1, command=scissors)
button_scissors.pack()

label_result = tk.Label(main, text="")
label_result.pack()

main.mainloop()

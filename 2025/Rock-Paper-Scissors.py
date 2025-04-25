import tkinter as tk
from tkinter import PhotoImage
import random

bot_choice = random.randint(1,3)# 1 = rock, 2 = paper, 3 = scissors

def rock():
  if bot_choice == 1:
    label_result.config(text="Rock! Go Again!")
  if bot_choice == 2:
    label_result.config(text="Paper! You lose!")
  if bot_choice == 3:
    label_result.config(text="Scissors! You win!")

def paper():
  if bot_choice == 1:
    label_result.config(text="Rock! You win!")
  if bot_choice == 2:
    label_result.config(text="Paper! Go Again!")
  if bot_choice == 3:
    label_result.config(text="Scissors! You lose!")

def scissors():
  if bot_choice == 1:
    label_result.config(text="Rock! You lose!")
  if bot_choice == 2:
    label_result.config(text="Paper! You win!")
  if bot_choice == 3:
    label_result.config(text="Scissors! Go again!")

main = tk.Tk()
main.title("Guess the Number!")
main.geometry("960x600")

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

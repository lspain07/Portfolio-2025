import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random

# 1 = rock, 2 = paper, 3 = scissors

win = 0
loss = 0
draw = 0

def rock():
  bot_choice1 = random.randint(1,3)
  global win, loss, draw
  if bot_choice1 == 1:
    label_result.config(text="Rock! Go again!")
    draw += 1
    draw_counter.config(text=f"Draws: {draw}")
  if bot_choice1 == 2:
    label_result.config(text="Paper! You lose!")
    loss += 1
    loss_counter.config(text=f"Losses: {loss}")
  if bot_choice1 == 3:
    label_result.config(text="Scissors! You win!")
    win += 1
    win_counter.config(text=f"Wins: {win}")

def paper():
  bot_choice2 = random.randint(1,3)
  global win, loss, draw
  if bot_choice2 == 1:
    label_result.config(text="Rock! You win!")
    win += 1
    win_counter.config(text=f"Wins: {win}")
  if bot_choice2 == 2:
    label_result.config(text="Paper! Go again!")
    draw += 1
    draw_counter.config(text=f"Draws: {draw}")
  if bot_choice2 == 3:
    label_result.config(text="Scissors! You lose!")
    loss += 1
    loss_counter.config(text=f"Losses: {loss}")

def scissors():
  bot_choice3 = random.randint(1,3)
  global win, loss, draw
  if bot_choice3 == 1:
    label_result.config(text="Rock! You lose!")
    loss += 1
    loss_counter.config(text=f"Losses: {loss}")
  if bot_choice3 == 2:
    label_result.config(text="Paper! You win!")
    win += 1
    win_counter.config(text=f"Wins: {win}")
  if bot_choice3 == 3:
    label_result.config(text="Scissors! Go again!")
    draw += 1
    draw_counter.config(text=f"Draws: {draw}")

main = tk.Tk()
main.title("Rock! Paper! Scissors!")

label_guess = tk.Label(main, text="Which one?")
label_guess.pack()

label_result = tk.Label(main, text="")
label_result.pack()

win_counter = tk.Label(main, text=f"Wins: {win}")
win_counter.pack()

loss_counter = tk.Label(main, text=f"Losses: {loss}")
loss_counter.pack()

draw_counter = tk.Label(main, text=f"Draws: {draw}")
draw_counter.pack()

rock1 = Image.open('rock.png')
rock1 = ImageTk.PhotoImage(rock1)
paper1 = Image.open('paper.png')
paper1 = ImageTk.PhotoImage(paper1)
scissors1 = Image.open('scissors.png')
scissors1 = ImageTk.PhotoImage(scissors1)

button_rock = tk.Button(main, image=rock1, command=rock)
button_rock.pack(side=tk.LEFT)

button_paper = tk.Button(main, image=paper1, command=paper)
button_paper.pack(side=tk.LEFT)

button_scissors = tk.Button(main, image=scissors1, command=scissors)
button_scissors.pack(side=tk.LEFT)

main.mainloop()

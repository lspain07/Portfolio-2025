import tkinter as tk
import random 

def game():
    while True:
        try:
            guess = int(entry_guess.get())
            answer = random.randint(1,10)
            if guess == answer:
                label_result.config(text="Yep! You got it right!")
                break
            elif guess > 10 or guess < 1:
                label_result.config(text="You idiot! That's not in the range!")
                break
            else:
                label_result.config(text=f"You got it wrong! The answer was {answer}!")
                break
        except ValueError:
            label_result.config(text="Invalid input. Please enter a whole number.")
        except KeyboardInterrupt:
            label_result.config(text="Invalid input. Please enter a whole number.")
            
main = tk.Tk()
main.title("Guess the Number!")

label_guess = tk.Label(main, text="Guess:")
label_guess.pack()

entry_guess = tk.Entry(main)
entry_guess.pack()

button_getanswer = tk.Button(main, text="Answer?", command=game)
button_getanswer.pack()

label_result = tk.Label(main, text="")
label_result.pack()

main.mainloop()

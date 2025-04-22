import tkinter as tk
import random 

def clear():
    entry_guess.delete(0, tk.END)

def game():
    while True:
        try:
            guess = int(entry_guess.get())
            answer = random.randint(1,10)
            if guess == answer:
                label_result.config(text="Yep! You got it right!")
                clear()
                break
            elif guess > 10 or guess < 1:
                label_result.config(text="You idiot! That's not in the range!")
                clear()
                break
            else:
                label_result.config(text=f"You got it wrong! The answer was {answer}!")
                clear()
                break
        except ValueError:
            label_result.config(text="Invalid input. Please enter a whole number.")
            clear()
            break
        except KeyboardInterrupt:
            label_result.config(text="Invalid input. Please enter a whole number.")
            clear()
            break
            
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

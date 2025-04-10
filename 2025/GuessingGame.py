import random
def game():
    while True:
        try:
            guess = int(input("Guess a number from 1 to 10: "))
            answer = random.randint(1,10)
            if guess == answer:
                print("You got it right!")
                break
            elif guess > 10 or guess < 1:
                print("You idiot! That's not in the range!")
            else:
                print("You got it wrong! The answer was " + str(answer) + "!")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except KeyboardInterrupt:
            print("Invalid input. Please enter a whole number.")
while True:
    try:
        game()
        query = input("Keep going? (y/n): ")
        if query.lower() != "y":
            break
    except KeyboardInterrupt:
            break

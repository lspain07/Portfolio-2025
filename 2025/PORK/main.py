import random

def help():
  print("")

def inventory():
  print("")
  
print("""
PORK: A Text-Based Adventure Game By Lukas Spain\n
Type "help" for a tutorial and a list of commands\n
A young boy was kidnapped by an evil wizard named Snort\n
You are a mercenary hired by his parents to recover him\n
He was dragged into the forest last night\n\n
You are standing to the south of the forest in a wide green clearing\n
There is a path ripped through the brush
""")

def forest3():
    print("")

def forest2():
    while True:
        try:
            move3 = str(input(""))
            if move3.capitalize() == "W":
                print("""
                
                """)
                forest3()
                break
            elif move3 == "inventory":
                inventory()
            elif move3 == "help":
                help()
        except ValueError:
            print("")
        except KeyboardInterrupt:
            print("")


def forest1():
  while True:
    try:
        move2 = str(input(""))
        if move2.capitalize() == "S":
            print("""
            You retreat from the forest back to the clearing, listening as the rustling continues
            """)
            forest2()
            break
        elif move2.capitalize() == "W" or "E":
            print("The forest is too dense to go that way")
        elif move2 == "inventory":
          inventory()
        elif move2 == "help":
          help()
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

def forest():
  while True:
    try:
      move1 = str(input(""))
      if move1.capitalize() == "N":
        print("""
        You take your first step into the forest path\n
        Darkness encroaches upon you, and you hear the rustling of beasts in the bushes around you\n
        You can not see anything in the dark, but the rustling is getting closer
        """)
        forest1()
        break
      elif move1 == "inventory":
        inventory()
      elif move1 == "help":
        help()
      else:
        print("There is nothing for you that way")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

forest()

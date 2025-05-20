import random

items = ["longsword","lantern"]

#class #gonna have to learn how to use classes to make all "move" variables applicable under the quit function

#def quit(): #this needs to return the false boolean value if the player ever types "quit"
#if 

def help():
  print("""
  Tutorial:\n
  PORK is controlled generally through directional commands
  Type "n" for north, "s" for south, and so on (there is no "ne" or "sw" for in-between directions, however)
  There will be enemies and opponents you will come upon that will require slaying
  Generally, a weapon is required to make it out of combat alive
  You start with a single "longsword" and a "lantern"
  You can access your held items by typing "inventory"\n
  An example scenario within PORK:\n
  You type "n" to move forward within an area
  Suddenly, a bandit jumps from the brush around you and brandishes a gleaming scimitar, snarling with yellowed teeth and hungry eyes\n
  What do you do?
  Typing a directional command could get you away from the situation...sometimes it won't
  If you possess a weapon, let's use our longsword example, and you type "longsword"
  You will attack with the chosen weapon and, hopefully, defeat the enemy\n
  UH OH!\n
  The bandit parries away your longsword and you drop it several meters away in the bushes\n
  What now?\n
  Some enemies are skilled in weaponry, more skilled than your character, and some have armor and hide so dense you could never hope to penetrate it
  There is no numerical value that represents these qualities, you must simply reason whether you think your relatively inexperienced regular human mercenary could overcome this problem through single combat
  If he can't, and you try to face it anyway, you'll die
  Dying puts you at the last checkpoint\n
  Welp, that's it
  Have fun! Try to get the highest score possible!
  """)

def inventory():
  print(items)
  
print("""
PORK: A Text-Based Adventure Game By Lukas Spain\n
Type "help" for a tutorial and a list of commands or "quit" at any time to exit the game\n
A young boy was kidnapped by an evil wizard named Snort
You are a mercenary hired by his parents to recover him
He was dragged into the forest last night\n
You are standing to the south of the forest in a wide green clearing
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
            elif move3 == false:
                break
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
        elif move3 == false:
          break
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
      elif move3 == false:
        break
      else:
        print("There is nothing for you that way")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

forest()

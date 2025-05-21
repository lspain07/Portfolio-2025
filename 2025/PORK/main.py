import random
import sys

items = ["longsword","lantern"]
lantern_status = False #False = off/True = on

#class/should probably use classes to simply player commands

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

def forest7():
  print("")

def forest6():
  print("")

def forest5():
  global lantern_status
  global inventory
  while True:
    try:
      move6 = str(input(""))
      if move6.capitalize == "N":
        print("""
        The brambles still block any further travel along the path
        """)
      elif move6 == "longsword" and lantern_status == True:
        print("""
        You manage to roughly chop yourself a hole in the wall of thorns after swinging the blade like a machete for a minute
        The forest is still dark ahead, but your lantern is a good enough light to make your way
        """)
        break
        forest6()
      elif move6 == "longsword" and lantern_status == False:
        print("""
        Swinging wildly at the dark isn't a very good idea, is it?
        You have no idea what you're cutting into, but eventually you manage to slam your blade into the hide of a tree\n
        Tugging on the blade reveals it is stuck
        """)
        del inventory[0]
        break
        forest7()
      elif move6 =="inventory":
        inventory()
      elif move6 == "help":
        help()
      elif move6 == "quit":
        sys.exit("Thanks for playing!")
      else:
        print("")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")
        

def forest4():
  while True:
    try:
      move5 = str(input(""))
      if move5 == "longsword":
        print("""
        The moment you brandish the blade hanging at your waist, the two eyes reflected before you disappear further back into the black
        """)
        break
        forest5()
      elif move5 =="inventory":
        inventory()
      elif move5 == "help":
        help()
      elif move5 == "quit":
        sys.exit("Thanks for playing!")
      else:
        print("")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

def forest3():
  while True:
    try:
      move4 = str(input(""))
      if move4.capitalize() == "S":
        print("""
        Apparently, you aren't strong enough to brave the depths of the forest
        The parents won't be very happy...
        """)
        break
      elif move4 =="inventory":
        inventory()
      elif move4 == "help":
        help()
      elif move4 == "quit":
        sys.exit("Thanks for playing!")
      else:
        print("")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

def forest2():
    while True:
        try:
            move3 = str(input(""))
            if move3.capitalize() == "W":
                print("""
                Strafing around your intial entry point yields nothing
                """)
                forest3()
                break
            elif move3 == "inventory":
                inventory()
            elif move3 == "help":
                help()
            elif move3 == "quit":
                sys.exit("Thanks for playing!")
            else:
              print("")
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
        elif move2 == "quit":
          sys.exit("Thanks for playing!")
        else:
          print("")
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
        You take your first step into the forest path
        Darkness encroaches upon you, and you hear the rustling of beasts in the bushes around you
        You can not see anything in the dark, but the rustling is getting closer
        """)
        forest1()
        break
      elif move1 == "inventory":
        inventory()
      elif move1 == "help":
        help()
      elif move1 == "lantern":
        print("""
        You unclip your lantern from your belt
        and brandish it at the darkness\n
        Despite the light, you can only see but a few meters in front of you
        where the northern path is enveloped by thorns and brambles\n
        In addition,
        the light is reflecting off the eyes of something watching you in those same thorns and brambles
        """)
        forest4()
        break
      elif move1 == "quit":
        sys.exit("Thanks for playing!")
      elif move1.capitalize() == "S" or "E" or "W":
        print("There is nothing for you that way")
      else:
        print("")
    except ValueError:
        print("")
    except KeyboardInterrupt:
        print("")

forest()

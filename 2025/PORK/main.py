import random

def help():
  

print("""
PORK: A Text-Based Adventure Game By Axion\n
Type "help" for a tutorial and a list of commands\n
A young boy was kidnapped by an evil wizard named Snort\n
You are a mercenary hired by his parents to recover him\n
He was dragged into the forest last night\n\n
You are standing to the south of the forest in a wide green clearing\n
There is a path ripped through the brush
""")

front_forest = str(input(""))

if front_forest.capitalize() == "N":
  print("""
  You take your first step into the forest path\n
  Darkness encroaches upon you, and you hear the rustling of beasts in the bushes around you\n
  You can not see anything in the dark, but the rustling is getting closer
  """)
else:
  print("There is nothing for you that way")

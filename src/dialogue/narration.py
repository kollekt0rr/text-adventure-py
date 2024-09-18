# Utilizing this to format text instead of clouding up other files. 
# Could probably replace with JSON file instead.

#imports for some reason
import random

#Menu Texts
menu_options = """Welcome adventurer! Please make a selection by typing one of the numbers below:  
1. New Game 
2. Load Game
3. Achievements
4. Rules & Hints
5. Embrace Cowardice (Quit) 
"""
menu_exception_handling_options = [
    "Sorry I could not understand your mumbling. Please attempt to communicate again.",
    "Hmm. Let's try that again.",
    "Now why would you go trying that?",
    "That's not quite one of the options I had in mind."
]

menu_exception_handling = random.choice(menu_exception_handling_options)

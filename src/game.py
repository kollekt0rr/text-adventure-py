#imports
import os, random, characters #some additional when new features are added

#initializing global variables
game_loop = True
initial_menu = True
play_game = False

#defining global functions 
def clear():
    os.system('cls')

#map generator
#to-do: import function to generate map and store in DS 

#main game loop 
while game_loop:
    
    while initial_menu:
        print("Welcome Adventurer! Please make a selection:")
        print("1. New Game \n2. Load Game \n3. Achievements \n4. Rules & Hints \n5. Give in to cowardice (Quit)")
        
        choice = input("> ")
        
        if choice == "1":
            clear()
            hero_name = input("Tell me hero, what do they call you?")
            initial_menu = False
            play_game = True
        elif choice == "2":
            pass #to-do: try-except with loading save file (TXT file?)
        elif choice == "3":
            pass #to-do: create and list achievements that provide unlocks
        elif choice == "4":
            pass #to-do: write rules and display key-binds
        elif choice == "5":
            quit_question = input("Have the cries of the innocent fallen upon deaf ears? \nYes  No").lower()
            
            if quit_question[0] == "y":
                quit()
            else:
                pass #return give either option of new game or load game 
        else:
            print("Sorry, I could not understand. Please try communicating again.")
            
    pass



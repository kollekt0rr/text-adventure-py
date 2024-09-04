#imports
import os, random, characters #some additional imports will be added when new features are developed
import dialogue.narration 

#initializing global variables
game_loop = True
initial_menu = True
playing_game = False

#defining global functions 
def clear():
    os.system('cls')

def format():
    print("\n======================================================================================================\n")

#map section
#to-do: import function to generate map and store in DS 

#main game loop 
while game_loop:
    
    while initial_menu:
        
        format()
        print(dialogue.narration.menu_options)
        format()
        
        choice = input("> ")
        
        if choice == "1":
            
            clear()
            format()
            hero_name = input("Tell me hero, what do they call you? \n> ")
            format()   
            initial_menu = False
            playing_game = True 
            
        elif choice == "2":
            
            pass #to-do: try-except with loading save file (TXT file?)
        
        elif choice == "3":
            
            pass #to-do: create and list achievements that provide unlocks
        
        elif choice == "4":
            
            pass #to-do: write rules and display key-binds
        
        elif choice == "5":
            
            format()
            quit_question = input("Have the cries of the innocent fallen upon deaf ears? \nYes  No\n>").lower()
            format()
            
            if quit_question[0] == "y":
                quit()
            
            else: #probably add some option to confirm that they are quitting otherwise return to menu
                
                pass
                
        else:
            
            format()
            print(dialogue.narration.menu_exception_handling)
            format()
            
    while playing_game:
        
        print(f"Welcome {hero_name}. You awaken in a damp, dark room. The dust fills your lungs and the cold bites at your flesh.")
        
    pass



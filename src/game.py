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
    print("\n======================================================================================================")

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
            if len(hero_name) < 1:
                print("Well no name, you will be a fun one.")
                hero_name = 'Nameless'
            else:
                continue
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
        
        format()
        print("HUD Elements") #to-do: exchange print statement with actual map location variable and other HUD elements.
        format()
        
        print(f"Welcome {hero_name}. You awaken in a damp, dark room.\nThe dust fills your lungs and the cold bites at your flesh.\nAs you rise, you feel stone beneath your palms and feet.")
        
        choice = input("What would you like to do? \n1. Actions\n2. Inventory\n3. Save\n4. Quit\n>  ")
        
        if choice == "1":
            print("1. Attack\n2. Inspect\n3. ")
        elif choice == "2":
            print("Inventory") #to-do: add inventory variable and display items in inventory along with dimensions (sizes and space left)
        elif choice == "3":
            pass #to-do: add save feature to write out to text file
        elif choice == "4":
            print("It is understandable the stresses of adventuring have proved too strong for such a weak heart.")
            quit()
        else:
            
              
    pass



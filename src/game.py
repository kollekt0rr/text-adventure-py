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
    print("======================================================================================================")

def save():
    save_file_items = [
        #add in variables like health or current room and inventory
    ]
    
    save_file = open("text_game_load.txt", "w")
    
    for item in save_file_items:
        save_file.write(item + "\n")
    save_file.close()
    
#map section
#to-do: import function to generate map and store in DS 

#main game loop 
while game_loop:
    
    while initial_menu:
        
        #save() whenever i finish adding the variables to save function
        
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
            format()
            action = input("1. Attack\n2. Inspect\n3. ...\n> ")
            format()
            if action == "1":
                pass
            elif action == "2":
                pass
            else:
                pass
        elif choice == "2":
            format()
            print("Inventory") #to-do: add inventory variable and display items in inventory along with dimensions (sizes and space left)
            format()
        elif choice == "3":
            pass #to-do: add save feature to write out to text file
        elif choice == "4":
            format()
            print(dialogue.narration.menu_exception_handling)
            format()
            quit()
        else:
            pass
        
        pass



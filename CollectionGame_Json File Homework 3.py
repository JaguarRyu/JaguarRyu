# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:09:37 2022

@author: stevo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Stevon mitchell
Course: 6050 Introduction to Computer Programming 
University: Wayne State University 
Assignment: Homework 3

"""


import json # json module for file writing

###################################
# Global Variables#################
###################################
test = False
 # empty list
players = [] 
 # can be set to anything greater than 1
num_items = 3
# only works with 2 players as is
num_players = 2 
# number of guesses each player gets
num_guesses = 3


###################################
# Function Declaration#############
###################################


###Writing to Json File###

def writeFile(location, name, data):
    
    if((location == "") or (name == "")): #Error checking 
        print("Need a filename and location")
        return False
    
    saveLocation = location + name #where the file will be printed out to
    
    # write to file as JSON
    myFile = open(saveLocation, 'w') #This allows us to write to the Json File
    with myFile as outputFile:
        json.dump(data, outputFile)

    return True


###Reading Json File###
def readFile(location, name):
    
    if((location == "") or (name == "")):
        # We have an error
        print("Need a filename and location")
        return False
    
    fileLocation = location + name
    
    myFile = open(fileLocation, 'r')
    with myFile as jsonFile:
        data = json.load(jsonFile)

    return data #Returns Json Data


###Create Users for Game###

def playerCreation(test, players, num_players, num_items):
    
    # Run loop to create each player (as defined by variable num_players).
    for playerProfile in range(num_players):       
    
        print("\n"*10)
        
        
        
        if num_players > 2:
            print("The game is now beginning.....\n")
            print("All other players please do not look at the screen...\n")                
            print("\n")*10
        
            
        else:
            if playerProfile == 0:
                player_eyes = 2 #Player eyes variable used to determine who 
                #is currently guessing 
            else:
                player_eyes = 1
        
            print("COVER YOUR EYES, PLAYER {}".format(player_eyes))
            
        
       
        
        players.append({   
     	"name": "",      
    		"score": 0,     
    		"collection": []  
     	})
        
        # Ask for name
        print("\n")
        new_name = input("Player {} Name: ".format(playerProfile + 1))
        
        # Check for "QUIT"
        if new_name.upper() == "QUIT":
            print("##########################")
            print("YOU Quit: GAME OVER!")
            print("##########################")
            return
        
        else:
            players[playerProfile]["name"] = new_name
        
        
        print("Enter {} items to put into your collection.".format(num_items))
        
        
        for collectionItem in range(num_items):
            collectionItem = collectionItem + 1 
            #Below is a code block for appending dictiornary
            collection_title = input("Item "+str(collectionItem)+" Name: ")
            collection_year = input("Item "+str(collectionItem)+" Year: ")
            collection_location = input("Item "+str(collectionItem)+" Location: ")
            collection_type = input("Item "+str(collectionItem)+" Type: ")
            
            # Check for QUIT
            if collection_title.upper() == "QUIT":
                print("GAME OVER: You Quit!!")
                           
                return
           
                
            # Add items as dictionary into list using append()
            players[playerProfile]["collection"].append({
                "title": collection_title, 
                "collection": collection_year, 
                "location": collection_location, 
                "type": collection_type})





        # TDB ADDED FOR HOMEWORK #3
        # WRITE TO FILE AS JSON
        location = "./"  # write to current directory where Python file is ran
        name = "Homework3jsonFile.json"
        # call function to write data
        writeFile(location, name, players)




        # For testing
        if test:    
            print(players[playerProfile]["collection"])
        
    return True

 
def askGuesses(test, players, num_players, num_items, num_guesses):
    
    for player in range(num_players):
               
        other_player = (player+1) % 2     
               
        currentPlayer = players[player]["name"]
        name_other = players[other_player]["name"]
        loops = num_guesses + 1 #This allows guesses to end at 3 instead of 2

        for i in range(1, loops):
            # Ask for guesses        
            player_guess = input("\n{}, you have {} guesses to guess 1 item from {}'s collection: ".format(currentPlayer, loops-1, name_other))

            if player_guess.upper() == "QUIT":
                print("\nYOU QUIT: GAME OVER")
                return
    
            location = "./"
            name = "Homework3jsonFile.json"
            fileDataJSON = readFile(location, name)
            
            # if you want to see the loaded information, change test to True
            if(test):
                print(fileDataJSON)
        
        
        
            #Have to use enumerate to help loop through dictionary 
            for key1, dictionary in enumerate(fileDataJSON[other_player]['collection']):
                # This is a dictionary, so I need to loop through
                for key2,val in dictionary.items():
                    if key2 == "title" and val.lower() == player_guess.lower():
                        flag = True
                        players[player]["score"] += 1
                        item = players[other_player]['collection'][key1]
                        break
                        
                    else:
                        flag = False
                
                if flag:
                    break

            # pause between reveal of guess
            
            if flag == True:
                print("\nYou are correct, {}. Way to go!\n\
                      You guessed it in {} trys.".format(currentPlayer, i))
                print("\n")
                print("Here is the complete record for that item:")
                
                for key2, val in item.items():
                    print("\t", key2.upper(), " : ", val)
                print("\n\n")
                break
            else:
                print("Sorry, {}. You are incorrect.".format(currentPlayer))

            # subtract 1 from loop count
            loops -= 1
            
    return True

# end the game         
def finish_game(test):
    for player in players:
        print("\n")
        print(player["name"] + " score: " + str(player["score"]))
        



###################################
#Main Program######################
###################################



print("Welcome Players...This is a guessing Game.\n\n")
print("Each player will create a list of items to be used in the game \n")    
print("Each list will contain {} types of data with 3 pieces of metadata\n".format(num_items))
print("Each player will then have {} guesses to guess an item from the other person's catalog.\n\n".format(num_guesses))

print("*************IMPORTANT*************")
print("FYI You can quit anytime by typing 'QUIT'!!!!!")
print("\n\n\n\n")
   
result = playerCreation(test, players, num_players, num_items) # run function

if result != None:
    print("\n"*10)
    print("!******************* TAKE A GUESS *******************!")
    print("\n"*10)

    result = askGuesses(test, players, num_players, num_items, num_guesses) # run function
else:
    print("\n\n")
    finish_game(test)
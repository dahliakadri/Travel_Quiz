# Project: Travel Quiz

# User is promted 3 questions about their work day
# Based on these questions the quiz will generate a far away location and activity the user should rather be doing

#Rules
    #Q1 - the more hours spent at work, the more remote the destination 
    #Q2 - based on a hot or cold drink response, the destination will be based in a cool or hot destination
    #Q3 - based on user physical activity level, the activity will be relaxing or strenuous 

#Script for the quiz starts here

def get_user_name ():
    user_name = input ("What's your name? ")
    user_name = user_name.title()
    print("")
    return user_name

def get_company_name (user_name):
    company_name = input ("Thanks {}, what is your company name? ".format(user_name))
    company_name = company_name.title()
    print("")
    print ("Ohh, hmmm... while working at {} sounds fascinating, I have a feeling you might be better suited for some vacation time.".format(company_name))
    print("")
    return company_name



def q1_answer() :
#receives user input on how many hours worked and returns value 0, 1 , 2 for hours
    
    while True:
        hours = input("How many hours have you worked today?")
    
        if hours.isdigit() and float(hours) < 2 :
            print("Ah, thanks for being honest. I see you are not really in work mode to begin with.")
            hours = 0
            break

        elif hours.isdigit() and float(hours) in range (2,5):
            print("Only {} hours in and already disctracted.".format(hours))
            hours = 1
            break
    
        elif hours.isdigit() and float(hours) > 4 :
            print("Woah, that's a lot! You really need this quiz.")
            hours = 2
            break
            
        else:
            print("Input Error. Please add a real number.")
    print ("Onto the next question.")
    return hours




def q2_answer():
#returns user input on hot or cold beverage
    while True:
        drink_temp = input ("Do you prefer a hot or cold beverage right now? ")
        drink_temp = drink_temp.lower()

        if drink_temp == "hot":
            print("A {} drink, I see... seems you might be up for a warm weather trip.".format(drink_temp))
            break
        
        elif drink_temp == "cold":
            print ("A {} drink, I see...seems you might be down for a cooler weather adventure.".format(drink_temp))
            break
        
        else: 
            print ("Input error. Try again and enter hot or cold.")

    print ("Onto our final question!")
    return drink_temp



def q3_answer():
#receives user input on activity level and returns value for activity level 0 or 1
    while True:
        user_activity = input("Have you worked out today?  ")
        user_activity = user_activity.lower()
       
        if user_activity == "yes":
            print ("Awesome! Seems you need a bit more of a relaxing trip. ")
            user_activity = 1
            break
        
        elif user_activity == "no":
            
            while True:
                user_activity = input("Uh oh. Do you plan to work out today? ")
                user_activity = user_activity.lower()

                if user_activity == "yes":
                    print("Great!")
                    user_activity = 1
                    break
                
                elif user_activity == "no":
                    print("I see... You are probably due for some physical activity. ")
                    user_activity = 0
                    break    

                else:
                    print("Invalid input. Answer yes or no. ")
            break
        
        else:
            print("Invalid input. Answer yes or no.")
    return user_activity



#data lists for destinations 
cold_cali_dest = ["San Francisco", "Medicino"]
hot_cali_dest = ["San Diego", "Los Angeles"]
cold_usa_dest = ["New York City" , "Chicago", "Killington"]
hot_usa_dest = ["Miami","Orlando"]
cold_world_dest = ["St. Petersburg", "Montreal"]
hot_world_dest = ["Barcelona", "St. Marteen"]

#data lists for activities
cold_activ_rec = ["skiing","snowboarding"]
hot_activ_rec = ["white water rafting", "scuba diving", "surfing", "mountain biking"]
cold_relax_rec = ["Hot Tub Time Machineing", "making snow angels"]
hot_relax_rec = ["tanning", "sand castle building", "flying a kite", "lazy river tubing"]

import random

def determine_location(user_responses):
#determines user location based on user responses  
    if user_responses[0] == 0:
        if user_responses[1] == "cold":
            dest_local = random.choice(cold_cali_dest)
        elif user_responses[1] == "hot":
            dest_local = random.choice(hot_cali_dest)

    elif user_responses[0] == 1:
        if user_responses[1] == "cold":
            dest_local = random.choice(cold_usa_dest)
        elif user_responses[1] == "hot":
            dest_local = random.choice(hot_usa_dest)

    elif user_responses[0] == 2:
        if user_responses[1] == "cold":
            dest_local = random.choice(cold_world_dest)
        elif user_responses[1] == "hot":
            dest_local = random.choice(hot_world_dest)
    
    return dest_local


def determine_activity(user_responses):
#determins user activity base on user responses
    if user_responses[2] == 1:
        if user_responses[1] == "cold":
            activity_name = random.choice(cold_relax_rec)
        elif user_responses[1] == "hot":
            activity_name = random.choice(hot_relax_rec)

    elif user_responses[2] == 0:
        if user_responses[1] == "cold":
            activity_name = random.choice(cold_activ_rec)
        elif user_responses[1] == "hot":
            activity_name = random.choice(hot_activ_rec)

    return activity_name


def play_quiz ():
    print ("Hello! Welcome to the travel quiz.")
    print("")
    user_name = get_user_name ()
    print("")
    company_name = get_company_name(user_name)
    print ("")
    print("Would you like to answer a few questions about your day to determine where and what you should really be doing? Input Yes or No.")

    while True:
    #loop to play the quiz
        
        answer_to_game = input (">")
        print("")
        
        answer_to_game = answer_to_game.title()
        
        if answer_to_game == "No":
            print("Okay, maybe next time. Good luck with work or whatever.")
            break
        
        elif answer_to_game == "Yes":
            print("Great! Let's begin!")
            print("")
            user_hours = q1_answer()
            print("")
            user_temp = q2_answer()
            print("")
            active_level = q3_answer()
            print("")
            user_responses = [user_hours, user_temp, active_level]
            user_activity = determine_activity(user_responses)
            user_location = determine_location(user_responses)
            print ("")
            print("Well, {}, based on your responses today, I see a trip that consists of leaving {} to do some {} in {} in your near future.".format(user_name, company_name, user_activity, user_location))
            print ("")
            
            while True:
                print ("")
                play_again = input("Would you like to play again? ")
                play_again = play_again.title()
                
                if play_again == "Yes":
                    print("Okay, but you should probably get back to work soon...")
                    print("")
                    print("On second thought, let's begin!")
                    print("")
                    user_hours = q1_answer()
                    print("")
                    user_temp = q2_answer()
                    print("")
                    active_level = q3_answer()
                    print("")
                    user_responses = [user_hours, user_temp, active_level]
                    user_activity = determine_activity(user_responses)
                    user_location = determine_location(user_responses)
                    print ("")
                    print("Okay {}, based on your latest responses, you definitely need to leave {} and go {} in {} in your near future.".format(user_name, company_name, user_activity, user_location))
                
                elif play_again == "No": 
                    break

                else:
                     print("Invalid answer. Input Yes or No")
        
        else:
            print("Invalid answer. Input Yes or No.")
      
play_quiz ()



#Next Edition:
#User can store their list in Box
#Multiplayer - based on the answers of both people, send them to a destination having them do a certain activity
#based on the actual location of the person using gps determine location of destination
#after game ends include hotel and real activities in the location that they can reserve/buy
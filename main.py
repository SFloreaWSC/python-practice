import random

FORMATTWO = "{}\nA){}\nB){}\n"
FORMATTHREE = "{}\nA){}\nB){}\nC){}\n"
FORMATFOUR = "{}\nA){}\nB){}\nC){}\nD){}\n"

replay = "yes"
while replay == "yes":
    #setting
    inst = 0
    points = 0
    re = 1
    #ask user's name
    print ("Hello.")
    name = input ("Please input your name")

    #greet user using name
    print (f"Nice to meet you, {name}.")
    while True:
        try:
            chance = input("How many chances would you like to answer questions? \nChoose a number from 1 to 3\n")
            chance = int(chance)
            if chance > 0 and chance <= 3:
                break
            if chance == 0 or chance > 3:
                print("Please enter a valid numerical value.")    
        except:
            print("Please enter a valid numerical value.")
    tries = chance
    print ("The questionnaire is ready for your participation.")
    #question 0
    while tries > 0:
        question = "When did you last do something bad?"
        a = "Very recently"
        b = "Recently"
        c = "Not recently"
        d = "Never"
        ans = input (FORMATFOUR.format(question, a, b, c ,d)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            tries = tries - 1
            while tries == 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        elif ans == "a" or ans == "very recently":
            points += 1
            break
        else: 
            print("duck")
            break
    tries = chance
    #question 1
    while tries > 0:
        question = "Do you think that you are a good person at heart?"
        a = "Yes"
        b = "No"
        c = "Who can say"
        ans = input (FORMATTHREE.format(question, a, b, c)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            tries = tries - 1
            while tries <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "who can say":
            points += 1
            break
        else:
            break
    tries = chance
    #question 2
    while tries > 0:
        question = "Would you steal 100,000 of untraceable cash from a man on his deathbed?"
        a = "Yes"
        b = "No"
        c = "Wouldn't you?"
        ans = input (FORMATTHREE.format(question, a, b, c)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            tries = tries - 1
            while tries <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "wouldn't you":
            points += 1
            break
        else:
            break
    tries = chance
    #question 3
    while tries > 0:
        question = "Do you feel like you are being watched?"
        a = "Yes"
        b = "No"
        c = "I am being watched"
        ans = input (FORMATTHREE.format(question, a, b, c)).lower()
        ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No \nC) I am being watched\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "i am being watched":
            points += 1
            break
        else:
            break
    tries = chance
    #question 4
    while tries > 0:
        question = "How often do you feel like life is meaningless?"
        a = "Frequently"
        b = "Occasionally"
        c = "Rarely"
        d = "Never"
        ans = input (FORMATFOUR.format(question, a, b, c ,d)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "b" or ans == "occasionally":
            points += 1
            break
        else:
            break
    tries = chance
    #question 5
    while tries > 0:
        question = "If you went missing, is there anyone who would miss you?"
        a = "There is"
        b = "There isn't"
        ans = input (FORMATTWO.format(question, a, b)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "a" or ans == "there isn't":
            points += 1
            break
        else:
            break
    tries = chance
    #question 6
    while tries > 0:
        question = "Do you regret the things you have done which you believe served the ‘greater good’?"
        a = "I do"
        b = "I don't"
        c = "I can't"
        d = "I won't"
        ans = input (FORMATFOUR.format(question, a, b, c ,d)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "i can't":
            points += 1
            break
        else:
            break
    tries = chance
    #question 7
    while tries > 0:
        question = "Do you regret the things you have done which did not serve the ‘greater good’?"
        a = "I do"
        b = "I don't"
        c = "I can't"
        d = "I won't"
        ans = input (FORMATFOUR.format(question, a, b, c ,d)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "d" or ans == "i won't":
            points += 1
            break
        else:
            break
    tries = chance
    #question 8
    while tries > 0:
        question = "Have you declared your participation in this questionnaire to anyone?"
        a = "I have"
        b = "I haven't"
        ans = input (FORMATTWO.format(question, a, b)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "b" or ans == "i haven't":
            points += 1
            break
        else: 
            break
    tries = chance
    #question 9
    while tries > 0:
        question = "Would anyone investigate if you suddenly were declared as missing?"
        a = "Yes"
        b = "No"
        ans = input (FORMATTWO.format(question, a, b)).lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "b" or ans == "no":
            points += 1
            break
        else:
            break
    #end of questionnaire
    if inst == 0:
        print("Thank you for answering all of our questions.")
    else:
        print("Thank you for, for the most part, answering all our questions.")
    #points
    if points <= 4:
        print("This data will be useful moving forward in out endeavors.")
        print(f"Goodbye, {name}.")
        re = 1
    if points > 4 and points <= 9:
        print("Nicely done, you have been placed on a waiting list.")
        print("If you are picked, we will contact you, do not try and contact us.")
        print(f"Thank you, {name}.")
        re = 1
    if points == 10:
        print("Well done, you are in the 99th percentile of participants.")
        print("Members of our corporation have been dispatched, please refrain from exiting the premises.")
        print(f"Thank you, {name}.")
        re = 0
        replay = "no"
    if points > 10:
        print("Please do not go anywhere, BAASA associates will be arriving soon.")
        print("Do not be alarmed. Do not leave. Do not resist.")
        re = 0
        replay = "no"
    
    while re == 1:
        replaie = input("If you would like to sumbit another questionnaire, please state so now. \n1) Yes\n2) No\n").lower()
        if replaie == "1" or replaie == "yes":
            replay = "yes"
            re = 0
        if replaie == "2" or replaie == "no":
            print("Goodbye.")
            replay = "no"
            re = 0

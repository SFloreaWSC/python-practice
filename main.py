import random
replay = "yes"
while replay == "yes":
    #setting
    inst = 0
    points = 0
    re = 1
    ques = 0
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
        ans = input ("When did you last do something bad? \nA) Very recently \nB) Recently\nC) Not recently\nD) Never\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        elif ans == "a" or ans == "very recently":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z" 
            break
    tries = chance
    #question 1
    while tries > 0:
        ans = input ("Do you think that you are a good person at heart? \nA) Yes \nB) No\nC) Who can say\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "who can say":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 2
    while tries > 0:
        ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            chance = chance - 1
            while chance <= 0:
                print("We do not have time for insolence.")
                print(f"Goodbye, {name}.")
                replay == "no"
                while True:
                    ques = "x"
        if ans == "c" or ans == "wouldn't you":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 3
    while tries > 0:
        ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No \nC) I am being watched\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No\nC) I am being watched\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No\nC) I am being watched\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "c" or ans == "i am being watched":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 4
    while tries > 0:
        ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "b" or ans == "occasionally":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 5
    while tries > 0:
        ans = input ("If you went missing, is there anyone who would miss you? \nA) There isn't \nB) There is\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("If you went missing, is there anyone who would miss you? \nA) Yes \nB) No\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("If you went missing, is there anyone who would miss you? \nA) Yes \nB) No\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "a" or ans == "there isn't":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 6
    while tries > 0:
        ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "c" or ans == "i can't":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 7
    while tries > 0:
        ans = input ("Do you regret the things you have done which did not serve the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "d" or ans == "i won't":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    tries = chance
    #question 8
    while tries > 0:
        ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "b" or ans == "i haven't":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z" 
            break
    tries = chance
    #question 9
    while tries > 0:
        ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n").lower()
        if ans == "" or ans == " ":
            inst = inst + 1
            print ("Please answer the question.")
            ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n").lower()
            if ans == "" or ans == " ":
                inst = inst + 1
                print ("Please answer the question.")
                ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n").lower()
                if ans == "" or ans == " ":
                    inst = inst + 1
        if ans == "b" or ans == "no":
            points = points + 1
            ans = "z"
            break
        else:
            ans = "z"
            break
    #end of questionnaire
    if inst == 0:
        print("Thank you for answering all of our questions.")
    elif inst == 1 or inst == 2:
        print("Thank you for, for the most part, answering all our questions.")
    #points
    if points < 4:
        print("This data will be useful moving forward in out endeavors,")
        print(f"Goodbye, {name}.")
        re = 1
    if points >= 4 and points <= 9:
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
        elif replaie == "2" or replaie == "no":
            print("Goodbye.")
            replay = "no"
            re = 0

#setting
inst = 0
temporary = 0
points = 0
QUESTION_FORMAT = "A){}"
#ask user's name
print ("Hello, you.")
name = input ("What is your name?")     

#greet user using name
print (f"Nice to meet you, {name}.")
print ("The questionnaire is ready for your participation.")

#question 0
ans = input ("When did you last do something bad? \nA) Very recently \nB) Recently\nC) Not recently\nD) Never\n".lower())
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("When did you last do something bad? \nA) Very recently \nB) Recently\nC) Not recently\nD) Never\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("When did you last do something bad? \nA) Very recently \nB) Recently\nC) Not recently\nD) Never\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Very recently" or ans == "very recently":
    points = points + 1
    ans = "z"
else:
    ans = "z"   

#question 1
ans = input ("Do you think that you are a good person at heart? \nA) Yes \nB) Who can say\nC) No\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Do you think that you are a good person at heart? \nA) Yes \nB) Who can say\nC) No\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Do you think that you are a good person at heart? \nA) Yes \nB) Who can say\nC) No\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "B" or ans == "b" or ans == "Who can say" or ans == "who can say":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 2
ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "C" or ans == "c" or ans == "Wouldn't you" or ans == "wouldn't you":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 3
ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No \nC) I am being watched\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No\nC) I am being watched\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Do you feel like you are being watched? \nA) Yes \nB) No\nC) I am being watched\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "C" or ans == "c" or ans == "I am being watched" or ans == "i am being watched":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 4
ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("How often do you feel like life is meaningless? \nA) Frequently \nB) Occasionally \nC) Rarely \nD) Never\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "B" or ans == "b" or ans == "Occasionally" or ans == "occasionally":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 5
ans = input ("If you went missing, is there anyone who would miss you? \nA) Yes \nB) No\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("If you went missing, is there anyone who would miss you? \nA) Yes \nB) No\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("If you went missing, is there anyone who would miss you? \nA) Yes \nB) No\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "B" or ans == "b" or ans == "No" or ans == "no":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 6
ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "C" or ans == "c" or ans == "I can't" or ans == "i can't":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 7
ans = input ("Do you regret the things you have done which did not serve the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Do you regret the things you have done which you believe served the ‘greater good’? \nA) I do\nB) I don't\nC) I can't\nD) I won't\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "D" or ans == "d" or ans == "I won't" or ans == "i won't":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 8
ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Have you declared your participation in this questionnaire to anyone? \nA) I have\nB) I haven't\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "B" or ans == "b" or ans == "I haven't" or ans == "i haven't":
    points = points + 1
    ans = "z"
else:
    ans = "z"

#question 9
ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("Please answer the question.")
    ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("Please answer the question.")
        ans = input ("Would anyone investigate if you suddenly were declared as missing? \nA) Yes\nB) No\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "B" or ans == "b" or ans == "No" or ans == "no":
    points = points + 1
    ans = "z"
else:
    ans = "z"

if inst > 2:
    print("We do not have time for insolence.")
    print(f"Goodbye, {name}.")
#END OF QUOESAIRIAIREEREE
if inst == 0:
    print("Thank you for answering all of our questions.")
    print(points)
elif inst == 1 or inst == 2:
    print("Thank you for, mostly, answering all the questions.")
#override

#points
    print("a")
if points >= 4 and points <= 9:
    print("b")
if points == 10:
    print("c")
if points > 10:
    print("???")


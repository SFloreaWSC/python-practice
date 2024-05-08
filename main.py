#var setting
inst = 0
temporary = 0
points = 0
#ask user's name
print ("Hello, you.")
name = input ("What is your name?")     

#greet user using name
print (f"Nice to meet you, {name}.")
print ("I have the questionnaire ready for you.")

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

if ans == "A".lower() or ans == "Very recently".lower():
    points = points + 1
    print(f"{points}")
    
#question 1
ans = input ("Do you think that you are a good person at heart? \nA) Yes \nB) Who can say\nC) No\n")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1

#question 2
ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
if ans == "" or ans == " ":
    inst = inst + 1
    ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        ans = input ("Would you steal 100,000 of untraceable cash from a man on his deathbed? \nA)Yes \nB)No \nC)Wouldn't you\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "C" or ans == "c" or ans == "Wouldn't you" or ans == "wouldn't you":
    points = points + 1

#question 3
ans = input ("")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1

#question 4
ans = input ("")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1

#question 5
ans = input ("")
ans = input ("")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1

#question 6
ans = input ("")
ans = input ("")
if ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1

#question 7
ans = input ("")
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1
elif ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
else:
    points = points 

#question 8
ans = input ("")
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1
elif ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
else:
    points = points 

#question 9
ans = input ("")
if ans == "A" or ans == "a" or ans == "Yes" or ans == "yes":
    points = points + 1
elif ans == "" or ans == " ":
    inst = inst + 1
    print ("INSERT \nA) X \nB) X\n")
    ans = input ("INSERT \nA) X \nB) X\n")
    if ans == "" or ans == " ":
        inst = inst + 1
        print ("INSERT")
        ans = input ("INSERT \nA) X \nB) X\n")
        if ans == "" or ans == " ":
            inst = inst + 1
else:
    points = points 

#INSERT CODE LAST QUESTION
if temporary == 3:
    print (f"Thank you for this valuble data, {name}.")
    print ("Goodbye.")

#add up score
#say goodbye (use user name)


#refuse to answer override
if inst == 2:
    print ("We do not have time for insolence.")
    print ("Goodbye.")
#var setting
inst = 0
temporary = 0
points = 0
#ask user's name
print ("Hello, you.")
name = input ("What is your name?") 

#greet user using name
print (f"Nice to meet you, {name}")
print ("I have a question for you.")

#ask if they feel like they are being watched
a0 = input ("Do you feel like you are being watched? A) Yes B) No")
if a0 == "A" or "a" or "Yes" or "yes":
    points = points + 1
elif a0 == " " or a0 == "":
    inst = inst + 1
    print ("Please answer the question.")
    a0 = input ("Do you feel like you are being watched? A) Yes B) No")
else:
    points = points 
    
#question 1
a1 = input ("temp")
if a1 == "temp":
    print("temp success")

#INSERT CODE LAST QUESTION
if temporary == 3:
    print (f"Thank you for this valuble data, {name}.")
    print ("Goodbye.")

#add up score
#say goodbye (use user name)


#refuse to answer override
if inst == 3:
    print ("We do not have time for insolence.")
    print ("Goodbye.")
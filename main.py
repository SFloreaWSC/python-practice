#var setting
inst = 0
temporary = 0

#ask user's name
print ("Hello, you.")
name = input ("What is your name?") 

#greet user using name
print (f"Nice to meet you, {name}")
print ("I have a question for you.")

#ask if they feel like they are being watched
a1 = input ("Do you feel like you are being watched? A) Yes B) No")
if a1 == "A" or a1 == "a":
    print ("Congratulations, That was correct!")
else:
    print ("I'm sorry, the correct answer was: Yes.")

#INSERT CODE LAST QUESTION
if temporary == 3:
    print (f"Thank you for this valuble data, {name}.")
    print ("Goodbye.")

#add up score
#say goodbye (use user name)


#refuse to answer override
if a1 == "" or a1 == " ":
    inst = inst + 1
    print ("Please answer the question.")
    a1 = "dhaifjhvnkdfghnmvkdiuhfbnmgkfreifgubhfenjdifvobifjdebdfjiofdeidhfbgjfdiefjbnfdjij"
    a1 = input ("Do you feel like you are being watched? A) Yes B) No")
if a1 == "" or a1 == " " and inst == 1:
    print ("We do not have time for insolence.")
    print ("Goodbye.")
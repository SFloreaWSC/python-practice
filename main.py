#ask user's name
print ("Hello, you")
name = input ("What is your name?") 

#greet user using name
print (f"Nice to meet you, {name}")
print ("I have a question for you.")

#ask if they feel like they are being watched
answer1 = input ("Do you feel like you are being watched? A) Yes. B) No.")

#tell correct answer
if answer1 == "A" or answer1 == "a":
    print ("Congratulations, That was correct!")
else:
    print ("I'm sorry, the correct answer was: Yes.")

#say goodbye (use user name)
print (f"Thank you for this valuble data, {name}.")
print ("Goodbye.")
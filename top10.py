HIGHEST_IMDB_ANSWER = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Shindler's List", "The Lord of the Rings: The Return of the King", "12 Angry Men", "The Godfather Part 2", "Pulp Fiction", "The Lord of the Rings: The Fellowship of the Ring", "12th Fail"]
guess = []
#---------------- FUNCTIONS ----------------

def intro():
    #ask user's name
    print ("Hello.")
    name = input ("Please input your name\n")
    #greet user using name
    print (f"Nice to meet you, {name}.")
#---------------------------------------------------
def getChance():
    while True:
        try:
            chance = input("How many chances would you like to answer questions? \nChoose a number from 1 to 3\n")
            chance = int(chance)
            if chance > 0 and chance <= 3:
                return chance  
            else:
                print("Please enter a valid numerical value.")
        except:
            print("Please enter a valid numerical value.")
#---------------------------------------------------
def inList(answer, list):
    if answer in list:
        return True
    else:
        return False
#---------------------------------------------------


#---------------- MAIN CODE ----------------
intro()
chance = getChance()
score = 0
while chance > 0:
    answer = input("Name one of the top 10 highest rated movies on IMDB:\n").lower()
    if inList(answer, HIGHEST_IMDB_ANSWER) == True:
        if inList(answer, guess) == True:
            print("You already guessed that one?")
        else:
            score +=1
            print("That's correct!")
            list.append(answer)
    else:
        chance -= 1
        print("Sorry, that's incorrect!")

print(f"That's all! Your final score was... {score}!")
# step 1. get a set of questions (hashmap/dictionary for Questions and Answers)
# step 2. set up scores
# step 3. get answer wrong 3 times, game is over
import sys
from time import sleep
import random
import copy
from threading import Timer
import msvcrt
import time
from threading import Thread


class TimeOutError(Exception): pass

def timed_question(question, time=3):
    def time_up():
        print("\nTime's up! ... press enter to continue")

    temp = True
    timer = Timer(time, time_up)
    timer.start()
    answer = input(question)
    if temp:
        timer.cancel()
        return answer
    else:
        raise TimeOutError

# $200 questions
lvlOneQuestions = {
    "This man has no real last name and is the creator of one of the most well-known artworks of all time...": "who is Leonardo da Vinci",
    "How many legs do those critters that live under the sea and even have a restaurant named after them, have?": "what is 10",
    "You wouldn't think these animals would want kids (plural answer)...": "what are Goats",
    "Elephant tusks are made of this material.. would also make for a good name for a child..": "what is ivory"
    "Three of these animals survived the Titanic sinking and was also the first of its kind to go into space...": "what is a Dog"
} 

# $400 questions
lvlTwoQuestions = {
    "Three of these animals survived the Titanic sinking and was also the first of its kind to go into space...": "what is a Dog",
    "I'm sure Alexander Graham Bell, the creator of this technology didn't think his invention would be advanced so much that even 3-year olds can use one!": "what is a Telephone",
    "In 1979, this activist became the first woman to be featured on US currency": "who is Susan B. Anthony",
    "This country gained its independence from Mexico in the 19th century": "who is Spain",
    "The words 'the', 'an', and 'a' are known as what in English grammar?": "what are Articles"
}

# $600 questions
lvlThreeQuestions = {
    "This country is both an island and a continent and the folks here have similar accents to their neighbors": "what is Australia",
    "Being the closest to the sun, I'm sure THIS planet doesn't get all four seasons": "what is Mercury",
    "The modern-day city of Istanbul was known by THIS name in the 13th century": "what is Constantinople",
    "How many countries are in North America?": "23",
    "Who did NOT sign the U.S. Constitution?": "who is John Hancock"
}

# $800 questions
lvlFourQuestions = {
    "THIS fort is where one of the deadliest American wars began": "what is Fort Sumpter",
    "THIS man became the U.S president after ol' Abe was assassinated": "who is Andrew Johnson",
    "THIS city has the best of both worlds as it lies in two different continents at the same time": "what is Istanbul",
    "Monet is known as the father of this art movement": "what is Impressionism",
    "1789 represents the start of which revolution?": "what is the French Revolution"
}

"""
questions = {
    "How many fingers does the average person have?": "10",
    "Who was the main character in the Nickelodeon show 'Victorious'?": "Tori Vega",
    "Who is my favorite artist?": "Drake",
    "What is 2+2?": "4",
    "What is my bestfriends name?": "Sydni Newsome"
}
"""
categories = [
                ["$200", "$400", "$600", "$800"], #category 1 
                ["$200", "$400", "$600", "$800"], #category 2
                ["$200", "$400", "$600", "$800"], #category 3
                ["$200", "$400", "$600", "$800"], #category 4
                ["$200", "$400", "$600", "$800"]  #category 5
            ]

score = 0
incorrect = 0
inGame = False;


def play():
    print ("\n")
    print ("Welcome to Jeopardy! Created by Kajoyrie Purcell\n")
    print ("                    Let's get started with a new game!\n")
    inGame = True;
    global score
    global incorrect
    while (inGame):

        print()
        board()

        if questions:

            choice = input("Choose a category (number 1-5): ")
            bet = input("For how much? (no dollar sign): ")


            print("\n--------You chose Category " + choice + " for " + "$" + bet + "--------")
            updateBoard(choice, bet)
            print("\n")
            print("Your question... is....")
            sleep(2)
            print()
            
            answer, question, tempDict = timeToAnswer(bet)

            if (answer == "" or answer != questions.get(question)):
                print("Wrong! The correct answer was: " + questions.get(question))
                if (incorrect == 2):
 
                    print("That wrong answer just cost you the game! Better luck next time.")
                    print("Your final score was: $" + str(score))
                    sys.exit(0)
                else:
                    incorrect = incorrect + 1
                    print("You now have " + str(incorrect) + " questions wrong. If you get 3, the game is over!")
            else:
                score += int(bet)
                print("Correct! You now have $" + str(score))

            removeQuestion(question) # removing question from dictionary so it's not chosen again
            print()

        else:

            print("You've answered all the questions, congrats!")
            print("Your final score was: $" + str(score))
            sys.exit(0)



def timeToAnswer(bet):
    answer = ""

    timeout = 5

    
    # picking a random question from the list of questions
    if bet == "200":
        chosen = random.choice(list(lvlOneQuestions))
        tempDict = copy.deepcopy(lvlOneQuestions)
    elif bet == "400":
        chosen = random.choice(list(lvlTwoQuestions))
        tempDict = copy.deepcopy(lvlTwoQuestions)
    elif bet == "600":
        chosen = random.choice(list(lvlThreeQuestions))
        tempDict = copy.deepcopy(lvlThreeQuestions)
    elif bet == "800":
        chosen = random.choice(list(lvlFourQuestions))
        tempDict = copy.deepcopy(lvlFourQuestions)
 
    # user has around 5 seconds to type something in
    try:
        answer = timed_question(chosen + ": ", timeout)
    except TimeOutError:
        pass
    return answer, chosen, tempDict

def removeQuestion(question):
    del questions[question]

def updateBoard(category, bet):
    if bet == "200":
        secondParam = 0
    elif bet == "400":
        secondParam = 1
    elif bet == "600":
        secondParam = 2
    elif bet == "800":
        secondParam = 3
    
    category = int(category)
    if categories[category - 1][secondParam] == "----":
        print("You already chose that!")
    else:
        categories[category - 1][secondParam] = "----"

def board():   
    print("--------------------------------------------------------------------------------") 
    print("  |  Category 1   |  Category 2  |  Category 3  |  Category 4  | Category 5  |")
    print("  |     " + categories[0][0] + "      |     " + categories[1][0] + "     |     " + categories[2][0]  + "     |     " + categories[3][0] + "     |    " 
            + categories[4][0] + "     |")
    print("  |     " + categories[0][1] + "      |     " + categories[1][1] + "     |     " + categories[2][1]  + "     |     " + categories[3][1] + "     |    " 
            + categories[4][1] + "     |")
    print("  |     " + categories[0][2] + "      |     " + categories[1][2] + "     |     " + categories[2][2]  + "     |     " + categories[3][2] + "     |    " 
            + categories[4][2] + "     |")
    print("  |     " + categories[0][3] + "      |     " + categories[1][3] + "     |     " + categories[2][3]  + "     |     " + categories[3][3] + "     |    " 
            + categories[4][3] + "     |")
    print("\n\n")

play()
# this function prints out the menu ant the menu options
def show_menu():
    print("1. Ask questions")
    print("2. Add question")
    print("3. Exit game")

# we add the option variable for the user to choose and return it
    option = input("Enter option: ")
    return option

# add ask_questions function


def ask_questions():
    questions = []      # add a list for the questions
    answers = []        # add a list for the answers

    with open("questions.txt", "r") as file:        # open the file with the "with block"
        lines = file.read().splitlines()

    # the enumeate creates a tuple in memory with a line at the beginning (the number is "i") and then the text.
    for i, text in enumerate(lines):
        if i % 2 == 0:
            # if i is even The first line in questions.txt is number 0 = even
            questions.append(text)
        else:
            # if i is odd The second line in questions.txt is number 1 = odd and so on!
            answers.append(text)

    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0       # initialize the score to start at zero

    for question, answer in questions_and_answers:        # zip() adds them togther
        guess = input(question + "> ")
        if guess == answer:
            score += 1          # adds the score to the variable score
            print("Correct!")
            print(score)
        else:
            print("Wrong!")

    print("You got {0} correct out of {1}".format(score, number_of_questions))


def add_question():     # add a function for option 2 Add a question.
    print("")
    question = input("Enter your question\n> ")    # > writes the :

    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))

    # add the question to the question.txt file for appending by using the "a"
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()        # the close function adds the question and answer to the file!
    # now we have to call the funtion to get it to work form inside the game_loop()

# test with print(show_menu())

# create the actual game loop


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()     # call the funtion ask_question
        elif option == "2":
            add_question()      # call the function add_question
        elif option == "3":
            break
        else:
            print("Invalid option!")
        print("")  # prints a blank line


game_loop()

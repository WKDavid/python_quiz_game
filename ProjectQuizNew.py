data = {
     'easy': {
         'text': '''\nGenerally, every ___1___  has to be within single
or double quotes. A ___1___ can be assigned to a ___2___. It is
a convention not to use capital letters in ___2___ naming.
A ___1___ can not be added to an ___3___, but they can be multiplied.
However, it is possible to add one ___1___ to another
in order to ___4___ them.\n''',
         'answers': ['string', 'variable', 'integer', 'concatenate'],
         'mistakes': 4
    },
    'medium': {
          'text': """\nA ___1___ is created with the def keyword.
You specify the inputs a ___1___ takes by adding ___2___ separated
by commas between the parentheses. ___1___s by default return
___3___ if you don't specify the value to return. ___2___ can be
standard data types such as string, number, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda
functions.\n""",
          'answers': ['function', 'arguments', 'none', 'list'],
          'mistakes': 3
    },
    'hard': {
          'text': '''\nA  ___1___ is a single file of python code that
can be implemented by using the ___2___ command. A ___3___ is a
collection of python ___1___s under a common namespace. In practice
one is created by placing multiple python ___1___s in a directory with
a special, ___4___ file. ___5___ is another python file, which usually
tells you that the ___1___ or the ___3___ you are about to install
has been ___3___d and distributed with Distutils, which is the standard
for distributing Python ___1___s. This allows you to easily install
Python ___3___s. Often it's enough to write: ___6___ command.\n''',
          'answers': ['module', 'import', 'package', '__init__.py', 'setup.py','python setup'],
          'mistakes': 2
    }
}


name = raw_input("\nHello, please state your name: ")
incorrect = '\nYour answer is not correct ' + name + '. Number of attempts left: '


def greeting():
    """
    Behavior: This function starts the program and greets a player using the global
    variable 'name'. Global variables have been assigned in order to avoid
    repetition of long lines. The function then guides user to the next step
    of a difficulty selection.
    """
    global name
    welcome = '\nWelcome to the python quiz game, ' + name + '!'*3
    print welcome
    return play_game(choose_difficulty())


def choose_difficulty():
    """
    Behaviour: The function asks user to choose a difficulty and returns it.
    Small dictionary used in order to make the difficulty selection easier
    and faster. The function alerts user in case of invalid selection and
    asks to choose again until a valid answer has been given.
    """
    choice = '\nPlease choose suitable difficulty: '
    choice += 'E for easy, M for medium and H for hard\n'
    choose = raw_input(choice).lower()
    difficulties = {"e": 'easy', "m": 'medium', "h": "hard"}
    while choose not in difficulties:
        print "Invalid entry, please try again."
        choose = raw_input(choice).lower()
    print name + ', you chose ' + difficulties[choose] + " difficulty!"
    return difficulties[choose]


def play_game(difficulty):
    """
    Behaviour: This is the main function of the game. It takes difficulty as
    an input. Based on an input it prints out the current text and asks to
    fill in the current blank of the text. The function keeps track of attempts
    and notifies user. Furthermore, it shares information about current
    progress with the following function 'attempts_check'.
    """
    text = data[difficulty]['text']
    attempts = data[difficulty]['mistakes']
    hits = 0
    while hits < len(data[difficulty]['answers']) and attempts > 0:
        print text
        answer = raw_input('Fill in the ___' + str(hits + 1) + '___\n').lower()
        if answer == data[difficulty]['answers'][hits]:
            print "Correct!"
            text = text.replace('___' + str(hits + 1) + '___', data[difficulty]['answers'][hits])
            hits += 1
            attempts_check(difficulty, attempts, text, hits)
        else:
            attempts -= 1
            print incorrect + str(attempts)
            attempts_check(difficulty, attempts, text, hits)


def attempts_check(difficulty, attempts, text, hits):
    """
    Behaviour: Using the current information from the main 'play_game' function
    as an input, this fuction ckecks, if the game should be ended and navigates
    user accordingly to the last function 'game_over', if necessary.
    """
    if attempts <= 0:
        print "\nThank you for playing, " + name + " too many mistakes.\n"
        game_over()
    elif hits == len(data[difficulty]['answers']):
        print text
        print '\nCongratulations on completing the test ' + name + ' !!!\n'
        game_over()
    else:
        return None


def game_over():
    """
    Behaviour: This function prompts user to start the game over. It calls
    the greeting function in case of positive asnwer and restarts the game.
    Negative answer leaves the game. Invalid entry starts the function over.
    """
    again_answ = raw_input('Would you like to start over ' + name + '? y/n: ' ).lower()
    if again_answ == 'y':
         greeting()
    elif again_answ == 'n':
         print '\nHave a wonderful time of the day!'
         exit()
    else:
         print '\nInvalid answer\n'
         game_over()


greeting()

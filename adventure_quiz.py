# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

'''

prompt user for difficutly
    difficulty x
    return difficultyLevel
    scene = scene x

numberOfGuesses=difficultyLevel

difficulty x scene=' ' #You wake up...
difficulty y scene=' ' #You wake up...
difficulty y scene=' ' #You wake up...

'''

class color: #color class from Boubakr @ stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
   DARKCYAN = '\033[36m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

replacement_items=['_1_', '_2_', '_3_', '_4_', '_5_']
death1='murders you to death... super hard'

#sets difficulty
def set_diff(user_input):
    user_input = raw_input('''Welcome adventurer, a great quest lies ahead!
Please choose a difficulty by typing easy, medium or hard below:
''')
    if user_input == 'easy':
        return color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.

To your left you find a rusty hunting knife and to your right, a pack of shepard lemons.

You're thankful to discover that you're fully clothed in Jeans and a warm sweater.

A ''' + color.BOLD + 'wild Bear appears! '+ color.END + color.DARKCYAN + 'You throw the' + color.RED + ' _1_ ' + color.DARKCYAN + 'at the bear and he...' + color.END
    if user_input == 'medium':
        return 'medium string _1_ _2_ medium yo'
    if user_input == 'hard':
        return 'hard string _1_ _2_ hard whaaaat'
    else:
        return 'wrong input'

# checks if an item in replacement_items is a substring of the scene passed in.
def item_in_scene(scene, replacement_items):
    for pos in replacement_items:
        if pos in scene:
            return pos
    return None

def check_answer1(answer):
    if answer == ('lemons'):
        return True
    else:
        return False

def turn(count):
    while count < 5:
        return True
    else:
        return False


def run_adventure1(count, replacement_items):
    while count > 0:
        scene_string=set_diff(raw_input)
        print ['You have'] + [count] + ['chances remaining']
        print scene_string
        replaced = []
        scene_string = scene_string.split()
        for i in scene_string:
            replacement = item_in_scene(i, replacement_items)
            if replacement != None:
                user_input = raw_input("Fill in the blank for " + replacement + ''':
    ''')
                i = i.replace(replacement, user_input)
                replaced.append(i)
            else:
                replaced.append(i)
        replaced = " ".join(replaced)
        #check answer
        if check_answer1(user_input) == False:
            #return replaced + color.RED + 'murders you to death for insulting his honor!, try again.' + color.END
            count = count - 1
            if count > 0:
                print replaced + color.RED + 'Murders you to death... Like so hard...' + color.GREEN + '''

You have failed to survive! Please select your difficulty and try again
''' + color.END
            #print run_adventure1(set_diff('easy'), count-1, replacement_items)
            #print run_adventure1(set_diff('easy'), count, replacement_items)
            #break
            #scene_string = set_diff(raw_input)
            else:
                break
        else:
            print replaced + color.GREEN + 'accepts your offering, wandering away, allowing you to live. Good job!!' + color.END
            print 'run_adventure2()'
    print color.RED + 'You have run out of chances! You die alone. Probably cold... Sucks I bet...'









#print scene
#dventure1(set_diff(raw_input), 5, replacement_items)
run_adventure1(3, replacement_items)
'''
if guessNumber > numberOfGuesses:





replacement function with raw_input
    if incorrect answer
        guesses = guesses - 1
    else
        append scene w user input


'''

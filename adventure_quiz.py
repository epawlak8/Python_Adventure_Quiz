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
replacement_items=['_1_', '_2_', '_3_']
blah_string='blahblahblah blah blah blah _1_ blag gggggg blah blah blah _2_ blah blah blahblah blah blah _3_ right?'
easy_scene='easy string _1_ _2_'
medium_scene='medium string _1_ _2_'
hard_scene='hard string _1_ _2_'


#sets difficulty
def set_diff(user_input):
    user_input = raw_input('''Welcome adventurer, a great quest lies ahead!
Please choose a difficulty by typing easy, medium or hard below:
''')
    if user_input == 'easy':
        return 'easy string _1_ _2_ so easy'
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

def run_adventure(scene_string, replacement_items):
    print scene_string
    replaced = []
    scene_string = scene_string.split()
    for i in scene_string:
        replacement = item_in_scene(i, replacement_items)
        if replacement != None:
            user_input = raw_input("Fill in the blank for " + replacement)
            i = i.replace(replacement, user_input)
            replaced.append(i)
        else:
            replaced.append(i)
    replaced = " ".join(replaced)
    return replaced


#print scene
print run_adventure(set_diff(raw_input),replacement_items)

'''
if guessNumber > numberOfGuesses:





replacement function with raw_input
    if incorrect answer
        guesses = guesses - 1
    else
        append scene w user input


'''

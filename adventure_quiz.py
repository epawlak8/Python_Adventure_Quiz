# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!


#psudocode



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

# Checks if an item in replacement_items is a substring of the scene passed in.
def item_in_scene(scene, replacement_items):
    for pos in replacement_items:
        if pos in scene:
            return pos
    return None

def run_adventure(scene_string, replacement_items):
    replaced = []
    scene_string = scene_string.split()
    for scene in scene_string:
        replacement = item_in_scene(scene, replacement_items)
        if replacement != None:
            user_input = raw_input("Fill in the blank for " + replacement)
            scene = scene.replace(replacement, user_input)
            replaced.append(scene)
        else:
            replaced.append(scene)
    replaced = " ".join(replaced)
    return replaced

print blah_string
print run_adventure(blah_string, replacement_items)

'''
if guessNumber > numberOfGuesses:





replacement function with raw_input
    if incorrect answer
        guesses = guesses - 1
    else
        append scene w user input


'''

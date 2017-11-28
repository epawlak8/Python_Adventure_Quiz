class color: #color class from Boubakr @ stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
   DARKCYAN = '\033[36m'
   YELLOW = '\033[93m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

replacement_items=['_1_', '_2_', '_3_', '_4_', '_5_']

#story strings to keep code below cleaner
die=color.RED + '''
You have chosen poorly and you die so hard.

''' + color.GREEN + '''
You have failed to survive! PLease Try again:
''' + color.END
welcome = 'Welcome adventurer, a great quest lies ahead!'
fill=color.GREEN + "Fill in the blank for "
l=''':
 ''' + color.END
accept='''
You have chosen well and you will live for now!
''' + color.END

out=color.RED + '''

You have run out of chances!

You die alone. Probably cold... Sucks I bet...''' + color.END
lvlup=color.GREEN + '''

***YOU MADE IT TO THE NEXT LEVEL, HELL YEAH BUDDY***

''' + color.END

#prompts user input and sets difficulty
def difficulty(user_input):
    user_input = raw_input('''Please choose a difficulty by typing easy, medium or hard below:
''')

    if user_input == 'easy':
        return 1
    if user_input == 'medium':
        return 2
    if user_input == 'hard':
        return 3

#select scene based on level and difficulty
def s_s(level, diff):
    if level == 1:
        return diff_scene1(diff)
    if level == 2:
        return diff_scene2(diff)
    if level == 3:
        return diff_scene3(diff)

#supplies scene for level 1 based on difficulty
def diff_scene1(diff):
    if diff == 1:
        return color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'rock' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + 'laptop, textbook, an angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'water bottle' + color.DARKCYAN + '''.
You're thankful to discover that you're fully clothed in Jeans, a warm sweater, running shoes and light gloves.

Nightfall is coming, choose which 4 items you'll keep in the backpack to survive
(note: use 1 word lowercase answers, ie. Rusty Hunting Knife = knife)

Your ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' will now hold:
''' + color.RED + '_1_ _2_ _3_ _4_' + color.END
    if diff == 2:
        return color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'rock' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + 'laptop, textbook, an angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'water bottle' + color.DARKCYAN + '''.
You're bummed out when you discover that you're only partially clothed in Jeans, a light shirt, but you have no shoes or gloves.

Nightfall is coming, choose which 4 items you'll keep in the backpack to survive
(note: use 1 word lowercase answers, ie. Rusty Hunting Knife = knife)

Your ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' will now hold:
''' + color.RED + '_1_ _2_ _3_ _4_' + color.END
    if diff == 3:
        return 'hard string _1_ _2_ hard whaaaat'
    else:
        return 'wrong input'

#supplies scene for level 2 based on difficulty
def diff_scene2(user_input):
    user_input = raw_input('''You've made it to level 2!
Please choose a difficulty by typing easy, medium or hard below:
''')
    if user_input == 'easy':
        return color.DARKCYAN + 'A' + color.BOLD + 'wild Bear appears! '+ color.END + color.DARKCYAN + 'You throw the' + color.RED + ' _1_ _2_ _3_ _4_ ' + color.DARKCYAN + 'at the bear and he...' + color.END
    if user_input == 'medium':
        return 'medium string _1_ _2_ medium yo'
    if user_input == 'hard':
        return 'hard string _1_ _2_ hard whaaaat'
    else:
        return 'wrong input'

#supplies scene for level 3 based on difficulty
def diff_scene3(user_input):
    user_input = raw_input('''You've made it to level 3!
Please choose a difficulty by typing easy, medium or hard below:
''')
    if user_input == 'easy':
        return color.DARKCYAN + 'level 3 _1_ _2_ _3_ _4_'
    if user_input == 'medium':
        return 'medium string _1_ _2_ medium yo'
    if user_input == 'hard':
        return 'hard string _1_ _2_ hard whaaaat'
    else:
        return 'wrong input'

#returns number of chances left
def chances(count):
    return color.RED + 'You have ' + str(count) + ' chances remaining' + color.END

# checks if an item in replacement_items is a substring of the scene passed in.
def item_in_scene(scene, replacement_items):
    for pos in replacement_items:
        if pos in scene:
            return pos
    return None

#checks answer based on level and difficulty
def check(level, answer, diff):
    if level == 1 and diff == 1:
        if answer == ('knife') or answer == ('textbook') or answer == ('lemons') or answer == ('bottle'):
            return True
        else:
            return False
    if level == 2:
        if answer == ('a') or answer == ('b') or answer == ('c') or answer == ('d'):
            return True
        else:
            return False
    if level == 3:
        if answer == ('a') or answer == ('b') or answer == ('c') or answer == ('d'):
            return True
        else:
            return False

#brings together all the functions
def run_adventure(level, count):
    if level < 2:
        print welcome
        #diff = difficulty(raw_input)
    while count > 0:
        diff = difficulty(raw_input)
        scene_string = s_s(level, diff)
        print chances(count)
        print scene_string
        replaced = []
        scene_string = scene_string.split()
        for i in scene_string:
            replacement = item_in_scene(i, replacement_items)
            if replacement != None:
                user_input = raw_input(fill + replacement + l)
                i = i.replace(replacement, user_input)
                replaced.append(i)
            else:
                replaced.append(i)
        replaced = " ".join(replaced)
        if check(level, user_input, diff) == False:
            count = count - 1
            if count > 0:
                print replaced + die
                continue
            else:
                break
        else:
            print replaced + accept
            level = level + 1
            if level > 3:
                return 'you win, kthxbye'
            else:
                print lvlup
                run_adventure(level, count)

    #return replaced + murder + out




#print scene
#dventure1(diff_scene(raw_input), 5, replacement_items)
print run_adventure(1, 2)

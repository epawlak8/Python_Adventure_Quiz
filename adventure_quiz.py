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
welcome ='Welcome adventurer, a great quest lies ahead!'
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

#supplies scene string based on level, difficulty and scene
def diff_scene(level, diff, scene):
    if level == 1 and diff == 1:
        if scene == 4:
            return color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
    To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'rock' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
    You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
    The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + 'laptop, textbook, an angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'water bottle' + color.DARKCYAN + '''.
    You're thankful to discover that you're fully clothed in Jeans, a warm sweater, running shoes and light gloves.

    Nightfall is coming, choose which 4 items you'll keep in the backpack to survive
    (note: use 1 word lowercase answers, ie. Rusty Hunting Knife = knife)

    Your ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' will now hold:
    ''' + color.RED + '_1_ _2_ _3_ _4_' + color.END

    if level == 2:
        if diff == 1 and scene == 1:
            return color.DARKCYAN + '''Thunder rumbles in the sky and you know rain will fall soon, you must find shelter.
    You remember a cave, and you know it is west of your current location.
    A sliver of the sun still shines to your right, though as you look, it dips below the horizon.

    You can go left, right, forwards or backwards to find the cave. You choose to go''' + color.RED + ''' _1_''' + color.DARKCYAN + '.' + color.END
        if diff == 1 and scene == 2:
            return'''
    5 minutes into your walk towards the cave heavy rain starts to fall.
    You think you hear a noise behind you, when you turn around you see ''' + color.RED + 'A WILD BEAR CHARGING AT YOU!' +color.DARKCYAN + '''
    You need to make a split decision, ''' + color.GREEN + 'stand your ground and use your knife (fight) ' + color.DARKCYAN + 'or' + color.GREEN + ''' Run like hell (flee)
    You choose to ''' + color.RED + '_2_' + color.END
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
def check(level, answer, diff, scene):
    if level == 1 and diff == 1 and scene == 4:
        if answer == ('knife') or ('lemons') or ('textbook') or ('bottle'):
            return True
        else:
            return False
    if level == 2 and diff == 1:
        if scene == 1 and answer == ('left'):
            return True
        else:
            return False
        if scene == 2 and answer == ('flee'):
            return True
        else:
            return False


#brings together all the functions
def run_adventure(level, count, scene_num):
    diff = difficulty(raw_input)
    if level < 2:
        print welcome
    while count > 0:
        #diff = difficulty(raw_input)
        #scene_num = 1
        scene_string = diff_scene(level, diff, scene_num)
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
        if check(level, user_input, diff, scene_num) == False:
            count = count - 1
            if count > 0:
                print replaced + die
                continue
            else:
                break
        else:
            print replaced + accept
            scene_num = scene_num + 1
            if scene_num < 5:
                level = level + 1
                if level > 3:
                    return 'you win, kthxbye'
                else:
                    if scene_num < 5:
                        print 'next scene'
                        run_adventure(level, count, scene_num)
                        #continue
            if scene_num == 5:
                level = level + 1
                print lvlup

                run_adventure(level, count, 1)
                #continue
            else:
                return 'you win, byeee'

    #return replaced + murder + out


#print item_in_scene()
#print diff_scene(1, 1, 1)
#print scene
#dventure1(diff_scene(raw_input), 5, replacement_items)
print run_adventure(1, 2, 4)

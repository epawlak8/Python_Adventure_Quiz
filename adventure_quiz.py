#color class from Boubakr @ stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
class color:
   DARKCYAN = '\033[36m'
   YELLOW = '\033[93m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

replacement_items=['_1_', '_2_', '_3_', '_4_', '_5_']

#story strings to keep functions below cleaner
die=color.RED + '''

You have chosen poorly and you die so hard.

''' + color.GREEN + '''
You have failed to survive! Please Try again:
''' + color.END
welcome=color.GREEN + '''

Welcome adventurer, a great quest lies ahead!

This game has 4 levels with 4 scenes per level.

You will be asked to provide text answers, please use 1 word, lowercase answers.

Good Luck!
''' + color.END
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

lvl_1_diff_1_scene_1=color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'rock' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + 'laptop, textbook, an angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'lighter' + color.DARKCYAN + '''.
You're thankful to discover that you're fully clothed in Jeans, a warm sweater, running shoes and light gloves.
The first item you put in your backpack is the '''+ color.RED + '''_1_''' + color.DARKCYAN + '.' + color.END

lvl_1_diff_1_scene_2=color.DARKCYAN + '''
The second item you put in your backpack is the ''' + color.RED + '_2_' + color.DARKCYAN + '.' + color.END

lvl_1_diff_1_scene_3=color.DARKCYAN + '''
The third item you put in your backpack is the ''' + color.RED + '_3_' + color.DARKCYAN + '.' + color.END

lvl_1_diff_1_scene_4=color.DARKCYAN + '''
The fourth item you put in your backpack is the ''' + color.RED + '_4_' + color.DARKCYAN + '.' + color.END

lvl_1_diff_2_scene_1=color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'decorative knome' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + '4 crayons, textbook, a very angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'lighter' + color.DARKCYAN + '''.
You're bummed out to discover that you're only wearing pants, flip flops and a belly shirt... odd... pretty drafty I bet.
The first item you put in your backpack is the '''+ color.RED + '''_1_''' + color.DARKCYAN + '.' + color.END

lvl_1_diff_3_scene_1=color.DARKCYAN + '''You awake in a cold forest, nightfall is coming. You find yourself surrounded by trees in every direction.
To your left you find a ''' +color.GREEN + 'rusty hunting knife' + color.DARKCYAN + ' and a ' + color.GREEN + 'decorative knome' + color.DARKCYAN + ''' and to your right, ''' +color.GREEN + 'a pack of shepard lemons' + color.DARKCYAN + '''.
You also find a ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' on the ground behind you.
The ''' +color.YELLOW + 'backpack' + color.DARKCYAN + ''' can fit 4 items, though it already holds a ''' +color.GREEN + '4 crayons, textbook, a very angry ferret' + color.DARKCYAN + ' and a ' + color.GREEN + 'lighter' + color.DARKCYAN + '''.
You're dismayed to discover that you're only wearing a swim suit and socks... Weird choice for a cold forest... I bet you die pretty quickly.
The first item you put in your backpack is the '''+ color.RED + '''_1_''' + color.DARKCYAN + '.' + color.END

lvl_2_diff_1_scene_1=color.DARKCYAN + '''Thunder rumbles in the sky and you know rain will fall soon, you must find shelter.
You remember a cave, and you know it is west of your current location.
A sliver of the sun still shines to your right, though as you look, it dips below the horizon.

You can go left, right, forwards or backwards to find the cave. You choose to go''' + color.RED + ''' _1_''' + color.DARKCYAN + '''.
''' + color.END

lvl_2_diff_1_scene_2=color.DARKCYAN + '''

5 minutes into your walk towards the cave heavy rain starts to fall.
You think you hear a noise behind you, when you turn around you see ''' + color.RED + 'A WILD BEAR CHARGING AT YOU!' +color.DARKCYAN + '''

You need to make a split decision, ''' + color.GREEN + 'stand your ground and use your knife (fight) ' + color.DARKCYAN + 'or' + color.GREEN + ''' Run like hell (flee)
You choose to ''' + color.RED + '_2_' + color.DARKCYAN + '.' + color.END + '''
''' + color.END

lvl_2_diff_1_scene_3=color.DARKCYAN + '''

You escape the bear and run through the forest, by the time you reach the cave it's like super dark out.
Near the entrance of the cave you find some dead twigs.
Once in the cave you use the ''' + color.RED + '_3_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ''' to light the twigs on fire.
''' + color.END

lvl_2_diff_1_scene_4=color.DARKCYAN + '''

The twigs are wet, and you need to use the ''' + color.RED +  '_4_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'Backpack' + color.DARKCYAN + ''' as kindling to get the fire going,
nice and toasty!

''' + color.END

lvl_2_diff_2_scene_1=color.DARKCYAN + '''Thunder rumbles in the sky and you know rain will fall soon, you must find shelter.
You think there is a cave somwhere, and you think it is west of your current location.
As you try to get your bearings from the sun you trip, fall and hit your head.
You awake later, it is pitch black, you don't know which way the cave is.

You can go left, right, forwards or backwards to find the cave. You choose to go''' + color.RED + ''' _1_''' + color.DARKCYAN + '''.
''' + color.END

lvl_2_diff_2_scene_2=color.DARKCYAN + '''

When you awoke the second time rain was already falling and...
OH SHIT! ''' + color.RED + 'A WILD BEAR IS CHARGING AT YOU!' +color.DARKCYAN + '''

You need to make a split decision, ''' + color.GREEN + 'stand your ground and use your knife (fight) ' + color.DARKCYAN + 'or' + color.GREEN + ''' Run like hell (flee)
You choose to ''' + color.RED + '_2_' + color.DARKCYAN + '.' + color.END + '''
''' + color.END

lvl_2_diff_2_scene_3=color.DARKCYAN + '''

You escape the bear and run through the forest, You trip and fall so much because it's like super dark out,
you're like 27.3 percent hurt... Pretty bad
Near the entrance of the cave you dont find any wood to burn, but you find a significant amount of bat guano.
Once in the cave you use the ''' + color.RED + '_3_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ''' to light the guano on fire.
You're about to have a terrbile fire... Just vile.
''' + color.END

lvl_2_diff_2_scene_4=color.DARKCYAN + '''

The guano is wet, and just like super gross, and you need to use the ''' + color.RED +  '_4_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'Backpack' + color.DARKCYAN + ''' as kindling to get the fire going,
Great! So enjoy the bat shit campfire...

''' + color.END

lvl_2_diff_3_scene_1=color.DARKCYAN + '''Rain starts to fall on you out of nowhere and it's a huge amount of rain.
You think there is a cave somwhere, but you honestly can't remember where it was.
As you try to get your bearings from the sun you trip, fall and hit your head.
You awake later, it is pitch black, you don't know which way the cave is.
You realize some sort of animal has eaten like... 67.2 percent of your left leg... soooo... Not great really...

You can go left, right, forwards or backwards to find the cave. You choose to go''' + color.RED + ''' _1_''' + color.DARKCYAN + '''.
''' + color.END

lvl_2_diff_3_scene_2=color.DARKCYAN + '''

You're wet and partially legless
OH SHIT! ''' + color.RED + 'A WILD BEAR IS CHARGING AT YOU!' +color.DARKCYAN + '''

You need to make a split decision, ''' + color.GREEN + 'stand your ground and use your knife (fight) ' + color.DARKCYAN + 'or' + color.GREEN + ''' Run like hell (flee)
You choose to ''' + color.RED + '_2_' + color.DARKCYAN + '.' + color.DARKCYAN + '''
But either way... I bet you loose a hand.''' + color.END

lvl_2_diff_3_scene_3=color.DARKCYAN + '''

You escape the bear and hobble through the forest, You trip and fall so much because it's like super dark out,
you're like 86.3 percent hurt...so bad.
I was right, you totally lost a hand back there with the bear, there was a lot of blood.
You fall into a hole and you can't really get out, so you just stay there.
Once in the hole you have to make a fire out of something, so use your socks I guess... Gross.
You use the ''' + color.RED + '_3_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ''' to light the socks on fire.
You're about to have a terrbile fire... Just vile.
''' + color.END

lvl_2_diff_3_scene_4=color.DARKCYAN + '''

The socks are wet, and just like so gross, and you need to use the ''' + color.RED +  '_4_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'Backpack' + color.DARKCYAN + ''' as kindling to get the fire going,
Great! So enjoy the dirty socks campfire...

''' + color.END

lvl_3_diff_1_scene_1=color.DARKCYAN + '''Your eyelids grow heavy and you finally begin to grow tired by the fire,
before you fall asleep you eat the ''' +color.RED + '_1_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + '.' + color.END

lvl_3_diff_1_scene_2=color.DARKCYAN + '''You settle in for the night and decide that because you don't know who or what may lurk nearby,
it's probably safest to sleep with the ''' + color.RED + '_2_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ' closest to you, just in case.' + color.END

lvl_3_diff_1_scene_3=color.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. You open your eyes to see the entrance of the cave filling in with rocks and
debris... 'It must be a mudslide' you think. You realize you'll either have to clear the rocks and debris
in the morning (later), or try to dig a whole through the muddy rocks while it's wet (now).
You choose to do it ''' + color.RED + '_3_' + color.DARKCYAN + '.' + color.END

lvl_3_diff_1_scene_4=color.DARKCYAN + '''Morning finally comes and you climb out the small hole you made the night before into the sunlight.
You know if you walk North you will eventually reach the highway, and someone who can help you.
The sun rises to your right, you know this means you must go(left, right forward or back) ''' + color.RED + '_4_' + color.DARKCYAN + '.' + color.END

lvl_3_diff_2_scene_1=color.DARKCYAN + '''Your eyelids grow heavy and you finally begin to grow tired by the fire,
before you fall asleep you eat the ''' +color.RED + '_1_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + '.' + color.END

lvl_3_diff_2_scene_2=color.DARKCYAN + '''You settle in for the night and decide that because you don't know who or what may lurk nearby,
it's probably safest to sleep with the ''' + color.RED + '_2_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ' closest to you, just in case.' + color.END

lvl_3_diff_2_scene_3=color.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to be drowning in a puddle.
You realize you'll either have to clear the debris and try to empty out the water.
You can do it in the morning (later), or try to dig a whole through the muddy rocks while it's wet (now).
You choose to do it ''' + color.RED + '_3_' + color.DARKCYAN + '.' + color.DARKCYAN + ''' You use your one existing hand to fling the water out of the hole.
It sucks and you're bleeding a bunch''' + color.END

lvl_3_diff_2_scene_4=color.DARKCYAN + '''Morning finally comes and you climb out the small hole you made the night before into the sunlight.
You know if you walk North you will eventually reach the highway, and someone who can help you.
The sun rises to your right, you know this means you must go(left, right forward or back) ''' + color.RED + '_4_' + color.DARKCYAN + '.' + color.END

lvl_3_diff_3_scene_1=color.DARKCYAN + '''Your eyelids grow heavy and you finally begin to grow tired by the fire,
before you fall asleep you eat the ''' +color.RED + '_1_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + '.' + color.END

lvl_3_diff_3_scene_2=color.DARKCYAN + '''You settle in for the night and decide that because you don't know who or what may lurk nearby,
it's probably safest to sleep with the ''' + color.RED + '_2_' + color.DARKCYAN + ' from your ' + color.YELLOW + 'backpack' + color.DARKCYAN + ' closest to you, just in case.' + color.END

lvl_3_diff_3_scene_3=color.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to be drowning in a puddle.
You realize you'll either have to clear the debris and try to empty out the water.
You can do it in the morning (later), or try to dig a whole through the muddy rocks while it's wet (now).
You choose to do it ''' + color.RED + '_3_' + color.DARKCYAN + '.' + color.DARKCYAN + ''' You use your one existing hand to fling the water out of the hole.
It sucks and you're bleeding a bunch''' + color.END

lvl_3_diff_3_scene_4=color.DARKCYAN + '''Morning finally comes and you climb out the small hole you made the night before into the sunlight.
You know if you walk North you will eventually reach the highway, and someone who can help you.
You will most certainly die today.
The sun rises to your right, you know this means you must go(left, right forward or back) ''' + color.RED + '_4_' + color.DARKCYAN + '''.
You try to go towards the highway, but obviously you don't make it and you die''' + color.END


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

#sets number of guesses the user gets
def set_count(user_input):
    user_input=raw_input('''Please type a number between 1 and 10 to select the number of guesses you will have to answer questions:
''')
    return user_input

#supplies scene string based on level, difficulty and scene
def diff_scene(level, diff, scene):
    while level == 1:
        while diff == 1:
            if scene == 1:
                return lvl_1_diff_1_scene_1
            if scene == 2:
                return lvl_1_diff_1_scene_2
            if scene == 3:
                return lvl_1_diff_1_scene_3
            if scene == 4:
                return lvl_1_diff_1_scene_4
        while diff == 2:
            if scene == 1:
                return lvl_1_diff_2_scene_1
            if scene == 2:
                return lvl_1_diff_1_scene_2
            if scene == 3:
                return lvl_1_diff_1_scene_3
            if scene == 4:
                return lvl_1_diff_1_scene_4
        while diff == 3:
            if scene == 1:
                return lvl_1_diff_3_scene_1
            if scene == 2:
                return lvl_1_diff_1_scene_2
            if scene == 3:
                return lvl_1_diff_1_scene_3
            if scene == 4:
                return lvl_1_diff_1_scene_4

    while level == 2:
        while diff == 1:
            if scene == 1:
                return lvl_2_diff_1_scene_1
            if scene == 2:
                return lvl_2_diff_1_scene_2
            if scene == 3:
                return lvl_2_diff_1_scene_3
            if scene == 4:
                return lvl_2_diff_1_scene_4
        while diff == 2:
            if scene == 1:
                return lvl_2_diff_2_scene_1
            if scene == 2:
                return lvl_2_diff_2_scene_2
            if scene == 3:
                return lvl_2_diff_2_scene_3
            if scene == 4:
                return lvl_2_diff_2_scene_4
        while diff == 3:
            if scene == 1:
                return lvl_2_diff_3_scene_1
            if scene == 2:
                return lvl_2_diff_3_scene_2
            if scene == 3:
                return lvl_2_diff_3_scene_3
            if scene == 4:
                return lvl_2_diff_3_scene_4
    while level == 3:
        while diff == 1:
            if scene == 1:
                return lvl_3_diff_1_scene_1
            if scene == 2:
                return lvl_3_diff_1_scene_2
            if scene == 3:
                return lvl_3_diff_1_scene_3
            if scene == 4:
                return lvl_3_diff_1_scene_4
        while diff == 2:
            if scene == 1:
                return lvl_3_diff_2_scene_1
            if scene == 2:
                return lvl_3_diff_2_scene_2
            if scene == 3:
                return lvl_3_diff_2_scene_3
            if scene == 4:
                return lvl_3_diff_2_scene_4
        while diff == 3:
            if scene == 1:
                return lvl_3_diff_3_scene_1
            if scene == 2:
                return lvl_3_diff_3_scene_2
            if scene == 3:
                return lvl_3_diff_3_scene_3
            if scene == 4:
                return lvl_3_diff_3_scene_4
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

#checks answer based on level and scene
def check(level, answer, scene):
    while level == 1:
        while scene == 1:
            if answer == ('knife'):
                return True
            else:
                return False
        while scene == 2:
            if answer == ('lemons'):
                return True
            else:
                return False
        while scene == 3:
            if answer == ('textbook'):
                return True
            else:
                return False
        while scene == 4:
            if answer == ('lighter'):
                return True
            else:
                return False

    while level == 2:
        while scene == 1:
            if answer == ('left'):
                return True
            else:
                return False
        while scene == 2:
            if answer == ('flee'):
                return True
            else:
                return False
        while scene == 3:
            if answer == ('lighter'):
                return True
            else:
                return False
        while scene == 4:
            if answer == ('textbook'):
                return True
            else:
                return False

    while level == 3:
        while scene == 1:
            if answer == ('lemons'):
                return True
            else:
                return False
        while scene == 2:
            if answer == ('knife'):
                return True
            else:
                return False
        while scene == 3:
            if answer == ('now'):
                return True
            else:
                return False
        while scene == 4:
            if answer == ('forward'):
                return True
            else:
                return False

#brings together all the functions
def run_adventure(level, count, diff, scene_num, rep):
    while count > 0:
        scene_string = diff_scene(level, diff, scene_num)
        print chances(count)
        print scene_string
        if scene_num == 1:
            replaced = []
        else:
            replaced = [rep]
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
        if check(level, user_input, scene_num) == False:
            count = count - 1
            if count > 0:
                print replaced + die
                continue
            else:
                print color.RED + 'You loose, how unfortunate!'
                break
        else:
            print replaced + accept
            scene_num = scene_num + 1
            if scene_num < 5:
                run_adventure(level, count, diff, scene_num, replaced)
            else:
                level = level + 1
                if level < 4:
                    print lvlup
                    run_adventure(level, count, diff, 1, replaced)
                print color.RED + 'you win, game over man'
                break
            break
        break

print welcome
run_adventure(1, int(set_count(raw_input)), difficulty(raw_input), 1, None)

class col:
    """
    Adds color to text strings
    color class from Boubakr @
    stackoverflow.com/questions/8924173/how-do-i-print-BO-text-in-python
    """
    DARKCYAN = '\033[36m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

    # From here to line 319 are story strings to keep functions below cleaner
die = col.RED + '''

You have chosen poorly and you die so hard.

''' + col.GREEN + '''
You have failed to survive! Please Try again:
''' + col.END

welcome = col.GREEN + '''

Welcome adventurer, a great quest lies ahead!

This game has 4 levels with 4 scenes per level.

You will be asked to provide text answers, please use 1 word answers.

Good Luck!
''' + col.END

fill = col.GREEN + "Fill in the blank for "

colon = ''':
 ''' + col.END

accept = '''

You have chosen well and you will live for now!
''' + col.END

out = col.RED + '''

You have run out of chances!

You die alone. Probably cold... Sucks I bet...''' + col.END

lvlup = col.GREEN + '''

***YOU MADE IT TO THE NEXT LEVEL, HELL YEAH BUDDY***

''' + col.END

lvl_1_diff_1_scene_1 = col.DARKCYAN + """
You awake in a cold forest, nightfall is coming.
You find yourself surrounded by trees in every direction.
To your left you find a """ + col.GREEN + """rusty hunting
knife""" + col.DARKCYAN + """ and a """ + col.GREEN + """rock,
""" + col.DARKCYAN + """ and to your right, """ + col.GREEN + """a pack of
shepard lemons""" + col.DARKCYAN + """. You also find a
""" + col.YELLOW + """backpack""" + col.DARKCYAN + """ on the ground behind
you. The """ + col.YELLOW + """backpack""" + col.DARKCYAN + """ can fit 4
items, though it already holds a """ + col.GREEN + """laptop, textbook,
an angry ferret""" + col.DARKCYAN + """ and a """ + col.GREEN + """lighter
""" + col.DARKCYAN + """. You're thankful to discover that you're fully
clothed in Jeans, a warm sweater, running shoes and light gloves.
The first item you put in your backpack is:
the """ + col.RED + "_1_" + col.DARKCYAN + "." + col.END

lvl_1_diff_1_scene_2 = col.DARKCYAN + '''
The second item you put in your backpack is the
''' + col.RED + '_2_' + col.DARKCYAN + '.' + col.END

lvl_1_diff_1_scene_3 = col.DARKCYAN + '''
The third item you put in your backpack is the
''' + col.RED + '_3_' + col.DARKCYAN + '.' + col.END

lvl_1_diff_1_scene_4 = col.DARKCYAN + '''
The fourth item you put in your backpack is the
''' + col.RED + '_4_' + col.DARKCYAN + '.' + col.END

lvl_1_diff_2_scene_1 = col.DARKCYAN + """
You awake in a cold forest, nightfall is coming.
You find yourself surrounded by trees in every direction.
To your left you find a """ + col.GREEN + """rusty hunting knife
""" + col.DARKCYAN + """ and a """ + col.GREEN + """decorative gnome,
""" + col.DARKCYAN + 'and to your right, ' + col.GREEN + """a pack of
shepard lemons""" + col.DARKCYAN + """. You also find a
""" + col.YELLOW + """backpack""" + col.DARKCYAN + """ on the ground behind
you. The """ + col.YELLOW + """backpack""" + col.DARKCYAN + """ can fit 4
items, though it already holds a """ + col.GREEN + """laptop, textbook,
an angry ferret""" + col.DARKCYAN + """ and a """ + col.GREEN + """lighter
""" + col.DARKCYAN + """. You're thankful to discover that
you're fully clothed in Jeans, a warm sweater, running shoes and light gloves.
The first item you put in your backpack is:
the """ + col.RED + "_1_" + col.DARKCYAN + "." + col.END

lvl_1_diff_3_scene_1 = col.DARKCYAN + '''You awake in a cold forest, nightfall
is coming. You find yourself surrounded by trees in every direction. To your
left you find a ''' + col.GREEN + 'rusty hunting knife' + col.DARKCYAN + '''
and a ''' + col.GREEN + 'decorative knome' + col.DARKCYAN + ''' and to your
right, ''' + col.GREEN + 'a pack of shepard lemons' + col.DARKCYAN + '''. You
also find a ''' + col.YELLOW + 'backpack' + col.DARKCYAN + ''' on the ground
behind you. The ''' + col.YELLOW + 'backpack' + col.DARKCYAN + ''' can fit 4
items, though it already holds ''' + col.GREEN + """4 crayons, textbook, a
very angry ferret""" + col.DARKCYAN + 'and a ' + col.GREEN + """lighter
""" + col.DARKCYAN + '''.
You're dismayed to discover that you're only wearing a swim suit and socks...
Weird choice for a cold forest... I bet you die pretty quickly. The first item
you put in your backpack is the
''' + col.RED + '''_1_''' + col.DARKCYAN + '.' + col.END

lvl_2_diff_1_scene_1 = col.DARKCYAN + '''Thunder rumbles in the sky and you
know rain will fall soon, you must find shelter. You remember a cave, and you
know it is west of your current location. A sliver of the sun still shines to
your right, though as you look, it dips below the horizon.

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RED + ' _1_' + col.DARKCYAN + '.' + col.END

lvl_2_diff_1_scene_2 = col.DARKCYAN + '''

5 minutes into your walk towards the cave heavy rain starts to fall.
You think you hear a noise behind you, when you turn around you see
''' + col.RED + 'A WILD BEAR CHARGING AT YOU!' + col.DARKCYAN + '''

You need to make a split decision,
''' + col.GREEN + '''stand your ground and use your knife (fight)
''' + col.DARKCYAN + ''' or''' + col.GREEN + ''' Run like hell (flee)
You choose to ''' + col.RED + '_2_' + col.DARKCYAN + '''.
''' + col.END

lvl_2_diff_1_scene_3 = col.DARKCYAN + '''

You escape the bear and run through the forest, by the time you reach the cave
it's like super dark out. Near the entrance of the cave you find some dead
twigs. Once in the cave you use the ''' + col.RED + '_3_' + col.DARKCYAN + '''
 from your ''' + col.YELLOW + 'backpack' + col.DARKCYAN + ''' to light the
twigs on fire. ''' + col.END

lvl_2_diff_1_scene_4 = col.DARKCYAN + '''

The twigs are wet, and you need to use the ''' + col.RED + '''_4_
''' + col.DARKCYAN + ' from your ' + col.YELLOW + '''Backpack
''' + col.DARKCYAN + ''' as kindling to get the fire going, nice and toasty!
''' + col.END

lvl_2_diff_2_scene_1 = col.DARKCYAN + '''Thunder rumbles in the sky and you
know rain will fall soon, you must find shelter. You think there is a cave
somwhere, and you think it is west of your current location. As you try to
get your bearings from the sun you trip, fall and hit your head. You awake
later, it is pitch black, you don't know which way the cave is.

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RED + ''' _1_''' + col.DARKCYAN + '''.
''' + col.END

lvl_2_diff_2_scene_2 = col.DARKCYAN + '''

When you awoke the second time rain was already falling and...
OH SHIT! ''' + col.RED + 'A WILD BEAR IS CHARGING AT YOU!' + col.DARKCYAN + '''

You need to make a split decision,
''' + col.GREEN + '''stand your ground and use your knife (fight)
''' + col.DARKCYAN + ''' or''' + col.GREEN + ''' Run like hell (flee)
You choose to ''' + col.RED + '_2_' + col.DARKCYAN + '.' + col.END + '''
''' + col.END

lvl_2_diff_2_scene_3 = col.DARKCYAN + '''

You escape the bear and run through the forest, You trip and fall so much
because it's like super dark out, you're like 27.3 percent hurt... Pretty bad
Near the entrance of the cave you dont find any wood to burn, but you find a
significant amount of bat guano. Once in the cave you use the
''' + col.RED + '_3_' + col.DARKCYAN + ' from your ' + col.YELLOW + '''backpack
''' + col.DARKCYAN + ''' to light the guano on fire.
You're about to have a terrbile fire... Just vile.
''' + col.END

lvl_2_diff_2_scene_4 = col.DARKCYAN + '''

The guano is wet, and just like super gross, and you need to use the
''' + col.RED + '_4_' + col.DARKCYAN + ' from your ' + col.YELLOW + '''Backpack
''' + col.DARKCYAN + ''' as kindling to get the fire going,
Great! So enjoy the bat shit campfire...

''' + col.END

lvl_2_diff_3_scene_1 = col.DARKCYAN + '''Rain starts to fall on you out of
nowhere and it's a huge amount of rain. You think there is a cave somwhere,
but you honestly can't remember where it was. As you try to get your bearings
from the sun you trip, fall and hit your head. You awake later, it is pitch
black, you don't know which way the cave is. You realize some sort of animal
has eaten like... 67.2 percent of your left leg... soooo... Not great really...

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RED + ''' _1_''' + col.DARKCYAN + '''.
''' + col.END

lvl_2_diff_3_scene_2 = col.DARKCYAN + '''

You're wet and partially legless
OH SHIT! ''' + col.RED + 'A WILD BEAR IS CHARGING AT YOU!' + col.DARKCYAN + '''

You need to make a split decision,
''' + col.GREEN + '''stand your ground and use your knife (fight)
''' + col.DARKCYAN + '''or''' + col.GREEN + ''' Run like hell (flee)
You choose to ''' + col.RED + '_2_' + col.DARKCYAN + '.' + col.DARKCYAN + '''
But either way... I bet you loose a hand.''' + col.END

lvl_2_diff_3_scene_3 = col.DARKCYAN + '''

You escape the bear and hobble through the forest, You trip and fall so much
because it's like super dark out, you're like 86.3 percent hurt...so bad.
I was right, you totally lost a hand back there with the bear, there was a
lot of blood. You fall into a hole and you can't really get out, so you just
stay there. Once in the hole you have to make a fire out of something, so use
your socks I guess... Gross. You use the ''' + col.RED + '''_3_
''' + col.DARKCYAN + ' from your ' + col.YELLOW + '''backpack
''' + col.DARKCYAN + ''' to light the socks on fire.You're about to have a
terrbile fire... Just vile.
''' + col.END

lvl_2_diff_3_scene_4 = col.DARKCYAN + '''

The socks are wet, and just like so gross, and you need to use the
''' + col.RED + '_4_' + col.DARKCYAN + ' from your ' + col.YELLOW + '''Backpack
''' + col.DARKCYAN + ''' as kindling to get the fire going,
Great! So enjoy the dirty socks campfire...

''' + col.END

lvl_3_diff_1_scene_1 = col.DARKCYAN + '''Your eyelids grow heavy and you
finally begin to grow tired by the fire, before you fall asleep you eat the
''' + col.RED + '_1_' + col.DARKCYAN + ''' from your
''' + col.YELLOW + 'backpack' + col.END

lvl_3_diff_1_scene_2 = col.DARKCYAN + '''You settle in for the night and
decide that because you don't know who or what may lurk nearby, it's probably
safest to sleep with the ''' + col.RED + '_2_' + col.DARKCYAN + ''' from your
''' + col.YELLOW + 'backpack' + col.DARKCYAN + ''' closest to you,
just in case.''' + col.END

lvl_3_diff_1_scene_3 = col.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. You open your eyes to see the entrance
of the cave filling in with rocks and debris... 'It must be a mudslide' you
think. You realize you'll either have to clear the rocks and debris in the
morning (later), or try to dig a whole through the muddy rocks while it's
wet (now). You choose to do it ''' + col.RED + '_3_' + col.DARKCYAN + '''.
''' + col.END

lvl_3_diff_1_scene_4 = col.DARKCYAN + '''Morning finally comes and you climb
out the small hole you made the night before into the sunlight. You know if
you walk north you will eventually reach the highway, and someone who can
help you. The sun rises to your right, you know this means you must go
(left, right forward or back) ''' + col.RED + '_4_' + col.DARKCYAN + '''.
''' + col.END

lvl_3_diff_2_scene_1 = col.DARKCYAN + '''Your eyelids grow heavy and you
finally begin to grow tired by the fire, before you fall asleep you eat the
''' + col.RED + '_1_' + col.DARKCYAN + ''' from your
''' + col.YELLOW + 'backpack' + col.END

lvl_3_diff_2_scene_2 = col.DARKCYAN + '''You settle in for the night and
decide that because you don't know who or what may lurk nearby, it's probably
safest to sleep with the ''' + col.RED + '_2_' + col.DARKCYAN + ''' from your
''' + col.YELLOW + 'backpack' + col.DARKCYAN + ''' closest to you,
just in case.''' + col.END

lvl_3_diff_2_scene_3 = col.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to
be drowning in a puddle. You realize you'll either have to clear the debris
and try to empty out the water. You can do it in the morning (later), or try
to dig a whole through the muddy rocks while it's wet (now). You choose to do
it ''' + col.RED + '_3_' + col.DARKCYAN + '.' + col.DARKCYAN + ''' You use
your one existing hand to fling the water out of the hole.
It sucks and you're bleeding a bunch''' + col.END

lvl_3_diff_2_scene_4 = col.DARKCYAN + '''Morning finally comes and you climb
out the small hole you made the night before into the sunlight. You know if
you walk north you will eventually reach the highway, and someone who can
help you. The sun rises to your right, you know this means you must go
(left, right forward or back) ''' + col.RED + '_4_' + col.DARKCYAN + '''.
''' + col.END

lvl_3_diff_3_scene_1 = col.DARKCYAN + '''Your eyelids grow heavy and you
finally begin to grow tired by the fire, before you fall asleep you eat the
''' + col.RED + '_1_' + col.DARKCYAN + ''' from your
''' + col.YELLOW + 'backpack' + col.END

lvl_3_diff_3_scene_2 = col.DARKCYAN + '''You settle in for the night and
decide that because you don't know who or what may lurk nearby, it's probably
safest to sleep with the ''' + col.RED + '''_2_
''' + col.DARKCYAN + ' from your ' + col.YELLOW + ''' backpack
''' + col.DARKCYAN + ' closest to you, just in case.' + col.END

lvl_3_diff_3_scene_3 = col.DARKCYAN + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to
be drowning in a puddle. You realize you'll either have to clear the debris
and try to empty out the water. You can do it in the morning (later), or try
to dig a whole through the muddy rocks while it's wet (now). You choose to
do it ''' + col.RED + '_3_' + col.DARKCYAN + '.' + col.DARKCYAN + ''' You use
your one existing hand to fling the water out of the hole. It sucks and you're
bleeding a bunch''' + col.END

lvl_3_diff_3_scene_4 = col.DARKCYAN + '''Morning finally comes and you climb
out the small hole you made the night before into the sunlight. You know if
you walk north you will eventually reach the highway, and someone who can
help you. You will most certainly die today. The sun rises to your right,
you know this means you must go
(left, right forward or back) ''' + col.RED + '_4_' + col.DARKCYAN + '''.
You try to go towards the highway,
but obviously you don't make it and you die''' + col.END


lvl_data = {
    # dict that provdies answers and items to be replaced based on level
    'lvl_1': {
        'answers': {'scene_1': 'knife',
                    'scene_2': 'lemons',
                    'scene_3': 'textbook',
                    'scene_4': 'lighter', }, },
    'lvl_2': {
        'answers': {'scene_1': 'left',
                    'scene_2': 'flee',
                    'scene_3': 'lighter',
                    'scene_4': 'textbook', }, },
    'lvl_3': {
        'answers': {'scene_1': 'lemons',
                    'scene_2': 'knife',
                    'scene_3': 'now',
                    'scene_4': 'forward', }, },
    'replacement_items': ['_1_', '_2_', '_3_', '_4_', '_5_']}

scene_data = {
    # dict that outputs correct string based on difficulty, level and scene
    'easy': {
        'lvl_1': {'scene_1': lvl_1_diff_1_scene_1,
                  'scene_2': lvl_1_diff_1_scene_2,
                  'scene_3': lvl_1_diff_1_scene_3,
                  'scene_4': lvl_1_diff_1_scene_4},
        'lvl_2': {'scene_1': lvl_2_diff_1_scene_1,
                  'scene_2': lvl_2_diff_1_scene_2,
                  'scene_3': lvl_2_diff_1_scene_3,
                  'scene_4': lvl_2_diff_1_scene_4},
        'lvl_3': {'scene_1': lvl_3_diff_1_scene_1,
                  'scene_2': lvl_3_diff_1_scene_2,
                  'scene_3': lvl_3_diff_1_scene_3,
                  'scene_4': lvl_3_diff_1_scene_4},
        'count': 5
            },
    'medium': {
        'lvl_1': {'scene_1': lvl_1_diff_2_scene_1,
                  'scene_2': lvl_1_diff_1_scene_2,
                  'scene_3': lvl_1_diff_1_scene_3,
                  'scene_4': lvl_1_diff_1_scene_4},
        'lvl_2': {'scene_1': lvl_2_diff_2_scene_1,
                  'scene_2': lvl_2_diff_2_scene_2,
                  'scene_3': lvl_2_diff_2_scene_3,
                  'scene_4': lvl_2_diff_2_scene_4},
        'lvl_3': {'scene_1': lvl_3_diff_2_scene_1,
                  'scene_2': lvl_3_diff_2_scene_2,
                  'scene_3': lvl_3_diff_2_scene_3,
                  'scene_4': lvl_3_diff_2_scene_4},
        'count': 3
             },
    'hard': {
        'lvl_1': {'scene_1': lvl_1_diff_3_scene_1,
                  'scene_2': lvl_1_diff_1_scene_2,
                  'scene_3': lvl_1_diff_1_scene_3,
                  'scene_4': lvl_1_diff_1_scene_4},
        'lvl_2': {'scene_1': lvl_2_diff_3_scene_1,
                  'scene_2': lvl_2_diff_3_scene_2,
                  'scene_3': lvl_2_diff_3_scene_3,
                  'scene_4': lvl_2_diff_3_scene_4},
        'lvl_3': {'scene_1': lvl_3_diff_3_scene_1,
                  'scene_2': lvl_3_diff_3_scene_2,
                  'scene_3': lvl_3_diff_3_scene_3,
                  'scene_4': lvl_3_diff_3_scene_4},
        'count': 1
            }}


def set_diff():
    # prompts user to select difficulty and returns value
    diff = raw_input('''Choose a level: (easy / medium / hard)
''').lower()
    if diff == 'easy':
        return 'easy'
    elif diff == 'medium':
        return 'medium'
    elif diff == 'hard':
        return 'hard'
    else:
        print 'wrong level'
        return set_diff()



def set_count(user_input):
    # takes user input to return an int as a number of guesses for play
    user_input = raw_input('''Please type a number between 1 and 10 to select
the number of guesses you will have to answer questions:
''')
    return int(user_input)


def select_scene(diff, level, scene):
    # takes difficulty level and scene as input and outputs scene string
        if scene in scene_data[diff][level]:
            return scene_data[diff][level][scene]
        return 'wrong scene'


def chances(count):
    # takes count as input and returns number of chances left as string
    return col.RED + 'You have ' + str(count) + ' chances remaining ' + col.END


def item_in_scene(scene, replacement_items):
    # checks if replacement item exists in a scene and returns the pos
    for pos in replacement_items:
        if pos in scene:
            return pos
    return None


def answer(level, answer, scene_num):
    # checks game answers depending on level and scene number
    if answer in lvl_data[level]['answers'][scene_num]:
        return True
    return False


def up(string):
    # takes string as input and changes either scene or level number to be +1
    string = list(string)
    if string[0] == 's':
        string[6] = int(string[6])+1
        string = ''.join(str(e) for e in string)
        return string
    if string[0] == 'l':
        string[4] = int(string[4])+1
        string = ''.join(str(e) for e in string)
        return string
    return 'bad up string'


def accept_loop(level, diff, count, scene, replaced):
    # this loop is to be used in the play funtion when an answer is correct
    print replaced + accept
    if scene != 'scene_4':
        scene = up(scene)
        play(level, diff, count, scene, replaced)
    else:
        if level != 'lvl_3':
            level = up(level)
            print lvlup
            play(level, diff, count, 'scene_1', replaced)
        print col.RED + 'you win, game over man'
        exit()


def fail_loop(level, diff, count, scene, replaced):
        # this loop to be used in the play funtion when an answer is incorrect
    count = count - 1
    if count > 0:
        print replaced + die
        play(level, diff, count, scene, replaced)
    else:
        print col.RED + 'You loose, how unfortunate!'
        exit()


def play(level, diff, count, scene, rep):
    '''
    Brings together all the functions and strings to play the game
    Takes as input the level, amount of guesses, difficulty, scene number and
    a replacement string then outputs the game until all guesses have
    been used or the game is won
    '''
    while count > 0:
        scene_string = select_scene(diff, level, scene)
        print chances(count)
        print scene_string
        replaced = [rep]
        scene_string = scene_string.split()
        for item in scene_string:
            replacement = item_in_scene(item, lvl_data['replacement_items'])
            if replacement is not None:
                user_input = raw_input(fill + replacement + colon).lower()
                item = item.replace(replacement, user_input)
                replaced.append(item)
            replaced.append(item)
        replaced = " ".join(replaced)
        if answer(level, user_input, scene) is not False:
            accept_loop(level, diff, count, scene, replaced)
        fail_loop(level, diff, count, scene, replaced)


print welcome
diff = set_diff()
count = scene_data[diff]['count']
play('lvl_1', diff, count, 'scene_1', '')

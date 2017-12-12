

class col:
    """
    Adds color to text strings
    color class from Boubakr @
    stackoverflow.com/questions/8924173/how-do-i-print-BO-text-in-python
    """
    DC = '\033[36m' # DARKCYAN
    YE = '\033[93m' # YELLOW
    GR = '\033[92m' # GREEN
    RE = '\033[91m' # RED
    BO = '\033[1m' # BOLD
    E = '\033[0m' # END

replacement_items=['_1_', '_2_', '_3_', '_4_', '_5_']


    # From here to line 318 are story strings to keep functions below cleaner
die=col.RE + '''

You have chosen poorly and you die so hard.

''' + col.GR + '''
You have failed to survive! Please Try again:
''' + col.E

welcome=col.GR + '''

Welcome adventurer, a great quest lies ahead!

This game has 4 levels with 4 scenes per level.

You will be asked to provide text answers, please use 1 word, answers.

Good Luck!
''' + col.E

fill=col.GR + "Fill in the blank for "

colon=''':
 ''' + col.E

accept='''

You have chosen well and you will live for now!
''' + col.E

out=col.RE + '''

You have run out of chances!

You die alone. Probably cold... Sucks I bet...''' + col.E

lvlup=col.GR + '''

***YOU MADE IT TO THE NEXT LEVEL, HELL YEAH BUDDY***

''' + col.E

lvl_1_diff_1_scene_1=col.DC + """
You awake in a cold forest, nightfall is coming.
You find yourself surrounded by trees in every direction.
To your left you find a """ + col.GR + """rusty hunting
knife""" + col.DC + """ and a """ + col.GR + 'rock,' + col.DC + """ and to your
right, """ +col.GR + """a pack of shepard lemons""" + col.DC + """. You
also find a """ +col.YE + """backpack""" + col.DC + """ on the ground behind
you. The """ + col.YE + """backpack""" + col.DC + """ can fit 4 items, though
it already holds a """ +col.GR + """laptop, textbook,
an angry ferret""" + col.DC + """ and a """ + col.GR + """lighter
""" + col.DC + """. You're thankful to discover that
you're fully clothed in Jeans, a warm
sweater, running shoes and light gloves.
The first item you put in your backpack is:
the """ + col.RE + "_1_" + col.DC + "." + col.E

lvl_1_diff_1_scene_2=col.DC + '''
The second item you put in your backpack is the
''' + col.RE + '_2_' + col.DC + '.' + col.E

lvl_1_diff_1_scene_3=col.DC + '''
The third item you put in your backpack is the
''' + col.RE + '_3_' + col.DC + '.' + col.E

lvl_1_diff_1_scene_4=col.DC + '''
The fourth item you put in your backpack is the
''' + col.RE + '_4_' + col.DC + '.' + col.E

lvl_1_diff_2_scene_1=col.DC + """
You awake in a cold forest, nightfall is coming.
You find yourself surrounded by trees in every direction.
To your left you find a """ + col.GR + """rusty hunting
knife""" + col.DC + """ and a """ + col.GR + 'decorative gnome,' + col.DC + """
and to your right, """ +col.GR + """a pack of shepard lemons""" + col.DC + """.
 You also find a """ +col.YE + """backpack""" + col.DC + """ on the ground
behind you. The """ + col.YE + """backpack""" + col.DC + """ can fit 4 items,
though it already holds a """ +col.GR + """laptop, textbook,
an angry ferret""" + col.DC + """ and a """ + col.GR + """lighter
""" + col.DC + """. You're thankful to discover that
you're fully clothed in Jeans, a warm
sweater, running shoes and light gloves.
The first item you put in your backpack is:
the """ + col.RE + "_1_" + col.DC + "." + col.E

lvl_1_diff_3_scene_1=col.DC + '''You awake in a cold forest, nightfall is
coming. You find yourself surrounded by trees in every direction. To your left
you find a ''' +col.GR + 'rusty hunting knife' + col.DC + ''' and
a ''' + col.GR + 'decorative knome' + col.DC + ''' and to your right,
''' +col.GR + 'a pack of shepard lemons' + col.DC + '''. You also find
a ''' +col.YE + 'backpack' + col.DC + ''' on the ground behind you. The
''' +col.YE + 'backpack' + col.DC + ''' can fit 4 items, though it already
holds ''' +col.GR + '4 crayons, textbook, a very angry ferret' + col.DC + '''
and a ''' + col.GR + 'lighter' + col.DC + '''.
You're dismayed to discover that you're only wearing a swim suit and socks...
Weird choice for a cold forest... I bet you die pretty quickly. The first item
you put in your backpack is the '''+ col.RE + '''_1_''' + col.DC + '.' + col.E

lvl_2_diff_1_scene_1=col.DC + '''Thunder rumbles in the sky and you know rain
will fall soon, you must find shelter. You remember a cave, and you know it
is west of your current location. A sliver of the sun still shines to your
right, though as you look, it dips below the horizon.

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RE + ' _1_' + col.DC + '.' + col.E

lvl_2_diff_1_scene_2=col.DC + '''

5 minutes into your walk towards the cave heavy rain starts to fall.
You think you hear a noise behind you, when you turn around you see
''' + col.RE + 'A WILD BEAR CHARGING AT YOU!' +col.DC + '''

You need to make a split decision,
''' + col.GR + 'stand your ground and use your knife (fight) ' + col.DC + '''
or''' + col.GR + ''' Run like hell (flee)
You choose to ''' + col.RE + '_2_' + col.DC + '''.
''' + col.E

lvl_2_diff_1_scene_3=col.DC + '''

You escape the bear and run through the forest, by the time you reach the cave
it's like super dark out. Near the entrance of the cave you find some dead
twigs. Once in the cave you use the ''' + col.RE + '_3_' + col.DC + ''' from
your ''' + col.YE + 'backpack' + col.DC + ''' to light the twigs on fire.
''' + col.E

lvl_2_diff_1_scene_4=col.DC + '''

The twigs are wet, and you need to use the ''' + col.RE +  '_4_' + col.DC + ' from your ' + col.YE + 'Backpack' + col.DC + ''' as kindling to get the fire going,
nice and toasty!

''' + col.E

lvl_2_diff_2_scene_1=col.DC + '''Thunder rumbles in the sky and you know rain
will fall soon, you must find shelter. You think there is a cave somwhere,
and you think it is west of your current location. As you try to get your
bearings from the sun you trip, fall and hit your head. You awake later, it
is pitch black, you don't know which way the cave is.

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RE + ''' _1_''' + col.DC + '''.
''' + col.E

lvl_2_diff_2_scene_2=col.DC + '''

When you awoke the second time rain was already falling and...
OH SHIT! ''' + col.RE + 'A WILD BEAR IS CHARGING AT YOU!' +col.DC + '''

You need to make a split decision,
''' + col.GR + 'stand your ground and use your knife (fight) ' + col.DC + '''
or''' + col.GR + ''' Run like hell (flee)
You choose to ''' + col.RE + '_2_' + col.DC + '.' + col.E + '''
''' + col.E

lvl_2_diff_2_scene_3=col.DC + '''

You escape the bear and run through the forest, You trip and fall so much
because it's like super dark out, you're like 27.3 percent hurt... Pretty bad
Near the entrance of the cave you dont find any wood to burn, but you find a
significant amount of bat guano. Once in the cave you use the
''' + col.RE + '_3_' + col.DC + ' from your ' + col.YE + '''backpack
''' + col.DC + ''' to light the guano on fire.
You're about to have a terrbile fire... Just vile.
''' + col.E

lvl_2_diff_2_scene_4=col.DC + '''

The guano is wet, and just like super gross, and you need to use the
''' + col.RE +  '_4_' + col.DC + ' from your ' + col.YE + '''Backpack
''' + col.DC + ''' as kindling to get the fire going,
Great! So enjoy the bat shit campfire...

''' + col.E

lvl_2_diff_3_scene_1=col.DC + '''Rain starts to fall on you out of nowhere
and it's a huge amount of rain. You think there is a cave somwhere, but you
honestly can't remember where it was. As you try to get your bearings from
the sun you trip, fall and hit your head. You awake later, it is pitch black,
you don't know which way the cave is. You realize some sort of animal has
eaten like... 67.2 percent of your left leg... soooo... Not great really...

You can go left, right, forwards or backwards to find the cave.
You choose to go''' + col.RE + ''' _1_''' + col.DC + '''.
''' + col.E

lvl_2_diff_3_scene_2=col.DC + '''

You're wet and partially legless
OH SHIT! ''' + col.RE + 'A WILD BEAR IS CHARGING AT YOU!' +col.DC + '''

You need to make a split decision,
''' + col.GR + 'stand your ground and use your knife (fight) ' + col.DC + '''
or''' + col.GR + ''' Run like hell (flee)
You choose to ''' + col.RE + '_2_' + col.DC + '.' + col.DC + '''
But either way... I bet you loose a hand.''' + col.E

lvl_2_diff_3_scene_3=col.DC + '''

You escape the bear and hobble through the forest, You trip and fall so much
because it's like super dark out, you're like 86.3 percent hurt...so bad.
I was right, you totally lost a hand back there with the bear, there was a
lot of blood. You fall into a hole and you can't really get out, so you just
stay there. Once in the hole you have to make a fire out of something, so use
your socks I guess... Gross. You use the ''' + col.RE + '_3_' + col.DC + '''
 from your ''' + col.YE + 'backpack' + col.DC + ''' to light the socks on fire.
You're about to have a terrbile fire... Just vile.
''' + col.E

lvl_2_diff_3_scene_4=col.DC + '''

The socks are wet, and just like so gross, and you need to use the
''' + col.RE +  '_4_' + col.DC + ' from your ' + col.YE + '''Backpack
''' + col.DC + ''' as kindling to get the fire going,
Great! So enjoy the dirty socks campfire...

''' + col.E

lvl_3_diff_1_scene_1=col.DC + '''Your eyelids grow heavy and you finally
begin to grow tired by the fire, before you fall asleep you eat the
''' + col.RE + '_1_' + col.DC + ' from your ' + col.YE + 'backpack' + col.E

lvl_3_diff_1_scene_2=col.DC + '''You settle in for the night and decide that
because you don't know who or what may lurk nearby, it's probably safest to
sleep with the ''' + col.RE + '_2_' + col.DC + ''' from your
''' + col.YE + 'backpack' + col.DC + ' closest to you, just in case.' + col.E

lvl_3_diff_1_scene_3=col.DC + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. You open your eyes to see the entrance
of the cave filling in with rocks and debris... 'It must be a mudslide' you
think. You realize you'll either have to clear the rocks and debris in the
morning (later), or try to dig a whole through the muddy rocks while it's
wet (now). You choose to do it ''' + col.RE + '_3_' + col.DC + '.' + col.E

lvl_3_diff_1_scene_4=col.DC + '''Morning finally comes and you climb out the
small hole you made the night before into the sunlight. You know if you walk
North you will eventually reach the highway, and someone who can help you.
The sun rises to your right, you know this means you must go
(left, right forward or back) ''' + col.RE + '_4_' + col.DC + '.' + col.E

lvl_3_diff_2_scene_1=col.DC + '''Your eyelids grow heavy and you finally
begin to grow tired by the fire, before you fall asleep you eat the
''' +col.RE + '_1_' + col.DC + ' from your ' + col.YE + 'backpack' + col.E

lvl_3_diff_2_scene_2=col.DC + '''You settle in for the night and decide that
because you don't know who or what may lurk nearby, it's probably safest to
sleep with the ''' + col.RE + '_2_' + col.DC + ''' from your
''' + col.YE + 'backpack' + col.DC + ' closest to you, just in case.' + col.E

lvl_3_diff_2_scene_3=col.DC + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to
be drowning in a puddle. You realize you'll either have to clear the debris
and try to empty out the water. You can do it in the morning (later), or try
to dig a whole through the muddy rocks while it's wet (now). You choose to do
it ''' + col.RE + '_3_' + col.DC + '.' + col.DC + ''' You use your one
existing hand to fling the water out of the hole.
It sucks and you're bleeding a bunch''' + col.E

lvl_3_diff_2_scene_4=col.DC + '''Morning finally comes and you climb out the
small hole you made the night before into the sunlight. You know if you walk
north you will eventually reach the highway, and someone who can help you.
The sun rises to your right, you know this means you must go
(left, right forward or back) ''' + col.RE + '_4_' + col.DC + '.' + col.E

lvl_3_diff_3_scene_1=col.DC + '''Your eyelids grow heavy and you finally
begin to grow tired by the fire, before you fall asleep you eat the
''' +col.RE + '_1_' + col.DC + ' from your ' + col.YE + 'backpack' + col.E

lvl_3_diff_3_scene_2=col.DC + '''You settle in for the night and decide that
because you don't know who or what may lurk nearby, it's probably safest to
sleep with the ''' + col.RE + '_2_' + col.DC + ' from your ' + col.YE + '''
backpack''' + col.DC + ' closest to you, just in case.' + col.E

lvl_3_diff_3_scene_3=col.DC + '''zzz...
zzz...
zzz...
zzz...

While sleeping you hear a loud bang. The hole has caved in and you appear to
be drowning in a puddle. You realize you'll either have to clear the debris
and try to empty out the water. You can do it in the morning (later), or try
to dig a whole through the muddy rocks while it's wet (now). You choose to
do it ''' + col.RE + '_3_' + col.DC + '.' + col.DC + ''' You use your one
existing hand to fling the water out of the hole. It sucks and you're
bleeding a bunch''' + col.E

lvl_3_diff_3_scene_4=col.DC + '''Morning finally comes and you climb out the
small hole you made the night before into the sunlight. You know if you walk
North you will eventually reach the highway, and someone who can help you.
You will most certainly die today. The sun rises to your right, you know
this means you must go
(left, right forward or back) ''' + col.RE + '_4_' + col.DC + '''. You try to
go towards the highway, but obviously you don't make it and you die''' + col.E


def difficulty(user_input):
    # prompts user to choose difficulty and returns an int
    user_input = raw_input('''Please choose a difficulty by typing easy,
medium or hard below:
''')

    if user_input == 'easy':
        return 1
    if user_input == 'medium':
        return 2
    if user_input == 'hard':
        return 3


def set_count(user_input):
    '''
    prompts user to select the number of guesses they may have and returns
    that int
    '''
    user_input=raw_input('''Please type a number between 1 and 10 to select
the number of guesses you will have to answer questions:
''')
    return user_input


def diff_scene(level, diff, scene):
    # supplies scene string based on level, difficulty and scene
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


def chances(count):
    # takes count as input and returns number of chances left as string
    return col.RE + 'You have ' + str(count) + ' chances remaining' + col.E


def item_in_scene(scene, replacement_items):
    # checks if replacement item exists in a scene and returns the pos
    for pos in replacement_items:
        if pos in scene:
            return pos
    return None


def check(level, answer, scene):
    # checks answer based on level and scene
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


def run_adventure(level, count, diff, scene_num, rep):
    '''
    Brings together all the functions and strings to play the game
    Takes as input the level, amount of guesses, difficulty, scene number and
    a replacement string(or none if not available) then outputs the game
    '''
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
                user_input = raw_input(fill + replacement + colon)
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
                print col.RE + 'You loose, how unfortunate!'
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
                print col.RE + 'you win, game over man'
                break
            break
        break



print welcome
run_adventure(1, int(set_count(raw_input)), difficulty(raw_input), 1, None)

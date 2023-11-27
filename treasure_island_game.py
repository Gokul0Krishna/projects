print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')
print("welcome to treasure island the game")
print("you are on a mission to find the treasure on this island")
print("each decision you make will affect the outcome of your quest")
print("your you begins form here......")
print('''                                                  .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')
print("you have washed ashore on an island,How do you wish to proceed")
print("have two options either to explore or to stay put\n")
pos=input()
pos.lower()
if pos== 'stay':
    print("you chose to stay where you are and wait for help")
    print('but no one came for help and you perished due to exhaustion ')
    print('''         _\<
                 (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((//
                             -  \)''')
    exit()
else:
    print("so you have chosen to explore")
    print("to your left there is lake that you must swim across and to your right there is a thick forest")
    print("you have to options to choose form")
    print("go right or go left")
    dir=input()
    dir.lower()
    if dir=="go right" :
        print("You find that the forest is getting thicker as you proceed")
        print("With how thick the roots are on the ground you can't make out whether your stepping on the ground") 
        print("As you are lost in thought, you don't pay attention to where you palce your foot")
        print("the next thing you know you,you find your self in a hole injured and with no one to help you,you are left to die")
        print('''         _\<
                 (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((//
                             -  \) ''')  
        exit()   
    else:
        print("you find your self swiming in a bottom less lake")
        print("as you reach the half waypoint of the river you come across a floating plank")
        print("you grab onto it and rest for sometime to catch you breath")
        print("now you have two options to choose form")
        print("to stay or to swim")
        liv=input()
        live=liv.lower()
        if live=='stay':
          print("as you stay put at one place unaware of the danger lie beneth")
          print("you are attacked by trout")
          print("whit nothing you can do and no where you can go you accept your fate")
          print('''  (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((// ''')
        else:
          print("as make it on to the shore with the last of your energy")
          print("you find an old abandoned structue, but a stuctre ")
          print("on furthur examining the stucture you find this to be a temple of sorts")
          print("temples being a place to store treasure,you get your hopes up and enter the temple")
          print("as you enter the temple you see 3 doors")
          print("print now you are presented with 3 options")
          print("to enter the 'left door','the middle door','the right door'")
          doo=input()
          door=doo.lower()
          if door=="left door":
            print("as you enter the door you fall in to a pit of fire unable to escape you perish")
            print('''   (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((// ''')
          elif door=="middle door" :
             print("you eneter a dim light room with a chest cover in dust and cobwebs")
             print("you open the chest to find it coverd in gold ") 
             print("you win") 
          else:
             print("as you enter the room to find it filled with beasts that have taken recedence there")
             print("unable to escape to defend your self you perish")
             print('''   (   >
                 __)(
           _____/  //   ___
          /        \\  /  \\__
          |  _     //  \     ||
          | | \    \\  / _   ||
          | |  |    \\/ | \  ||
          | |_/     |/  |  | ||
          | | \     /|  |_/  ||
          | |  \    \|  |     >_ )
          | |   \. _|\  |    < _|=
          |          /_.| .  \/
  *       | *   **  / * **  |\)/)    **
   \))ejm97/.,(//,,..,,\||(,wo,\ ).((// ''')          
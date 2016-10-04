items = []
money = 0

def start():
    print "Welcome to The Dream Portal."
    global player
    player = raw_input ("I'm Lucy and I'll be your guide. What is your name? : ") #2. Assign a string to a variable
    print""
    print "It's very nice to meet you "+ player.capitalize() +"!" #4. Use the print function and .format() notation to print out the variable you assigned
    print "You'll have to make some very important choices, but I will be here to guide you along the way."
    remember()


def remember():
    choice1 = raw_input ("Do you often remember your dreams? (yes or no?) ")

    if choice1 == "yes": #7. Use of conditional statements: if, elif, else
        print""
        print "That's great "+player+", you'll do fantastic in The Dream Portal!"
        entrance()

    elif choice1 == "no": #7. Use of conditional statements: if, elif, else
        print""
        print "I see. Well I hope you will remember your time here in the The Dream Portal."
        entrance()

    else: #7. Use of conditional statements: if, elif, else
        print""
        print "I'm sorry, I couldn't hear you."
        remember()

def entrance():
    print "Follow me to the supply room so we can get you everything you need."
    hat()

def hat():
    choice2 = raw_input ("Here's a satchel to hold your tools. Do you prefer to use the red flying hat or the blue vanishing hat? (red or blue?) ")

    if choice2 == "red":
        print""
        print "Great choice, you will be able to fly when you wear it, but you can only use it once."
        items.append("red hat")
        amulet()

    elif choice2 == "blue":
        print""
        print "Awesome, please try it on and look in the mirror! Can't see yourself at all?"
        print "That blue hat makes you vanish from sight for 10 seconds. It might come in handy, but you can only use it once."
        items.append("blue hat")
        amulet()

    else:
        print""
        print "I'm sorry, I couldn't hear you."
        hat()

def amulet():
    print "Now you need to choose two amulets to help you. The amulets are based on the elements and they can only be used once. You can choose from fire, water, wind or earth."
    choice3 = raw_input ("Which is your first choice? (fire, water, wind or earth?) ")

    if choice3 == "fire":
        items.append("fire")
        print ""
        gotfire()

    elif choice3 == "water":
        items.append("water")
        print""
        gotwater()

    elif choice3 == "wind":
        items.append("wind")
        print""
        gotwind()

    elif choice3 == "earth":
        items.append("earth")
        print""
        gotearth()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        amulet()

def gotfire():
    choicefire = raw_input ("Now that you have fire, what other element do you want? (water, wind or earth?) ")

    if choicefire == "water":
        items.append("water")
        leavesupply()

    elif choicefire == "wind":
        items.append("wind")
        leavesupply()

    elif choicefire == "earth":
        items.append("earth")
        leavesupply()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        gotfire()

def gotwater():
    choicewater = raw_input ("Now that you have water, what other element do you want? (fire, wind or earth?) ")

    if choicewater == "fire":
        items.append("fire")
        leavesupply()

    elif choicewater == "wind":
        items.append("wind")
        leavesupply()

    elif choicewater == "earth":
        items.append("earth")
        leavesupply()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        gotwater()


def gotwind():
    choicewind = raw_input ("Now that you have wind, what other element do you want? (fire, water, or earth?) ")

    if choicewind == "water":
        items.append("water")
        leavesupply()

    elif choicewind == "fire":
        items.append("fire")
        leavesupply()

    elif choicewind == "earth":
        items.append("earth")
        leavesupply()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        gotwind()
        
def gotearth():
    choiceearth = raw_input ("Now that you have earth, what other element do you want? (fire, water, or wind?) ")

    if choiceearth == "water":
        items.append("water")
        leavesupply() #13. Call the function you defined above and print the result to the shell

    elif choiceearth == "wind":
        items.append("wind")
        leavesupply() 

    elif choiceearth == "fire":
        items.append("fire")
        leavesupply()



def leavesupply(): #12. Defining a function that returns a string variable
    print ""
    print "You have these items in your satchel:" + " " + items[0] + " + " + items[1] + " amulet + " + items[2] + " amulet."
    print "Now you can be on your way. Let's walk into the forest."
    journey()

def journey():
    global money
    print ""
    print "Suddenly a horse appears and it asks you if you have an amulet that can fix it's horn?"
    choicehorse = raw_input ("Lucy says maybe you can try the " + items[1] + " amulet or " + items[2] + " amulet? (" + items[1] + " or " + items[2] + "?)")

    if choicehorse == items[1]:
        print""
        print "Thank you! That did fix my horn. As you can see, I'm a Unicorn, so for helping me I would like to give you 10 coins."
        print ("You have used " + items[1] + ".")
        money = money + 10 #1. Assign an integer to a variable 5. Use each of these operators +
        items.remove(items[1])
        path()

    elif choicehorse == items[2]:
        print ""
        print "That didn't work. The horse is sorry you had to use your amulet, so he gives you 2 and a half coins to thank you for trying."
        print ("You have used " + items[2] + ".")
        money = money + 2.5 #3. Assign a float to a variable
        items.remove(items[2])
        path()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        journey()

def path():
    global money
    print ""
    print "There is a giant spider blocking our path. How will we get past it? Lucy says you can use the " + items[0] + "."
    print ""
    choicespider = raw_input ("Would you like to use it? (yes or no?)")

    if choicespider == "yes" and items[0] == "red hat": #Use of logical operators and
        print ""
        print "It's working, we're flying right over the spider! You find 3 coins floating in the clouds."
        items.remove(items[0])
        money += 3 #5. Use each of these operators +=
        print "You now have " + str(money) + " coins."
        river()
       
    elif choicespider == "yes" and items[0] == "blue hat":
        print ""
        print "It's working, we can sneak by the spider without it even seeing us! You find 6.5 coins on the ground."
        items.remove(items[0])
        money += 6.5
        print "You now have " + str(money) + " coins."
        river()

    elif choicespider == "no" and items[0] == "red hat":
        print ""
        print "The spider sees you and is so happy to have a vistor he triples your coins."
        money = money * 3 #5. Use each of these operators *
        print "You now have " + str(money) + " coins."
        river()

    elif choicespider == "no" and items[0] == "blue hat":
        print ""
        print "The spider sees you and is so happy to have a vistor he quadruples your coins."
        money = money * 4
        print "You now have " + str(money) + " coins." 
        river()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        path()

def river():
    global money
    print""
    print "That's a big river we need to cross. Luckily for us there's a ferry to cross it. It costs 1 coin to take the ferry."
    money -= 1 #5. Use each of these operators -=
    print "You now have " + str(money) + " coins."
    choicesleep = raw_input ("You are feeling sleepy. Would you like to take a nap? (yes or no?)")

    if choicesleep == "no":
        rocket()

    if choicesleep == "yes":
        nap()

def rocket():
    global money
    print ""
    print "On the other side of the river is a space rocket. It's about to take off!"
    countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] #10. Creating a list and iterate through that list using a for loop to print each item out on a new line
    for x in countdown: #9. Use of a for loop
        print (x)
    print "Blast off!"

    print "There is another rocket and this one is landing. It needs your help to land. Instead of counting down, we need to count up."
    countup = 1
    while (countup < 11): #8. Use of a while loop
       print countup
       countup = countup + 1
    print "The rocket landed! An astronaut climbs out and wants to share his space treasure with you. He triples your coins."
    money = money * 3
    print "You now have " + str(money) + " coins." 
    cafe()

def nap():
    global money
    print ""
    print "There's a nice patch of grass that looks perfect for sleeping, so you take a quick nap."
    print "A lion wakes you up and asks you to play a game."
    choicelion = int(raw_input("Pick any number from 1 to 99."))

    if choicelion == 2 or choicelion == 4: #6. Use of logical operators or
       print "" 
       print "You guessed it! That's amazing. The lion increases your coins by an order of magnitude!"
       money = money * 10
       print "You now have " + str(money) + " coins." 
       cafe()

    elif choicelion == 1 or choicelion == 3:
       print ""
       print "That was not correct, but you were close. The lion quadruples your coins."
       money = money * 4
       print "You now have " + str(money) + " coins."
       cafe()

    elif choicelion >= 5 and choicelion <= 99:
       print ""
       print "That was not correct, but the lion thanks you for playing by doubling your coins."
       money = money * 2
       print "You now have " + str(money) + " coins."
       cafe()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        nap()

def cafe():
    global money
    print ""
    print "Moving along, you arrive at a cafe and a bear asks to take your order. You look at the menu and see:"
    food = ('pizza', 'waffle', 'burrito', 'smoothie', 'sushi')
    for x in food: #11. Create a tuple and iterate through it using a for loop to print each item out on a new line print x
        print x

    choicemeal = raw_input("Which do you order?")

    if choicemeal == 'pizza' or choicemeal == 'waffle' or choicemeal == 'burrito' or choicemeal =='smoothie':
        print ""
        print "Great choice! That cost half of your coins."
        money = money / 2 #5. Use each of these operators /
        print "You now have " + str(money) + " coins."
        home()

    elif choicemeal == 'sushi':
        print ""
        print "Sushi is expensive, that cost you all of your coins that can be put in groups of 5."
        money = money % 5 #5. Use each of these operators %
        print "You now have " + str(money) + " coins."
        home()

    else:
        print ""
        print "I'm sorry, I couldn't hear you."
        cafe()
       
def home():
    global money
    print ""
    print "Now it's time to go home. It costs 2 coins to get home through The Dream Portal. Do you have enough?"
    print "You have " + str(money) + " coins."

    if money >= 2:
        win()

    else:
        lose = (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.50, 1.75)
        not (money != lose) #6. Use of logical operators not
        lost()

def win():
    print "You have enough to get home! Congratulations! you had a successful journey!"
    print "You will live happily ever after. The End"

def lost():
    global money
    print "Sorry, you do not have enough to get home. Try again and maybe you will be able to leave The Dream Portal."
    money = 0
    entrance()
    

start()


# Imports the time, math, random module and the playsound package
import time
import math
import random
from playsound import playsound 
import sys
# I was going to use the sys module to resize the terminal, but I will just add in the README.md to play in fullscreen mode
#import sys
#sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=200, cols=350))

# Function to "Type" out the string, so that it doesn't print the string out at once, but sort of 
def type(string):
    for char in string:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

section = "A" 

# List randomizers for all the different correct, incorrect and splash audio files
correctSound = ["Audio/correctAnswer1.mp3", "Audio/correctAnswer2.mp3", "Audio/correctAnswer3.wav", "Audio/correctAnswer4.wav"]
incorrectSound = ["Audio/wrongAnswer1.wav", "Audio/wrongAnswer2.wav", "Audio/wrongAnswer3.wav", "Audio/wrongAnswer4.wav"]
splashSound = ["Audio/splash1.wav", "Audio/splash2.wav", "Audio/splash3.wav"]

# Welcome Screen
def welcomeScreen():
    # Y9 Design - Welcome Screen Part 1
    print("""\033[1m
         __      __ ______         _______                    __                   
        /  \    /  /      \       /       \                  /  |                  
        $$  \  /$$/$$$$$$  |      $$$$$$$  | ______   _______$$/  ______  _______  
         $$  \/$$/$$ \__$$ |      $$ |  $$ |/      \ /       /  |/      \/       \ 
          $$  $$/ $$    $$ |      $$ |  $$ /$$$$$$  /$$$$$$$/$$ /$$$$$$  $$$$$$$  |
           $$$$/   $$$$$$$ |      $$ |  $$ $$    $$ $$      \$$ $$ |  $$ $$ |  $$ |
            $$ |  /  \__$$ |      $$ |__$$ $$$$$$$$/ $$$$$$  $$ $$ \__$$ $$ |  $$ |
            $$ |  $$    $$/       $$    $$/$$       /     $$/$$ $$    $$ $$ |  $$ |
            $$/    $$$$$$/        $$$$$$$/  $$$$$$$/$$$$$$$/ $$/ $$$$$$$ $$/   $$/ 
                                                                /  \__$$ |         
                                                                $$    $$/          
                                                                $$$$$$/           
    """) 

    time.sleep(1) # Wait 1 seconds
    # Barrier to split in between different print commands to make it look more organized and simple
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(1)  # Wait 1 seconds

    # Welcome to Jabari Jumps - Welcome Screen Part 2
    print("""\033[1m
                 __        __   _                            _                     
                 \ \      / ___| | ___ ___  _ __ ___   ___  | |_ ___               
                  \ \ /\ / / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \              
                   \ V  V |  __| | (_| (_) | | | | | |  __/ | || (_) |             
                    \__\_/ \___|_|\___\___/|_| __| |_|\___|  \__\___/    
                                                                            
                | | __ _| |__   __ _ _ __(_)     | |_   _ _ __ ___  _ __  ___ 
             __ | |/ _` | '_ \ / _` | '__| |  _  | | | | | '_ ` _ \| '_ \/ __|
            | |_| | (_| | |_) | (_| | |  | | | |_| | |_| | | | | | | |_)\__ \ 
             \___/ \__,_|_.__/ \__,_|_|  |_|  \___/ \__,_|_| |_| |_|__/|___/ 
                                                                   |_| 
    """)

    time.sleep(1) # Wait 1 seconds
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m") 
    time.sleep(1) # Wait 1 seconds

# Transition screen between sections
def transitionScreen(): 
    print("""   \033[1m                                                                 
     .                                                                     
    .?GJ:                                                                  
      !B&Y!~                                                               
       .Y@@&^                                                              
         ~G@BJ^                                                            
           ?&@&BY~                            .YP^                         
            ^G@&&&G^                          P@B!:                        
             .Y&&&&#^                         G&G!                         
               !&&&&P                         5@7                          
                Y@&&&P7:                     :#@J                          
                .P@&&&&#P7:                  ?&&5                          
                  ?#&&&&&&#Y:               .B&&5                          
                   ^P&&&&&&&#Y7~^.           G&&Y                          
                     J&&&&&&&&&&&#5:         !&&&!  .JB!                   
                      !#&&&&&&&&&&@B:         P&&#^^#@&!   .               
                       :P&&&&&&&&&&&P.        :#&&BG&#Y:.?GBBP?:           
                         ?#&&&&&&&&&&G!^:^^~7?Y#&&&&&! .P@&&&&@#7          
                          :YB&&&&&&&&&&&#&&&&&&&&&&&&#G#&&&&&&&@7          
                            .~JP#&&&&&&&&&&&&&&&&&&&&&&&&&&&&@B!           
                                .^7YG#&&&&&&&&&&&&&BJ~::?##G55~            
                                     .^!J5G#&&&#GJ~      .:                
                                           :~!~:                           
                                                                 
                                                                           
    \033[36m                                                                       
       ..^!J?~:.         :!~.           .:^!?YGGY??7!!!!!!7JYPPJ!^:...     
    :7JY5PB@@&&#GGP555555#@@#GP5YJJJJYYJ??J5PGB#&P??JYYYJ??Y#&&#B5J7!^.    
     .^!JPB##BBGPPYJ?!^:.~!7!!!!!~^^:..        .^!!:       ^~^:.           
      .:::....                     .  .....                                
                                . ..    ...    
\033[0m                            
""")
    playsound(random.choice(splashSound)) # Plays random splash sound ... etc

# Game Instructions & Information about Section A
def sectionAInfo(): 
    global section
    type("\033[1mWelcome to Jabari Jumps Text-Based Game! \033[0m\nThis game will fun and engaging while testing your knowledge on Jabari Jumps!")
    type("\n\033[2m\nBy: Zeen Liu.\n\033[0m")
    time.sleep(3)
    type("\n\033[1mInstructions:\033[0m")
    type("\n\n    * Prerequisites - Found in 'README.md', Make sure you've read it!")
    type("\n    * Section A - Basic Comprehension.")
    type("\n    * Section B - Reflective Questions.")
    type("\n    * Section C - Vocabulary Review.")
    type("\n    * This game is designed to be under 20 minutes of total playtime.")
    type("\n    * There will be multiple choice + short answer questions. ")
    type("\n    * There are wait times during the code, so don't type in anything before it tells you that you can.")
    type("\n    * If you enter something before the wait time is over, you risk crashing the game. ")
    type("\n    * Also, accurate is spelling is important. Sometimes if you miss a letter in a word, the filter will count it as incorrect.")
    time.sleep(10)
    type("\n\nSection A will only be Multiple-Choice questions.")
    type("\nIt is your only chance to earn coins and spend it on hints & boosters later, so make sure to think about the questions carefully!")
    time.sleep(4)
    type("\033[1m\n\nReward System: \033[0m") 
    type("\n\n    * 1 coin for each first-try correct answer.")
    type("\n    * No coins deducted for wrong answer.")
    time.sleep(4) 
    section = "A"
    startConfirmation()

# Game Start Confirmation
def startConfirmation():
    gameStart = False
    while gameStart == False:
        type("\033[1m\n\nType in 'ok' when you've read through all the instructions.\n\033[0m")
        start = input("\n")
        if start.lower() == "ok":
            type("\033[2m\nAlright, let's proceed to Section " + section + ".\n\n\033[0m")
            gameStart = True
            time.sleep(2)
            transitionScreen()
            time.sleep(1)
        else:
            type("\nNot ready? You got this! Try again.\n")
            time.sleep(1)

# Section A Data Set
dataA = {
    "questions": [
        "Question 1: Based on the title page, what do you think this story is about?",
        "Question 2: Just by looking at the pictures, how do you think Jabari feels?",
        "Question 3: How did the author describe the diving board?",
        "Question 4: At first, was Jabari afraid to jump?",
        "Question 5: Why was Jabari confident in diving?",
        "Question 6: When the other kids took turns to dive, did it seem hard for Jabari?",
        "Question 7: When Jabari's dad squeezes his hand, why does he squeeze back?",
        "Question 8: SPLASH! Jabari is next in line to dive. What does he do?",
        "Question 9: Why does Jabari do this?",
        "Question 10: When it is Jabari's turn again, why can't he climb the ladder?",
        "Question 11: Who gives Jabari advice?",
        "Question 12: Jabari then realized that he forgot to do something. What did he forget?",
        "Question 13: What does Jabari's dad tell him to do when he feels scared?",
        "Question 14: Did Jabari finally decide to climb the ladder?",
        "Question 15: Why does Jabari suddenly feel ready to dive?",
        "Question 16: SPLASH! How did it go? How did Jabari feel about it afterwards?"
        ],
    "answers": [
        ["A. Jabari is dreaming about becoming a diver.","B. Jabari is going to swim in a pool with his friends.","C. Jabari is about to dive off a swimming board."],
        ["A. Nervous.", "B. Confident.", "C. Happy."],
        ["A. White.", "B. High.", "C. Funny."],
        ["A. Yes", "B. No"],
        ["A. He passed his swim test.", "B. He took diving lessons.", "C. He ate a good breakfast."],
        ["A. Yes, it seemed impossible to do such a dive.", "B. No, it looked like a piece of cake."],
        ["A. He likes squeezing his dad's hands.", "B. It makes him calmer.", "C. He feels cool when he squeezes his dad's hands."],
        ["A. He stares at the sky and doesn't move.", "B. He climbs up the ladder to dive.", "C. He tells the kid behind in line to go before him."],
        ["A. Because he is too scared and doesn't want to dive.", "B. Because he is being nice and kind to the person behind him.", "C. Because he needs to think about his special jump."],
        ["A. He is too excited.", "B. He is too tired.", "C. He is too nervous."],
        ["A. His sister.", "B. His dad.", "C. Nobody."],
        ["A. He forgot to stretch.", "B. He forgot to wear his goggles."],
        ["A. Think about the worst that could happen.", "B. Do nothing and hope for the beast.", "C. Take a deep breath and tell himself that he is ready."],
        ["A. Yes, he listens to his dad's advice and feels ready.", "B. No, he decides to dive on another day."],
        ["A. He realized that he is a good diver and isn't scared anymore.", "B. He thought the dive would be a surprise, and he loved surprises."],
        ["A. Jabari is relieved and loved the surprise.", "B. Jabari is happy that he managed to dive.", "C. Jabari is already excited to dive again."]
        ],
    "answer": [
        "c", "a", "b", "b", "a", "b", "b", "c", "c", "b", "b", "a", "c", "a", "b", ["a", "b", "c"]
        ]
}

# Section A - Comprehension Questions
def sectionA(): 
    global coins
    coins = 0
    time.sleep(1)
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(1)
    for question in range(len(dataA["questions"])):
        print("\033[1m\n" + dataA["questions"][question]+"\n\033[0m") # Displays the question
        time.sleep(3)
        for multipleChoice in dataA["answers"][question]: # Displays the multiple choice options
            print(multipleChoice)
            correct = False
            firstTry = True
        while correct == False: 
            userAnswer = input("\033[1m\nYour answer: \033[0m") # Asks the user for their answer
            if type(dataA["answer"][question]) is str:
                if userAnswer.lower() == dataA["answer"][question]: # Checks if the answer is right
                    print("Congrats! This is the right answer. ")
                    correct = True
                    if firstTry == True: # Gives the user 1 coin if they get it first try
                        coins += 1
                        print("You gain 1 coin for getting it first try! ")
                    else:
                        coins += 0
                    playsound(random.choice(correctSound)) # Plays random correct sound ... etc
            elif type(dataA["answer"][question]) is list: # Checks if the answer is right
                if userAnswer.lower() in dataA["answer"][question]:
                    print("Congrats! This is the right answer. ")
                    correct = True
                    if firstTry == True: # Gives the user 1 coin if they get it first try
                        coins += 1
                        print("You gain 1 coin for getting it first try! ")
                    else:
                        coins += 0
                    playsound(random.choice(correctSound))
                else:
                    print("Please try again.")
                    playsound(random.choice(incorrectSound)) # Plays random incorrect sound ... etc
                    firstTry = False
        print(f'\033[2m\n  * Coin Balance: {coins} \n\033[0m')

# Information about Section B
def sectionBInfo():
    global section
    type("\033[1mNow, we will be moving onto Section B.\n\033[0m")
    time.sleep(2)
    type("\n    * This section will ask you harder, open-ended and reflective questions.")
    type("\n    * As well, you will be introduced to a new concept - United Nations Sustainability Development Goals (UN SDGs).")
    type("\n    * Essentially, they are goals in order to improve the world that we live in!")
    type("\n    * Don't worry if you feel challenged! This section is designed for you to learh abstract concepts about the UN SDGs.")
    type("\n    * We will go step-by-step through the process together.")
    time.sleep(8)
    type("\n\nSection B will have a combination of Multiple-Choice questions as well as Open-Ended questions.")
    type("\nMake sure to pay special attention to all the terms that are introduced, as Section C will test you later on them! ")
    time.sleep(4)
    section = "B"
    startConfirmation()

# Section B Data Set: Questions, Answers, Correct Answer, Question Type
dataB = {
    "questions": [
        "As you read through the story, you probably noticed that even though Jabari seemed to be excited at first to dive, when it was actually his turn, he seemed very nervous.",
        "1. Let's Recall: By the end of the book, was Jabari able to dive?",
        "That's right! Jabari built up the courage to make his first ever dive. You might have noticed that after his first dive, he immediately wanted to dive again. This happens often after a 'First Experience'.",
        "2. Reflect back. Why do you think 'First Experiences' are so important in controlling fears?",
        "3. Let's also think back on what we just learned. How do you think Jabari overcame his fear of diving?",
        "4. Now, take a moment to think of a time you controlled a fear. What was the fear?",
        "5. How did you control this fear from scaring or bothering you? How did you overcome it?",
        "6. Did anyone help you defeat the fear. Do you still have this fear today?",
        "7. Now, let's think back on Jabari's fear of diving. Do you think that Jabari will still be scared the next time he dives?",
        "Both are correct! Jabari might still be scared but will definitely be less scared but will definitely be less scared than his first experience because he learned from the challenge and this increased his ability to control his fear of diving. This is called a 'Growth Mindset'.",
        "8. Reflect back. Why do you think a 'Growth Mindset' is important to overcome fears?",
        "9. Conclusion: Apply the knowledge of a growth mindset and first experiences. Explain how they can help you overcome your fears in the future.",
        "10. Now, let's focus on the bigger picture - United Nations Sustainability Development Goals (UNSDG). These are the foundation to build a better society. \nDo you think every child can be like Jabari and have a swimming pool to dive in?",
        "Excellent thinking! Unfortunately, not every city in the world can afford good infrastructure - the foundation and the structure of our city. An example of infrastructure would be public pools.",
        "11. Which of these do you think is part of a city's infrastructure?",
        "12. Why do you think infrastructure is important for a city?",
        "13. Now think about how much water a pool needs to function. Do you think all cities can afford these public pools?",
        "14. Why do you think some cities or countries don't have enough water?",
        "Exceptional thinking! While some cities have the money for pools, they might not have nearly enough water to sustain it."
        ],
    "answers": [
        [],
        ["A. No.", "B. Yes."],
        [],
        [],
        [],
        [],
        [],
        [],
        ["A. No.", "B. Yes."],
        [],
        [],
        [],
        ["A. No.", "B. Yes."],
        [],
        ["A. A road", "B. A library", "C. A school"],
        [],
        ["A. Yes.", "B. No."],
        [],
        []
        ],
    "answer": [
        "", "b", "", "", "", "", "", "", ["a","b"], "", "", "", "a", "", ["a", "b", "c"], "", "b", "", ""
        ],
    "type": [ # 'mc' = multiple choice, 'sa' = short answer, 'is' = info slide
        "is", "mc", "is", "sa", "sa", "sa", "sa", "sa", "mc", "is", "sa", "sa", "mc", "is", "mc", "sa", "mc", "sa", "is"
    ]   
} 

# Section B - Reflective Questions
def sectionB():
    global questionsB
    global answersB
    questionsB = []
    answersB = []
    time.sleep(1)
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(1)
    for question in range(len(dataB["questions"])):
        if dataB["type"][question] == "mc": # Checks if question is multiple choice
            print("\033[1m\n" + dataB["questions"][question]+"\n\033[0m")
            time.sleep(2)
            for multipleChoice in dataB["answers"][question]: # Prints multiple choice options
                print(multipleChoice)
            correct = False
            while correct == False: 
                # Asks user for their answer and checks if it is correct
                # Will loop if the user gives an invalid answer
                userAnswer = input("\033[1m\nYour answer: \033[0m") 
                if type(dataB["answer"][question]) is str:
                    if userAnswer.lower() == dataB["answer"][question]:
                        print("Congrats! This is the right answer. ")
                        playsound(random.choice(correctSound))
                        correct = True
                    else: 
                        print("Please try again.")
                        playsound(random.choice(incorrectSound))
                elif type(dataB["answer"][question]) is list:
                    if userAnswer.lower() in dataB["answer"][question]:
                        print("Congrats! This is the right answer. ")
                        playsound(random.choice(correctSound))
                        correct = True
                    else: 
                        print("Please try again.")
                        playsound(random.choice(incorrectSound))
        elif dataB["type"][question] == "sa": # Checks if the question is short answer
            time.sleep(2)
            shortAnswer = input("\033[1m\n" + dataB["questions"][question]+"\033[0m\033[1m\n\nYour answer: \033[0m") # Asks user for their answer
            # Saves the user's answer
            questionsB.append(dataB["questions"][question])
            answersB.append(shortAnswer)
            print("\nAnswer submitted!\n")
            playsound(random.choice(splashSound))
        elif dataB["type"][question] == "is": # Checks if the question is info slide
            time.sleep(2)
            print("\033[2m\033[1m\n" + dataB["questions"][question]+"\n\033[0m")
            time.sleep(5)
    print(f'\033[2m\n  * Coin Balance: {coins} \n\033[0m')
    time.sleep(5)

# Information about Section C
def sectionCInfo():
    global section
    type("\033[1m\nNow, we will be moving onto Section C.\n\033[0m")
    time.sleep(2)
    type("\n    * This section will be a vocabulary test to see what you've learned today!")
    type("\n    * You will have to write a correct meaning in your own words for each of words in the randomized list.")
    time.sleep(4)
    type("\033[1m\n\nOn each question can use your hard-earned coins to spend it on hints.\n\033[0m")
    type("\n    * 3 coins = 1 hint.")
    type("\n    * If you wish to use a hint for a word, simply type 'hint' in the answer prompt.\n")
    time.sleep(4)
    type("\nAfter you enter your answer, a system checks whether you have written the important keywords.")
    type("\nThe more keywords that match in your answer, the higher you climb on the ladder.")
    type("\nWhen writing your answer, DO NOT use commas, because it will break the filter.")
    time.sleep(4)
    type("\n            \033[1m\n   * The height is also affected by perks that you can buy with coins each turn.\033[0m\n")
    time.sleep(2)
    type("\n        \033[1m* Hint Perk:\033[0m")
    type("\n            * Cost - 1")
    type("\n            * Max Level - 3")
    type("\n            * Description - It costs less to purchase a hint and they deduct less height.")
    time.sleep(2)
    type("\033[1m\n\n        * Time Perk:\033[0m")
    type("\n            * Cost - 2")
    type("\n            * Max Level - 5")
    type("\n            * Description - Streaks of correct keywords give more height.")
    time.sleep(2)
    type("\033[1m\n\n        * Streak Perk:\033[0m")
    type("\n            * Cost - 2")
    type("\n            * Max Level - 5")
    type("\n            * Description - Longer time to answer a question deducts less height.")
    time.sleep(2)
    type("\033[1m\n\nIn the end, the total height that you have climbed will influence your performance score.\033[0m")
    time.sleep(4)
    section = "C"
    startConfirmation()

# Section C Data Set: Words, Hints, Keywords
dataC = { 
    "words": [
        "Growth Mindset", 
        "Infrastructure",
        "First Experience",
        "Fear",
        "UNSDG",
        "Foundation",
        "Sustainability",
        "Development",
    ], 
    "hint":[
        "Hint: Think back on how Jabari overcame his fear of diving. How did his mindset change and 'grow' after he jumped?",
        "Hint: Think of swimming pools, libraries, roads and schools. What do they have in common? How does this help with improving a city?",
        "Hint: Think of doing something for the first time. It can be scary, but it can also be relieving once you defeat that inner fear! How do First Experiences help overcoming a fear?",
        "Hint: Think of something that always scares you, like diving in Jabari's case. Give an example of one of your fears.",
        "Hint: Think of the goals that the United Nations came up with. What are they for and how will they help us?",
        "Hint: Think of the CN Tower. What are the downsides if the foundation is not wide enough? Would that make a stable or dangerous design?",
        "Hint: Think about the life cycle. What would happen if there wasn't enough food to sustain a certain species?",
        "Hint: Think of how our city is developing, as we sophisticate our technology and modern society."    
    ],
    "keywords":[
        ["better", "change", "changing", "overcome", "overcame", "growing", "grow", "dedication", "challenge", "challenges", "fear", "fears", "time", "effort"],
        ["swimming", "pool", "pools", "library", "libraries", "road", "roads", "improve", "improving", "city", "cities", "structure", "example", "foundation"],
        ["first", "time", "fear", "inner", "scary", "relief", "relieving", "defeat", "overcome", "defeating", "overcoming"],
        ["scary", "scared", "scares", "panic", "terror", "danger", "panicking", "experience"],
        ["united", "nations", "sustainability", "development", "goals", "better", "society", "build", "building", "foundation", "structure", "infrastrcture", "develop", "sustain"],
        ["building", "tower", "stable", "base", "sustain", "build", "structure", "hold", "strong"],
        ["sustain", "maintain", "sustained", "maintained", "life", "cycle", "food", "species", "same", "long", "time", "example", "plant", "plants", "animal", "animals"],
        ["growth", "grow", "evolve", "evolution", "develop", "developing", "process", "technology", "modern", "society", "change", "changing", "improve", "improving"]
    ]   
}

# Section C - Vocab
def sectionC(): 
    global coins
    global hintUse
    global questionsC
    global answersC
    global boosterList
    global totalHeight
    questionsC = []
    answersC = []
    hintUse = 0
    totalHeight = 0
    boosterList = [0, 0, 0]
    originalList = [1, 2, 3, 4, 5, 6, 7, 8]
    randomList = []
    time.sleep(1)
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(1)

    for rep in range(len(originalList)): # Randomizes the vocab word order so that it is unique every time
        randomNumber = random.choice(originalList)
        originalList.remove(randomNumber)
        randomList.append(randomNumber)

    questionNumber = 0
    for vocab in randomList:
        questionNumber += 1
        loop = False

        # Asks the user whether they want to buy any booster before they start the question
        while loop == False:
            booster = input(f"\033[1m\033[4m\nBuy Boosters Before Question {questionNumber}!\033[0m\n\nEnter 0 to pass\nEnter 1 to upgrade Hint Perk (1 coin)\nEnter 2 to upgrade Time Perk (2 coins)\nEnter 3 to upgrade Streak Perk (2 coins)\n\n")
            if booster == '1':
                if coins-1 < 0: # Checks if the user has enough coins
                    print("Not enough coins!")
                    playsound("Audio/invalidPurchase.wav") # Invalid purchase sound... etc
                elif boosterList[0] == 3: # Checks if the user already has the max level perk
                    print("Hint perk is already max level (3/3)!") 
                    playsound("Audio/invalidPurchase.wav")
                else:
                    boosterList[0] += 1
                    loop = True
                    print(f"\nHint Perk Level {boosterList[0]}/3 Purchased!\n")
                    playsound("Audio/coinPurchase.wav") # Coin purchase sound... etc
                    print("\033[2m    * Coin Balance: " + str(coins) + " - " + str(1) + " (Hint Perk) = " + str(coins-1) + " coins.\033[0m")
                    coins -= 1
            elif booster == '2':
                if coins-2 < 0: # Checks if the user has enough coins
                    print("Not enough coins!") 
                    playsound("Audio/invalidPurchase.wav")
                elif boosterList[1] == 5: # Checks if the user already has the max level perk
                    print("Time perk is already max level (5/5)!") 
                    playsound("Audio/invalidPurchase.wav")
                else:
                    boosterList[1] += 1
                    loop = True
                    print(f"\nTime Perk Level {boosterList[1]}/5 Purchased!\n")
                    playsound("Audio/coinPurchase.wav")
                    print("\033[2m    * Coin Balance: " + str(coins) + " - " + str(2) + " (Time Perk) = " + str(coins-2) + " coins.\033[0m")
                    coins -= 2
            elif booster == '3':
                if coins-2 < 0: # Checks if the user has enough coins
                    print("Not enough coins!")
                    playsound("Audio/invalidPurchase.wav")
                elif boosterList[2] == 5:
                    print("Streak perk is already max level (5/5)!") # Checks if the user already has the max level perk
                    playsound("Audio/invalidPurchase.wav")
                else:
                    boosterList[2] += 1
                    loop = True
                    print(f"\nStreak Perk Level {boosterList[2]}/5 Purchased!\n")
                    playsound("Audio/coinPurchase.wav")
                    print("\033[2m    * Coin Balance: " + str(coins) + " - " + str(2) + " (Streak Perk) = " + str(coins-2) + " coins\033[0m")
                    coins -= 2
            elif booster == '0':
                time.sleep(1)
                print(f"\033[2m\nProceeding to Question {questionNumber} ...\n\033[0m")
                loop = True 
            else: # Checks if the user inputs a valid option
                print("Please choose a valid option!\n")
                playsound("Audio/invalidPurchase.wav")
        time.sleep(3)

        hintCost = hintsBooster(boosterList[0]) # Sets the hint cost based on the new perks in action
        hintUsed = False
        timeStart = time.time()

        # Asks the user for their answer to the vocabulary question
        answer = input("\033[1m\n" + str(questionNumber) + ". What is " + dataC["words"][vocab-1] + ": \n\n\033[0m\033[1mYour answer: \033[0m")
        if answer.lower() == 'hint': # Checks if the user wants to purchase a hint
            if coins-hintCost < 0: # Checks if the user has enough coins
                print("\nNot enough coins!\n")
                playsound("Audio/invalidPurchase.wav")
                answer = input("\n" + str(questionNumber) + ". What is " + dataC["words"][vocab-1] + ": \n\n\033[1mYour answer: \033[0m")  
            else:
                hintUsed = True
                print("\nHint purchased!\n")
                playsound("Audio/coinPurchase.wav")
                print("\033[2m    * Coin Balance: " + str(coins) + " - " + str(hintCost) + " (hint) = " + str(coins-hintCost) + " coins\033[0m")
                answer = input("\033[1m\n" + dataC["hint"][vocab-1] + "\033[0m\n\n\033[1mYour answer: \033[0m")
                hintUse += 1
                coins -= hintCost
        print("\nAnswer Submitted!\n")
        playsound(random.choice(splashSound))
        print(f'\033[2m    * Coin Balance: {coins}\033[0m')
            
        timeEnd = time.time()
        answersC.append(answer) # Saves the user's answer
        timeTotal = int(timeEnd - timeStart)

        # Keyword filter, checks if it matches with the keywords in 'DataC' dataset
        answerList = answer.split()
        correctList = []
        for word in answerList:
            if word.lower() in dataC["keywords"][vocab-1]:
                correctList.append(word.lower())

        # Keyword streak calculation into initial height gain
        initialGain = 100 + len(correctList) * (boosterList[2]+1)*5 

        # Height calculation
        height = pointCalculation(boosterList, initialGain, timeTotal, hintUsed)
        totalHeight = totalHeight + height

        # Displays the ladder with the user's current height, adjusted with if statements for 2-3-4 digits in height.
        if totalHeight < 100: 
            print(f"""\033[1m\033[34m
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}     ████████████
                █          █
        {int(totalHeight*1.5)}     ████████████
                █          █
    {">>> "}{int(totalHeight)}      ████████████
                █          █
""")
        elif totalHeight >= 100 and totalHeight*2 <= 999:
            print(f"""\033[1m\033[34m
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}     ████████████
                █          █
        {int(totalHeight*1.5)}     ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █\033[0m
""")
        elif totalHeight*2 > 999 and totalHeight*1.5 < 999:
            print(f"""\033[1m\033[34m
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}     ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █\033[0m
""")
        elif totalHeight*1.5 > 999 and totalHeight < 999:
            print(f"""\033[1m\033[34m
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}    ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █\033[0m
""")
        elif totalHeight > 999:
            print(f"""\033[1m\033[34m
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}    ████████████
                █          █
    {">>> "}{int(totalHeight)}    ████████████
                █          █\033[0m
        """)

        playsound("Audio/ladder.mp3") # Ladder climbing sound

        # Displays how many keywords the user got right, and prints what they are
        print("\033[0m\033[1m\nYou got " + str(len(correctList)) + " keywords!\n\033[0m")
        for keywords in correctList:
            print(f"    - {keywords.capitalize()}")      

        # Saves the vocabulary question 
        questionsC.append(str(questionNumber) + ". What is " + dataC["words"][vocab-1] + "?")
        time.sleep(2)
    
    type ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(1)

def pointCalculation(boosterList, initialGain, totalTime, hintUsed): 
    # The main function to calculate the "height" of a user's answer in Section C
    # Time, hints used and keyword streaks are key factors here
    # Basically, aside from the math, the higher perk level the user has purchased, the bigger effect it will have on the final "height"
    if hintUsed == False: # Calculates the hint multiplier deduction
        hintMultiplier = 1
    else:
        hintMultiplier = 0.8 + boosterList[0]*0.05
    timeIntervals30 = math.floor(totalTime/30) # Calculates the time multiplier based on how many intervals of 30 seconds the user took to complete their answer
    timeMultiplier = 1 - timeIntervals30*(0.05-0.01*boosterList[1]) 
    totalMultiplier = initialGain * hintMultiplier * timeMultiplier # Calculates the total multiplier
    return totalMultiplier

def hintsBooster(level:int): # Decides how much a hint would cost, based on the Hint Perk level
    hintCost = 5 - level
    return hintCost
   
def timeConvert(sec): # Converts seconds into a properly formatted clock [x mins y secs]
    if sec < 60:
        elapsedTime = str(str(sec) + " seconds")
        return elapsedTime
    else:
        mins = sec//60
        sec = sec % 60
        mins = mins % 60
        elapsedTime = str(mins) + " minutes " + str(sec) + " seconds "
        return elapsedTime

def gameFinish(): # Conclusion & Summary of Text-Based Game

    # Ending dialogue game, as you jump down the ladder
    type("\nYou look down.")
    time.sleep(2)
    type("\n\n...")
    time.sleep(2)
    type("\n\nWow! You have come a long way up the ladder.")
    time.sleep(4)
    type("\033[1m\n\nYou get ready to take another dive off the board.")
    time.sleep(2)
    type("\n\n...")
    time.sleep(2)
    type("\n\n...")
    time.sleep(2)
    type("\n\nSSSSSSSSPLAAAAAAASHHHHH!\033[0m")
    playsound(random.choice(splashSound))
    multiplierList = [1, 1.05, 1.1, 1.15, 1.2]
    totalHeight = int(totalHeight*(random.choice(multiplierList)))

    time.sleep(3)
    transitionScreen()
    time.sleep(3)
    print("")
    print("""\033[1m\033[32m\n\n
╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌┌─┐┬
║  │ │││││ ┬├┬┘├─┤ │ │ ││  ├─┤ │ ││ ││││└─┐│
╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘└─┘o\033[0m
""")
    
    time.sleep(3)

    print(f"\033[1m\033[4mYour Final Performance Score: {totalHeight}!\n\033[0m")

    # Time Calculation of Individual Sections
    gameElapsed = gameEnd - gameStart
    gameElapsed = int(gameElapsed)
    gameElapsed = timeConvert(gameElapsed)

    sectionAElapsed = sectionAEnd - sectionAStart
    sectionAElapsed = int(sectionAElapsed)
    sectionAElapsed = timeConvert(sectionAElapsed)

    sectionBElapsed = sectionBEnd - sectionBStart
    sectionBElapsed = int(sectionBElapsed)
    sectionBElapsed = timeConvert(sectionBElapsed)

    sectionCElapsed = sectionCEnd - sectionCStart
    sectionCElapsed = int(sectionCElapsed)
    sectionCElapsed = timeConvert(sectionCElapsed)

    time.sleep(3)

    # Gives the score of Section A out of 16 & in percentage
    percentage = int(totalCoins/16*100)
    print("\033[1m\nYour Comprehension Score ......")
    playsound("Audio/drumroll1.mp3") # Drumroll
    print("Section A: \033[0m" + str(totalCoins) + "/16 -- " + str(percentage) + "%!")
    playsound("Audio/drumroll2.mp3")

    # Sends a congrats message for the user finishing the game, and the tone/sound effect varies depending on how good/bad the user did in Section A
    if totalCoins == 0:
        print("Hmm, are you typing in random things?")
        playsound("Audio/kiddingRight0.mp3")
    elif totalCoins >= 1 and totalCoins <= 4:
        print("Nice try, you'll do better next time!")
        playsound("Audio/huh1-4.mp3")
    elif totalCoins >= 5 and totalCoins <= 8:
        print("Keep up the good effort and keep trying!")
        playsound("Audio/singingLaughing5-8.mp3")
    elif totalCoins >= 9 and totalCoins <= 12:
        print("Keep up the great work, you read the book very well!")
        playsound("Audio/winShow9-12.mp3")
    elif totalCoins >= 13 and totalCoins <= 16:
        print("Excellent job, you really impressed me!")
        playsound("Audio/applause13-16.mp3")

    # Coin summaries (Total + Hints + Boosters + Coins Remaining)
    time.sleep(3)
    print("\n\033[1mTotal Earned Coins: " + str(totalCoins) + " coins.\n\033[0m")
    print("\033[1mTotal Hints Used: " + str(hintUse) + " hints.\033[0m")
    totalBoosters = 0
    for booster in boosterList:
        totalBoosters += booster
    print("\033[1mTotal Boosters Used: " + str(totalBoosters) + " boosters.\033[0m")
    print("    * Hint Perk: Level " + str(boosterList[0]) + "/3")
    print("    * Time Perk: Level " + str(boosterList[1]) + "/5")
    print("    * Streak Perk: Level " + str(boosterList[2]) + "/5")
    print("\033[1m\nCoins Remaining: " + str(coins) + " coins\n\033[0m")

    # Time summaries (Total + Section A + Section B + Section C)
    time.sleep(3)
    print("")
    print("\033[1mTotal Elapsed Time: " + str(gameElapsed) + "\033[0m")
    print("Section A Elapsed Time: " + str(sectionAElapsed))
    print("Section B Elapsed Time: " + str(sectionBElapsed))
    print("Section C Elapsed Time: " + str(sectionCElapsed))
    print("")

# Game summaries (coins, hints)
    time.sleep(3)
    print("\033[1m\033[4m\nSection B Short Answers: \n\033[0m")
    for question in range(len(questionsB)):
        print("\033[1m" + questionsB[question] + "\033[0m")
        print(answersB[question] + "\n")
        time.sleep(0.3)
    time.sleep(3)
    print("\033[1m\033[4m\nSection C Vocab Answers: \n\033[0m")
    for question in range(len(questionsC)):
        print("\033[1m" + questionsC[question] + "\033[0m")
        print(answersC[question] + "\n")
        time.sleep(0.3)
    time.sleep(3)

    print("\033[1mI hope you enjoyed my game!")
    print(f"Make sure to share your performance score of \033[4m{totalHeight}\033[24m with your friends to challenge them to beat it!\033[0m") 

# Core Game Functions (THE GAME FUNCTIONS ARE HERE)
gameStart = time.time()
welcomeScreen()
sectionAInfo()
sectionAStart = time.time()
sectionA()
sectionAEnd = time.time()
totalCoins = coins
sectionBInfo()
sectionBStart = time.time()
sectionB()
sectionBEnd = time.time()
sectionCInfo()
sectionCStart = time.time()
sectionC()
sectionCEnd = time.time()
gameEnd = time.time()
gameFinish()

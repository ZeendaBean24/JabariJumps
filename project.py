import time
import math
import random
from playsound import playsound 
# ideas: add emojis, bold words and make titles bigger with ascii (welcome screen finish screen), make user WAIT for the wait times, name input
section = "A" # add quotations to encourage the user on the ladder and an animation at the end of jabari jumping off. "You got this, keep on climbing!", maybe add final booster when they jump off to perform moves, add wait times
correctSound = ["correctAnswer1.mp3", "correctAnswer2.mp3", "correctAnswer3.wav", "correctAnswer4.wav"]
incorrectSound = ["wrongAnswer1.wav", "wrongAnswer2.wav", "wrongAnswer3.wav", "wrongAnswer4.wav"]
splashSound = ["splash1.wav", "splash2.wav", "splash3.wav"]

def welcomeScreen():
    # Welcome Screen

    # Y9 Design
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
   
    time.sleep(3)
    print ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(3)

    # Welcome to Jabari Jumps
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

    time.sleep(3)
    print ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(3)

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
    playsound(random.choice(splashSound))

def sectionAInfo(): # add information about the user waiting for the waiting times for "your answer"
    # Instructions
    global section
    print("\033[1mWelcome to Jabari Jumps Text-Based Game! \033[0m\nThis game will fun and engaging while testing your knowledge on Jabari Jumps!")
    print("\033[2m\nBy: Zeen Liu.\n\033[0m")
    time.sleep(3)
    print("\033[1mInstructions:\033[0m")
    print("    * Prerequisites - Only keyboard is needed, mouse is optional, played in IDLE.")
    print("    * Section A - Basic Comprehension.")
    print("    * Section B - Reflective Questions.")
    print("    * Section C - Vocabulary Review.")
    print("    * This game is designed to be under 20 minutes of total playtime.")
    print("    * There will be multiple choice + short answer questions. ")
    print("    * There are wait times during the code, so don't type in anything before it tells you that you can.")
    print("    * If you enter something before the wait time is over, you risk crashing the game. ")
    print("    * Also, accurate is spelling is important. Sometimes if you miss a letter in a word, the filter will count it as incorrect.")
    time.sleep(8)
    print("\nSection A will only be Multiple-Choice questions.")
    print("It is your only chance to earn coins and spend it on hints & boosters later, so make sure to think about the questions carefully!")
    time.sleep(4)
    print("\033[1m\nReward System: \033[0m") 
    print("    * 1 coin for each first-try correct answer.")
    print("    * No coins deducted from wrong answer.")
    time.sleep(4) # Wait 10 seconds
    section = "A"
    startConfirmation()

# Game Start Confirmation
def startConfirmation():
    gameStart = False
    while gameStart == False:
        start = input("\033[1m\nType in 'ok' when you've read through all the instructions.\n\033[0m")
        if start.lower() == "ok":
            print("\nAlright, let's proceed to Section " + section + ".\n")
            gameStart = True
            time.sleep(3)
            transitionScreen()
            time.sleep(3)
        else:
            print("Not ready? You got this! Try again.")

# Section A 
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

def sectionA(): #instead of just "your answwer" add a message for when it is wrong, make it clear to the user when they receive a coin and if they get the question first try
    global coins
    coins = 0
    time.sleep(3)
    print ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    time.sleep(3)
    for question in range(len(dataA["questions"])):
        print("\033[1m\n" + dataA["questions"][question]+"\n\033[0m")
        time.sleep(3) # wait 3 seconds
        for multipleChoice in dataA["answers"][question]:
            print(multipleChoice)
            correct = False
            firstTry = True
        while correct == False: 
            userAnswer = input("\033[1m\nYour answer: \033[0m")
            if type(dataA["answer"][question]) is str:
                if userAnswer.lower() == dataA["answer"][question]:
                    print("Congrats! This is the right answer. ")
                    correct = True
                    if firstTry == True:
                        coins += 1
                        print("You gain 1 coin for getting it first try! ")
                    else:
                        coins += 0
                    playsound(random.choice(correctSound))
            elif type(dataA["answer"][question]) is list:
                if userAnswer.lower() in dataA["answer"][question]:
                    print("\nCongrats! This is the right answer. ")
                    correct = True
                    if firstTry == True:
                        coins += 1
                        print("You gain 1 coin for getting it first try! ")
                    else:
                        coins += 0
                    playsound(random.choice(correctSound))
            if userAnswer.lower() != dataA["answer"][question]:
                print("Please try again.")
                playsound(random.choice(incorrectSound))
            firstTry = False
        print(f'\033[2m\n  * Coin Balance: {coins} \n\033[0m')

# Section B

def sectionBInfo():
    global section
    print("\033[1mNow, we will be moving onto Section B.\n\033[0m")
    time.sleep(2)
    print("    * This section will ask you harder, open-ended and reflective questions.")
    print("    * As well, you will be introduced to a new concept - United Nations Sustainability Development Goals (UN SDGs).")
    print("    * Essentially, they are goals in order to improve the world that we live in!")
    print("    * Don't worry if you feel challenged! This section is designed for you to learh abstract concepts about the UN SDGs.")
    print("    * We will go step-by-step through the process together.")
    time.sleep(8)
    print("\nSection B will have a combination of Multiple-Choice questions as well as Open-Ended questions.")
    print("Make sure to pay special attention to all the terms that are introduced, as Section C will test you later on them! ")
    time.sleep(4)
    section = "B"
    startConfirmation()

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
        "Now, let's focus on the bigger picture - United Nations Sustainability Development Goals (UNSDG). These are the foundation to build a better society. \nDo you think every child can be like Jabari and have a swimming pool to dive in?",
        "Excellent thinking! Unfortunately, not every city in the world can afford good infrastructure - the foundation and the structure of our city. An example of infrastructure would be public pools.",
        "10. Which of these do you think is part of a city's infrastructure?",
        "They are all correct! \n11. Why do you think infrastructure is important for a city?",
        "11. Now think about how much water a pool needs to function. Do you think all cities can afford these public pools?",
        "12. Why do you think some cities or countries don't have enough water?",
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
    "type": [
        "is", "mc", "is", "sa", "sa", "sa", "sa", "sa", "mc", "is", "sa", "sa", "mc", "is", "mc", "sa", "mc", "sa", "is"
    ]   
} #mc (multiple choice), sa (short answer), is (info slide)

def sectionB(): # fix the congrats this is the right answer screen
    global questionsB
    global answersB
    coins = 16 # remove ltr
    questionsB = []
    answersB = []
    print ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
    print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
    print("\033[0m")
    for question in range(len(dataB["questions"])):
        if dataB["type"][question] == "mc":
            print("\033[1m\n" + dataB["questions"][question]+"\n\033[0m")
            time.sleep(2)
            for multipleChoice in dataB["answers"][question]:
                print(multipleChoice)
            correct = False
            while correct == False: 
                userAnswer = input("\033[1m\nYour answer: \033[0m")
                if type(dataB["answer"][question]) is str:
                    if userAnswer.lower() == dataB["answer"][question]:
                        print("Congrats! This is the right answer. ")
                        playsound(random.choice(correctSound))
                        correct = True
                    else: 
                        print("Please try again.")
                elif type(dataB["answer"][question]) is list:
                    if userAnswer.lower() in dataB["answer"][question]:
                        print("Congrats! This is the right answer. ")
                        playsound(random.choice(correctSound))
                        correct = True
                    else: 
                        print("Please try again.")
                        playsound(random.choice(incorrectSound))
        elif dataB["type"][question] == "sa":
            time.sleep(2)
            shortAnswer = input("\n" + dataB["questions"][question]+"\033[1m\n\nYour answer: \033[0m")
            questionsB.append(dataB["questions"][question])
            answersB.append(shortAnswer)
            print("\nAnswer submitted!\n")
            playsound(random.choice(splashSound))
        elif dataB["type"][question] == "is":
            time.sleep(2)
            print("\033[2m\033[1m\n" + dataB["questions"][question]+"\n\033[0m")
            time.sleep(5)
    print(f'\033[2m\n  * Coin Balance: {coins} \n\033[0m')
    time.sleep(5)

def sectionCInfo():
    global section
    print("Now, we will be moving onto Section C.")
    print("    * Section C will be a vocabulary test to see what you've learned today!")
    print("    * This will be the last section, you will have to write a correct meaning in your own words for each of words in the randomized list.")
    print("    * You can use your hard-earned coins to spend it on hints.")
    print("        * 3 coins = 1 hint.")
    print("        * If you wish to use a hint for a word, simply type in 'hint' when typing your answer.")
    print("    * After you enter your answer, a system checks whether you have written the important keywords.")
    print("    * The more keywords you write in your answer, the higher you climb on the ladder.")
    print("    * The height is also affected by perks that you can buy with coins each turn.")
    print("        * Hint Perk:")
    print("            * Cost - 1")
    print("            * Max Level - 3")
    print("            * Description - It costs less to purchase a hint and they deduct less height.")
    print("        * Time Perk:")
    print("            * Cost - 2")
    print("            * Max Level - 5")
    print("            * Description - Streaks of correct keywords give more height.")
    print("        * Streak Perk:")
    print("            * Cost - 2")
    print("            * Max Level - 5")
    print("            * Description - Longer time to answer a question deducts less height.")
    print("    * In the end, the total height that you have climbed will be your final performance score.")
    time.sleep(10)
    section = "C"
    startConfirmation()

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
        ["growth", "grow", "evolve", "evolution", "developing", "process", "technology", "modern", "society", "change", "changing"]
    ]   
}

def sectionC(): #add the option to buy boosters on every turn, add more info on each booster, add a limit, 
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
    coins = 16 # remove ltr
    boosterList = [0, 0, 0]
    originalList = [1, 2, 3, 4, 5, 6, 7, 8]
    randomList = []
    for rep in range(len(originalList)): 
        randomNumber = random.choice(originalList)
        originalList.remove(randomNumber)
        randomList.append(randomNumber)
    questionNumber = 0
    for vocab in randomList:
        loop = False
        while loop == False:
            booster = input("\nEnter 0 to pass\nEnter 1 to upgrade Hint Perk (1 coin)\nEnter 2 to upgrade Time Perk (2 coins)\nEnter 3 to upgrade Streak Perk (2 coins)\n\n")
            if booster == '1':
                if coins-1 < 0:
                    print("Not enough coins!")
                    playsound("invalidPurchase.wav")
                elif boosterList[0] == 3:
                    print("Hint perk is already max level (3/3)!")
                    playsound("invalidPurchase.wav")
                else:
                    boosterList[0] += 1
                    loop = True
                    print(f"\nHint Perk Level {boosterList[0]}/3 Purchased!\n")
                    playsound("coinPurchase.wav")
                    print("    * Coin Balance: " + str(coins) + " - " + str(1) + " (Hint Perk) = " + str(coins-1) + " coins.")
                    coins -= 1
            elif booster == '2':
                if coins-2 < 0:
                    print("Not enough coins!")
                    playsound("invalidPurchase.wav")
                elif boosterList[1] == 5:
                    print("Time perk is already max level (5/5)!")
                    playsound("invalidPurchase.wav")
                else:
                    boosterList[1] += 1
                    loop = True
                    print(f"\nTime Perk Level {boosterList[1]}/5 Purchased!\n")
                    playsound("coinPurchase.wav")
                    print("    * Coin Balance: " + str(coins) + " - " + str(2) + " (Time Perk) = " + str(coins-2) + " coins.")
                    coins -= 2
            elif booster == '3':
                if coins-2 < 0:
                    print("Not enough coins!")
                    playsound("invalidPurchase.wav")
                elif boosterList[2] == 5:
                    print("Streak perk is already max level (5/5)!")
                    playsound("invalidPurchase.wav")
                else:
                    boosterList[2] += 1
                    loop = True
                    print(f"\nStreak Perk Level {boosterList[2]}/5 Purchased!\n")
                    playsound("coinPurchase.wav")
                    print("    * Coin Balance: " + str(coins) + " - " + str(2) + " (Streak Perk) = " + str(coins-2) + " coins")
                    coins -= 2
            elif booster == '0':
                time.sleep(1)
                print(f"\nProceeding to Question {questionNumber+1} ...\n")
                loop = True 
            else:
                print("Please choose a valid option!\n")
                playsound("invalidPurchase.wav")
        time.sleep(3)
        questionNumber += 1
        hintCost = hintsBooster(boosterList[0])
        hintUsed = False
        timeStart = time.time()
        answer = input("\n" + str(questionNumber) + ". What is " + dataC["words"][vocab-1] + ": \n\n")
        if answer.lower() == 'hint':
            if coins-hintCost < 0:
                print("\nNot enough coins!")
                playsound("invalidPurchase.wav")
                answer = input("\n" + str(questionNumber) + ". What is " + dataC["words"][vocab-1] + ": \n\n")  
            else:
                hintUsed = True
                print("Hint purchased!\n")
                playsound("coinPurchase.wav")
                print("    * Coin Balance: " + str(coins) + " - " + str(hintCost) + " (hint) = " + str(coins-hintCost) + " coins")
                answer = input("\n" + dataC["hint"][vocab-1] + "\n\n")
                hintUse += 1
                coins -= hintCost
        print("\nAnswer Submitted!\n")
        print(f'    * Coin Balance: {coins}')
        playsound(random.choice(splashSound))
            
        timeEnd = time.time()
        answersC.append(answer)
        timeTotal = int(timeEnd - timeStart)

        answerList = answer.split()
        correctList = []
        for word in answerList:
            if word.lower() in dataC["keywords"][vocab-1]:
                correctList.append(word.lower())


        initialGain = 100 + len(correctList) * boosterList[2]*5 
        height = pointCalculation(boosterList, initialGain, timeTotal, hintUsed)
        totalHeight = totalHeight + height
        if totalHeight < 100: 
            print(f"""
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
            print(f"""
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}     ████████████
                █          █
        {int(totalHeight*1.5)}     ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █
""")
        elif totalHeight*2 > 999 and totalHeight*1.5 < 999:
            print(f"""
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}     ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █
""")
        elif totalHeight*1.5 > 999 and totalHeight < 999:
            print(f"""
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}    ████████████
                █          █
    {">>> "}{int(totalHeight)}     ████████████
                █          █
""")
        elif totalHeight > 999:
            print(f"""
                █          █
        Height  ████████████
                █          █
        {int(totalHeight*2)}    ████████████
                █          █
        {int(totalHeight*1.5)}    ████████████
                █          █
    {">>> "}{int(totalHeight)}    ████████████
                █          █
        """)

        playsound("ladder.mp3")

        print("\nYou got " + str(len(correctList)) + " keywords!\n") # add emoji, 
        for keywords in correctList:
            print(f"    - {keywords.capitalize()}")       

        print ("\033[31m\n| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
        print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |")
        print ("| ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ |\n")
        print("\033[0m")

        questionsC.append(str(questionNumber) + ". What is " + dataC["words"][vocab-1] + "?")
        time.sleep(2)

def pointCalculation(boosterList, initialGain, totalTime, hintUsed):
    if hintUsed == False:
        hintMultiplier = 1
    else:
        hintMultiplier = 0.8 + boosterList[0]*0.05
    timeIntervals60 = math.floor(totalTime/30)
    timeMultiplier = 1 - timeIntervals60*(0.05-0.01*boosterList[1])
    totalMultiplier = initialGain * hintMultiplier * timeMultiplier
    return totalMultiplier

def hintsBooster(level:int):
    hintCost = 5 - level
    return hintCost
   
def timeConvert(sec):
    if sec < 60:
        elapsedTime = str(str(sec) + " seconds")
        return elapsedTime
    else:
        mins = sec//60
        sec = sec % 60
        mins = mins % 60
        elapsedTime = str(mins) + " minutes " + str(sec) + " seconds "
        return elapsedTime

# Core Game Functions

gameStart = time.time()
# welcomeScreen()
# sectionAInfo()
sectionAStart = time.time()
# sectionA()
sectionAEnd = time.time()
# totalCoins = coins
totalCoins = 16
# sectionBInfo()
sectionBStart = time.time()
# sectionB()
sectionBEnd = time.time()
sectionCInfo()
sectionCStart = time.time()
sectionC()
sectionCEnd = time.time()
gameEnd = time.time()

def gameFinish():
    # Conclusion & Summary of Text-Based Game
    time.sleep(3)
    transitionScreen()
    time.sleep(3)
    print("")
    print(""""
╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌┌─┐┬
║  │ │││││ ┬├┬┘├─┤ │ │ ││  ├─┤ │ ││ ││││└─┐│
╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘└─┘o\n
""")
    time.sleep(3)

    # Sends a congrats message for the user finishing the game, and the tone varies depending on how good/bad the user did.
    if totalCoins == 0:
        print("Hmm, are you typing in random things?")
        playsound("kiddingRight0.mp3")
    elif totalCoins >= 1 and totalCoins <= 4:
        print("Nice try, you'll do better next time!")
        playsound("huh1-4.mp3")
    elif totalCoins >= 5 and totalCoins <= 8:
        print("Keep up the good effort, keep on trying!")
        playsound("singingLaughing5-8.mp3")
    elif totalCoins >= 9 and totalCoins <= 12:
        print("Keep up the great work, you read the book very well!")
        playsound("winShow9-12.mp3")
    elif totalCoins >= 13 and totalCoins <= 16:
        print("Excellent job, you really impressed me!")
        playsound("applause13-16.mp3")

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

    percentage = int(totalCoins/16*100)
    print("\nYour Comprehension Score ......")
    playsound("drumroll1.mp3")
    print("Section A: " + str(totalCoins) + "/16 -- " + str(percentage) + "%!\n")
    playsound("drumroll2.mp3")

    time.sleep(3)
    print("Total Earned Coins: " + str(totalCoins) + " coins.")
    print("Total Hints Used: " + str(hintUse) + " hints.")
    totalBoosters = 0
    for booster in boosterList:
        totalBoosters += booster
    print("Total Boosters Used: " + str(totalBoosters) + " boosters.")
    print("    * Hint Perk: Level " + str(boosterList[0]) + "/3")
    print("    * Time Perk: Level " + str(boosterList[1]) + "/5")
    print("    * Streak Perk: Level " + str(boosterList[2]) + "/5")
    print("\nCoins Remaining: " + str(coins) + " coins\n")

    # Time summaries (Total + Section A + Section B + Section C)
    time.sleep(3)
    print("")
    print("Total Elapsed Time: " + str(gameElapsed))
    print("Section A Elapsed Time: " + str(sectionAElapsed))
    print("Section B Elapsed Time: " + str(sectionBElapsed))
    print("Section C Elapsed Time: " + str(sectionCElapsed))
    print("")

# Game summaries (coins, hints)
    time.sleep(3)
    print("\n\nSection B Answers: \n")
    for question in range(len(questionsB)):
        print(questionsB[question])
        print(answersB[question] + "\n")
        time.sleep(0.3)
    time.sleep(3)
    print("\nSection C Answers: \n")
    for question in range(len(questionsC)):
        print(questionsC[question])
        print(answersC[question] + "\n")
        time.sleep(0.3)
    time.sleep(3)

    print("I hope you've enjoyed my game!")
    print(f"Make sure to share your score of {totalHeight} with your friends to challenge them to beat it!") 

gameFinish()

# make the animation to end it off, add in instructions to watch out for their spelling, performance score

# make sure to add audio folder on github

# improvements: stablization of perks, better names (no pain no gain + buff time perk), better fomratting, clearer instructions, add difficultues (more/less coins, deducting coins when answer is wrong), github, leaderboard
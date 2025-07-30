"""
1.random number
2.user number 
3.number qualificaton
4.match

"""

import random

computer = random.randint(1,100)
play = True
again = True
a = True
while again:
    
    replay = input("Do you want to play guessing game?[y/n]: ").strip().lower()

    if replay in ["y","n"]:

        if replay == "y":

            while a:            
            
                try:
                    while play:
                        user = int(input("\n📝 Guess the number[1-100]: "))

                        if user == computer:
                            print("\n✅ Congratulation! You have guessed the number..\n")
                            break
                            play = False
                            a = False

                        elif user < computer:
                            print("🤏 Its too low !")
                            a = False
                        
                        elif user > computer:
                            print("🚀 Its too high !")
                            a = False

                except ValueError:
                    print("⚠️ Please enter a valid number..")
                    a = True


        elif replay == "n":

            print("👋 You have exited the game!")
            again = False

        else:
            print("Invalid choice !")

    else:
        print("Invalid choice !")
    
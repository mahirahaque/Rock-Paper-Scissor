import time
import random
list1=['rock','paper','scissor']
player_score=0
computer_score=0
while True:
    player = input("Enter (Rock,paper,scissor): ").lower()
    computer = random.choice(list1)
    print("computer is thinking......")
    time.sleep(0.7)
    print("computer chose: ",computer)
    if computer==player:
        print("🧩 Tie 🧩")
    elif (player=='rock' and computer=='scissor') or (player=='scissor' and computer=='paper') or (player=='paper' and computer=='rock'):
        print("🎯 You win 🎯")
        print("YAYYYYY BULLSEYE!!")
        player_score+=1
    elif player not in list1:
        print("Invalid!! enter rock paper scissors only")
    else:
        print("🪩 Computer Wins 🪩")
        computer_score+=1
    print("scoreboard")
    print(f"Player : {player_score}  ||  Computer : {computer_score}")
    
        

    replay = input("Do you want to play the game again(Yes/No): ").lower()
    if replay!='yes':
        print("Final Score")
        print(f"Player : {player_score}  ||  Computer : {computer_score}")
        if computer_score > player_score:
            print("You lose")
        elif player_score> computer_score:
            print("You win")
        else:
            print("It's a tie")

        print("Thanks for playing")
        break

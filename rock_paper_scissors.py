import random

# note the following
# paper beats rock (paper wraps rock)
# scissors beats paper ( scissors cuts paper)
# rock beats scissors (rock blunts scissors)

user_wins = 0
computer_wins = 0

# creat a list containing the possible picks
options = ['rock','paper','scissors']


# a while loop where all conditions are true
while True:
    
    #prompt a user to enter his or her pick
    user_pick = input("Enter rock/paper/scissors or Q to quit the game : ").lower()
    
    if user_pick == 'q':
        break
    
    if user_pick not in options :
        continue
    
    # create a random variabe to instantiate the list
    
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print("computer picked",computer_pick)
    
    # rock =0 ,paper=1, scissors=2
    
    if user_pick == "rock" and computer_pick == "scissors":
        print("You won !")
        user_wins +=1
        
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won !")
        user_wins +=1
    elif user_pick == "paper" and computer_pick == "rock":
        print("you won !")
        
    else:
        print("The computer won !")
        computer_wins +=1
        
print('You won ', user_wins ,"times")
print("computer won", computer_wins , "times")
print("Thanks for your time , Goodbye")
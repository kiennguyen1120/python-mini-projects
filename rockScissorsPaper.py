import random

def play():
    while True:
        user = input("s for scissors, p for paper, r for rock, q for quit ")
        if user == 'q':
            print("thank u")
            break
        if user not in ['r','p','s']:
            print("invalid value")
            continue
        computer = random.choice(['r','p','s'])
        print(f"computer choice {computer}")
        if(user == computer):
            print("tie")
        elif is_win(user,computer):
            print("u won")
        else:
            print("u lose")

def is_win(user, computer):
    return (user == 'r' and computer == 's') or \
           (user == 'p' and computer == 'r') or \
           (user == 's' and computer == 'p')

play() 
   

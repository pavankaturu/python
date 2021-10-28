import sys

user1=input("what is your name?")
user2=input("and your name")
user1_ans=input("%s,do you want to choose rock,paper or scissors?"%user1)
user2_ans=input("%s,do you want to choose rock,paper or scissors?"%user2)

def compare(u1,u2):
    if u1 == u2:
        print("its a tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            print("rock wins")
        else:
            print("paper wins")
    elif u1 == 'scissors':
        if u2 == 'paper':
            print("scissors win")
        else:
            print("rock win")
    elif u1 == 'paper':
        if u2 == 'rock':
            print("papers win")
        else:
            print("scissors win")
    else:
        print("invalid input you have not entered rock,paper or scissors,try again")
        sys.exit()

    print(compare(user1_ans,user2_ans))



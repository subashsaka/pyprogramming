import random
print("choose 1 for rock\nchoose 2 for scissor\nchoose 3 for paper")
user = int(input())

roboinput = [1,2,3]
#1=rock
#2=scissor
#3=paper
robo = random.choice(roboinput)
if user == robo:
    print(f"you both choose same {user} ,{robo} draw")
elif user == 1 and robo == 2:
    print(f"user win because he chose rock")
elif user == 1 and robo == 3:
    print(f"user win because he chose rock")
elif user == 2 and robo == 3:
    print(f"user win because he chose sicssor")
elif robo == 2 and user == 3:
    print(f"robo win because he chose sicssor")
elif robo == 1 and user == 2:
    print(f"robo win because he chose sicssor")
elif robo == 1 and user == 3:
    print(f"robo win because he chose sicssor")
elif user == 2 and robo == 3:
    print(f"user win because he chose sicssor")
elif user == 2 and robo == 3:
    print(f"user win because he chose sicssor")    
else:
    print("choose bettr")










"""
{1, 2}
{1, 3}
{2, 3}
"""
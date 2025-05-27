print("Welcome to my quiz!")
user = (input("Do you want to play my Quiz? "))
if user.lower() == "yes":
    print("lets play")
else:
    quit()
score = 0
question1 = input("who is the prime minister of india? ")
if question1.lower() == "modi":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
question1 = input("who is the cheif minister of andhra pradesh? ")
if question1.lower() == "chandra babu naidu":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
question1 = input("who is the deputy cm of andhra pradesh? ")
if question1.lower() == "pawan kalyan":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
question1 = input("who is the director of movie kalki ? ")
if question1.lower() == "naga ashwin":
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")
print("you scored " + str(score) + " questions correct")
print("your percentage is " + str((score / 4) * 100) )
#hello
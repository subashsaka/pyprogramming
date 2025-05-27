import random
wordlist = ["TIGER","CHEETHA","LION"]
randomword = random.choice(wordlist)
print("WELCOME TO MY HANGMAN GAME")
print("YOU HAVE SIX LIFES LEFT SO USE YOUR MIND!")

emptyspace = ''
for num in range(len(randomword)):
    emptyspace += "_"
print(emptyspace)

lives = 6
corretlet = []
gameover = False
while not gameover:
    guess = input("Guess a Letter: ").upper()
    display = ""
    for i in randomword:
        if i == guess:
            display+=i
            corretlet.append(i)
        elif i in corretlet:
            display+=i
        else:
            display+="_"
    print(display)

    if guess not in randomword:
        lives -= 1
        if lives == 0:
            gameover = True
            print("you lost")

    if "_" not in display:
        gameover = True
        print("you won")
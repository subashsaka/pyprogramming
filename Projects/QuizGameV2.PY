

questions = ("what is the largest planet in our solar system",
            "what is the Next plant to earth",
            "How many bones are there in a human body",
            "How many elements in perodic tabel",
            "who is the prime minister of india")
options = (("A. earth","B. mars","C. jupiter"),
           ("A. mars","B. venus","C. saturn"),
           ("A. 206","B. 100","C. 207"),
           ("A. 118","B. 109","C. 207"),
           ("A. modi","B. rahul gandhi","C. jagan"))
answers = ("C","A","A","A","A")
gusses = []
score = 0
qnum = 0
for question in questions:
    print("----------------------------------------------")
    print(question)
    for optin in options[qnum] :
        print(optin)
    guess = input("Enter your answer (A B C)\n").upper()
    gusses.append(guess)
    if guess == answers[qnum]:
        score +=1
        print("correct!")
    else:
        print("Incorrect")
        print(f"{answers[qnum]} is the correct answer")
    qnum = qnum+1


print("-----------------------------------------------")
print("                   RESULT                      ")
print("ANSWERS")
for answer in answers:
    print(answer,end = " ")
print()
print("GUESSES")
for guess in gusses:
    print(guess,end = " ")
print()
score = score / len(questions) * 100
print(f"your score is {score} %")
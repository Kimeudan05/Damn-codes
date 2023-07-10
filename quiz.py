print("-------------------------")
print("*************************")
print("Welcome to the quiz game, be ready to learn ):")
questions = ("What is the largest country :? ",
             "How many planets do we have in the solar system : ?",
             "how many provinces were there previously in kenya :?",
             "Which year did kenya gain her independence: ?",
             "Who is the current kenyan president : ?"
             )

options = (('A.Tanzania','B.Morrocco','C.Russia','D.Canada'),
           ('A.3','B.5','C.2','D.9'),
           ('A.8','B.7','C.10','D.5'),
           ('A.1978','B.1963','C.1999','D.1964'),
           ('A.Ruto','B.Uhuru','C.Kenyatta','D.Moi')
           )

answers = ("C",'D','A','B','A')

guesses = []

score = 0

question_num = 0

for question in questions:
    print('------------------------')
    print (question)
    for option in options[question_num]:
        # print('------------------------')
        print(option)
        
    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
    print(f'{answers[question_num]} is the correct answer')
        
        
    question_num  += 1 
        
print("--------------------------")

print('           RESULTS         ')

print('answers:',end='')


for answer in answers:
    print(answer , end=' ')
print()

print('guesses :' , end=' ')

for guess in guesses:
    print(guess, end= ' ')
print()
    
score = int(score/len(questions)*100)
print(f'your score is : {score}%')
        

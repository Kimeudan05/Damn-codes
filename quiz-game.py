print("Welcome to my computer quiz")

x=input("Do you want to play ? ")
score=0
if x.lower() != "yes":
    quit()

answer=input("What does cpu stand for? ").lower()
if answer == "central processing unit":
    print ("correct !")
    score += 1
else:
    print("Incorrect !") 
    
answer=input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print ("correct !")
    score += 1
else:
    print("Incorrect !") 

answer=input("What does CLI stand for? ").lower()
if answer == "command line interface":
    print ("correct !")
    score += 1
else:
    print("Incorrect !") 
    
answer=input("What does PSB stand for? ").lower()
if answer == "public service board":
    print ("correct !")
    score += 1
else:
    print("Incorrect !") 
    
   
percent = str((score/answer.len)*100)
 
print("you got", percent,"questions correct")
# print("you got "+str((score/4 )*100) + "%")


print("Thanks for your time hope to see you back again soon ")
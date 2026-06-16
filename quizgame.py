print("welcome to my computer quiz!")

playing = input("Do you want to play?" )
if playing.lower() != "yes":
    quit()
print("Okay!Let's play")
score=0
answer1= input("What does CPU stands for? ")
if answer1.lower()=="central processing unit":
    print("your answer is correct ")
    score+=1
else:
    print("Incorrect")
answer2= input("What does GPU stands for? ")
if answer2.lower()=="graphics processing unit":
    print("your answer is correct ")
    score+=1
else:
    print("Incorrect")
answer3= input("What does RAM stands for? ")
if answer3.lower()=="random access memory":
    print("your answer is correct ")
    score+=1
else:
    print("Incorrect")
answer4= input("What does PSU stands for? ")
if answer4.lower()=="power supply":
    print("your answer is correct ")
    score+=1
else:
    print("Incorrect")
print("You got"+str(score)+"question correct!")
print("You got"+str((score/4)*100)+"%")
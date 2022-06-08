print("welcome to quiz")

playing=input("do you want to play? ")

if playing.upper() != "YES":
    quit()

print("okay lest play :)")
score=0

answer=input("capital of ka? ")
if answer.upper()=="BANGALORE":
    print("correct!")
    score+=1
    #print("score is " + str(score))
else:
    print("incorrect!!!")

answer=input("langauge of KA? ")
if answer.upper()=="KANNADA":
    print("Correct")
    score += 1
else:
  print("incorrect")

answer=input("capital of india ")
if answer.upper()=="DELHI":
    print("correct")
    score +=1
else:
    print("incorrect")

print("the score is " + str(score))
print("the % is " + str((score/3)*100))


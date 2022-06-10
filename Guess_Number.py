import random

computer_guess=input("Guess a number between ")

if computer_guess.isdigit():
    computer_guess=int(computer_guess)
else:
    print("enter the number only!!!!")

    if computer_guess <=0:
     print("enter a number ")
     quit()

random_number=random.randint(0,computer_guess)

while True:

 user_guess=input("Guess the number ")

 if user_guess.isdigit():
     user_guess=int(user_guess)
 else:
     print("please type a number only")
     continue

 if user_guess==random_number:
     print("correct")
     break
 elif user_guess > random_number:
  print("its above the random number")
 else:
  print("its below the random number")

print("you got it!")

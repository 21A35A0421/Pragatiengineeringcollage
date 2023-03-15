import random
top_range=int(input("enter the top range of number:"))
r=random.randint(0,top_range)
count=0
while True:
    count+=1
    user_guess=int(input("guess the number:"))
    if r==user_guess:
        print("you got it")
        break
    elif user_guess>r:
        print("you were above the number")
    elif user_guess<r:
        print("you were below the number")
print('you guessed in ',count,"chances")
    
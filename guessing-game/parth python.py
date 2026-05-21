import random
x=1
i=random.randint(1,100)
print(i)
while True:
    a=int(input("Guess a number between 1 to 100- "))
    b=abs(i-a)
    if b!=0:
        if b>=75:
            print("Oops! Too far from the number")
        elif b<=15:
            print("So close! Try again!")
        elif 15<b<75:
            print("You're not too far! Try again!")
        x=x+1
    else:
        break
print("You've got the correct number!")
print("Number of tries-",x)


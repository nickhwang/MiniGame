import random

#1.在1～99隨機
secret = random.randint(1,99)
guess = 0
tries = 0   
print("AHOY! Come try my game！")

#2.加入限制猜的次數
while guess != secret and tries<6:
    guess = int(input("what's your guess: "))
    if guess < secret:
        print('too low, Try again!')
    elif guess > secret:
        print('too high, Try again!')
    tries = tries + 1
    
#3.贏&輸
if guess == secret:
    print('great, you win!')
else:
    print('bye, you lose!')

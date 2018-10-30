# MiniGame
import random

secret = random.randint(1,99)
guess = 0
tries = 0
print("AHOY! I'm the Dread Pirate,")
while guess != secret and tries<6:
    guess = int(input('whats your guess: '))
    if guess < secret:
        print('too low')
    elif guess > secret:
        print('too high')
    tries = tries + 1

if guess == secret:
    print('great!')
else:
    print('bye')

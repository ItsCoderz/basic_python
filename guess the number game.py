import random
n = random.randint(1,10)
guess_count = 0
guess_limit = 2
while guess_count <= guess_limit:
    guess = int(input("Guess any number from 1 to 10 :"))
    guess_count +=1

    if guess == n:
        print("You Win")
        break
else:
    print("Sorry, you lose")

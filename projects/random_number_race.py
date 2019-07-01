import random
from time import time

while True:
    start_time = time()
    for i in range(50):
        print("\n")
    lower_target = 0
    high_target = 1000
    random_number = random.randint(lower_target, high_target)
    guesses = 0
    while True:
        random_number2 = random.randint(lower_target, high_target)
        if random_number2 != random_number:
           print("Status: Wrong")
           print("Number Guess:", random_number2)
           print("Guesses:", guesses)
           print("")
           guesses += 1
           continue
        else:
            print("Status: Correct")
            print("Number Guess:", random_number2)
            print("Guesses:", guesses)
            break
    print("It took: " + str(time() - start_time) + " seconds")
    break


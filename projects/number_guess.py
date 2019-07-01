import random

while True:
    times = -0
    random_num = random.randint(0, 10)
    guessed = False
    while True:
        for i in range(50):
            print("\n")
        print("You have guessed", times, "times")
        guess = int(input("What is the number. It is between 1 and 10.\n"))
        if guess == random_num:
            break
        else:
            times += 1
            continue
    print("You guessed the number! Congrats! \nThe number was: " + str(random_num) + "\n" + "It took you " + str(times) + " times" "\n\n")
    play_again = bool(int(input("Do you wanna play again? Answer with 0 (no) or 1 (yes)\n")))
    if play_again:
        continue
    else:
        break

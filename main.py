import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    number = input("Please guess a number between 1 and {} : ".format(range))
    number = int(number)
    count = -1
    while number != random_number: 
        number =  input("Please guess a number between 1 and {} : ".format(range))  
        number = int(number)
        count = count + 1
        if not number.isdigit():
            print("Enter a number!") 
        else:    
            print("Sorry, that's not it")
            if number > random_number:
                print("Too high!")
            elif number < random_number:
                print("Too Low!")
    print("Good job!")        
    print("You guessed it in {} tries".format(count))
    play_again = input("\nWould you like to play again? (yes or no)")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else: 
        quit = True

print("\n\nThanks for playing! See you soon")
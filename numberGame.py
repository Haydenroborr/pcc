intro = "I'm thinking of a number! Try to guess the number I'm thinking of:\n"
end = "That's it! Would you like to play again? Y/N\n"
wrong = "Guess again:\n"
high = "Too high!"
low = "Too low!"
want = "Would you like to play a game? Y/N\n"

def numbergame(guess):
    guess = int(guess)
    while guess != number:
        guess = int(guess)
        if guess < number:
            print(low)
            guess = input(wrong)
            pass
        elif guess > number:
            print(high)
            guess = input(wrong)
            pass
        elif guess == number:
            break
        else:
            print("I fucked up somewhere here.")



play = input(want)

while play == "Y" or 'y':
    import random
    number = random.randrange(1, 100)
    guess = input(intro)
    numbergame(guess)
    play = input(end)

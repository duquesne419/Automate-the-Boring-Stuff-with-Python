def collatz(number):
    while True:
        if number == 1:
            break
        elif number % 2 == 0:
            number /= 2
            print(number)
        elif number % 2 == 1:
            number *= 3
            number += 1
            print(number)
        else:
            print('You did not enter a valid number')

def game():
        print('Enter an interger.')
#        guess = input()
        while True:
            try:
#                guess = int(str(guess))
                guess = int(input())
                break
            except ValueError:
                print('You did not enter an integer.')
        collatz(guess)

game()


def collatz(number):

        while True:
            if number == 1:
                break
            elif number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
            else:
                print('You did not enter a valid number.')
        print('Congratulations!')
    
def game():
    print('Enter an interger.')
    guess = input()
    try:
        guess = int(guess)
        collatz(guess)
    except ValueError:
        print('You did not enter an integer.')
        continue
     
game()

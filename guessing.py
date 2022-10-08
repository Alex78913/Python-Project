import random


def guessing():

    print("""
        Welcome to the Number Guessing Game! 
        I'm thinking of a number between 1 and 100.  
        You have 5 attempts remaining to guess the number.
        """)
    number_to_guess = random.randint(1, 100)
    attempt = 0
    choice_level = input('Choice level , easy or hard? : ')
    if choice_level == 'easy':
        attempt += 10
    elif choice_level == 'hard':
        attempt += 5
    else:
        print('Bad wrong!')

    while attempt:
        if attempt > 0:
            number = int(input('Write a number to guess: '))
            if number == number_to_guess:
                print('Congratulations! You win!')
                attempt = 0
            elif number > number_to_guess:
                attempt -= 1
                print("""
            To high.
            Write again!
            -----------------------------""")
                print(f'You have {attempt} attempt')
            elif number < number_to_guess:
                attempt -= 1
                print("""
                To low.
                Write again!
                -----------------------------""")
                print(f'You have {attempt} attempt')
            else:
                print('Not a number!')
        else:
            print('Sorry , you lose.')



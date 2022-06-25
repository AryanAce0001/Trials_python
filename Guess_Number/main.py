import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input('Guess it!: '))
        print(guess)
        if guess<random_number:
            print('Too Low! Guess Again!: ')
        elif guess>random_number:
            print('Too High! Guess Again!: ')
    
    print('Congrats! You\'re right {} ' .format(random_number))

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high=guess -1
        elif feedback == 'l':
            low= guess+1
    print('I guessed it!  (〜￣▽￣)〜  it\'s {}!'.format(guess))

m=int(input('Please choose \n1. You(Human) \n2. Computer'))
if m==1:
    guess(100)
elif m==2:
    computer_guess(50)
else:
    print('ERROR! \nINVALID INPUT!')
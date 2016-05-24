from random import randint

def guess_a_number(guess):
    """Game to guess a number the computer randomly generated."""
    
    random_number = randint(0, 100)
    i =0
    
    guess = check_raw()

    while evaluate_my_number(guess, random_number) == False:

        i = i+1
        guess= check_raw()

        if i ==21 :
            print ('New game you needed too much trys')
            break

        elif i < 21:
            print ('You tried '+ str(i)+ ' time(s)')
            

    # TODO:
    # generate a random number (uniformly distributed between 0 and 100)
    # read input from the user and validate that the input is numeric (use the function check_raw)
    # check whether the number was guessed 
    # implement the functions evaluate_my_number, which checks whether the number is too high or too low
    # and print this information to the user
    # let the computer guess, therefore implement the demo_a_number function
    


def check_raw():
    """Gets the string, raw_input should print, checks and returns the input.""" 
    guess = input ("Please enter an integer: ")
    
    try:
        guess = int(guess)

    except:
        print ('Try again')
        guess= check_raw()
    
    return guess

def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""
    boolint = False
    
    if guess < random_number:
        print ('Get higher')
        boolint = False
    elif guess > random_number:
        print ('Get lower')
        boolint = False
    elif guess == random_number:
        print ('Oh YEAH')
        boolint = True
    return boolint

def demo_a_number():
    """The computer tries to guess the number"""
    
    random_number = randint(0,100)
    cp_guess = 50

    cp_unter=0
    cp_ober=100
    i=1

    while cp_guess != random_number:

        print (cp_guess)
        i=i+1

        if cp_guess < random_number:
            cp_unter = cp_guess

            cp_guess = (cp_guess+cp_ober)//2
            
            
        elif cp_guess >random_number:
            cp_ober= cp_guess

            cp_guess = (cp_guess+cp_unter)//2
            
            

    print (str(cp_guess)+ ' is the number')
    print (str(i)+' tries')

    
demo_a_number()

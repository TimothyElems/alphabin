'''
*all good programmers start with documentation

I want to convert Inglish to Binary

Convert a binary number, 0b01001000 to an alphabet or string, through chr()
Pseudocode:\
    - Start with a variable that is a string (later, make it an input)
    - Convert the string to an integer
    - Convert the integer to binary
    - Loop the operation


I need to loop something. A loop is a condition + clause(s).
What I need is for the program to continually take input and turn that into binary code. The program will also need a way to stop this process.\
    Condition: As long as the input isn't 'quit' or 'Quit', run the loop; or else, end the loop.
    Clause: Turn the alphanumeric characters into binary chars.
'''


import string

def ing_2_bin():
    print('Hello!\nType a message and you\'ll see it in binary.\nType "quit" to end the program.')
    dope = input("Type it here: ")
    # if dope != 'quit' or 'Quit':
    for i in dope:
        dope2num = str(i)
        num2bin = ord(dope2num)
        binned = bin(num2bin)
        print(binned)
           
            # IT WORKS!!!!!!!!!!!!!!!!!!!!!!!! BOOOWOOOOM
   
        



ing_2_bin() 


def run_up():
    apple = input()
    if apple == 'yes':
        print('Thanks')        
    else:    
        for i in range(0, 60):
            print(i)
        # dapple = input()
        apple = input()
        print('Do you want to try again? Yes or no:', apple)
        

# run_up()

# *** Ta-Da List ***
# What is the iterative block?
# What initiates the loop?
# What ends the loop?
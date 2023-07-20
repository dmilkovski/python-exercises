
def ask() :
    while True:
        try :
            x = int(input('Input integer'))
            x = x**2
            print(f'Thank you your number squared is {x}')
            break;
        except :
            print('An error occured! Please try again');
            
            
ask()

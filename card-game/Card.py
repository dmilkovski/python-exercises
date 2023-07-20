import random

class Card :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
    
    def __str__ (self) :
        return f'{self.rank} of {self.suit}'
    
def square(n) :
    for x in range(0,n) :
        yield x**2
        
# for x in square(10):
#     print(x)
    
def generate_random_list(min, max, n) :
    for x in range(0, n) :
        yield random.randrange(min, max+1)
        
# for x in generate_random_list(1,100, 3):
#     print(x)
    
some_str = 'random str'
iter_some_str = iter(some_str)

print(next(iter_some_str))
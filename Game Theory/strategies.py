import random

def random(s):
    return random.choice(['C', 'D'])

def freidman(s):
    '''Holds a grudge, cooperates until the opponent defects then always defects'''
    if 'D' in s:
        return 'D'
    else:
        return 'C' 

def joss(s):
    '''If first move it cooperates, then mimics the opponent's last move with a 10% chance of defecting'''
    if len(s) == 0:
        return 'C'
    else:
        if random.random() < 0.1:
            return 'D'
        else:
            return s[-1]
        
def titfortat(s):
    '''If first move it cooperates, then mimics the opponent's last move'''
    if len(s) == 0:
        return 'C'
    else:
        return s[-1]
        
def grasskamp(s):
    '''If first move it cooperates, then mimics the opponent's last move unless its the 50th '''
    
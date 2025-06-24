'''
this program sings (i.e. prints) the road trip song, "99 Bottles of Beer".
'''
def get_starting_number():
    ''' 
    this function asks the user how many bottles of beer on the wall they want to start singing with
    as many times as necessary until the user enters a valid response,
    which is considered to be any integer 1 or greater.
    '''
    rounds= input("How many bottles of beer on the wall? (use an integer more or equal to 1).")
    if  rounds.isdigit() and int(rounds)>=1:
        rounds=int(rounds)
        return rounds
    else:
        get_starting_number()

def sing(n):
    '''
    this function takes an argument specifying how many bottles of beer to start with, 
    and then outputs the lyrics to the song, starting from that number of bottles.
    '''
    if n>1:
        next_word="bottles"  
        for i in range(n,1,-1):
            next_n = i - 1
            if next_n == 1:
                next_word = "bottle"
            print(f'''{i} bottles of beer on the wall, {i} bottles of beer.
                  Take one down, pass it around, {(i-1)} {next_word} of beer on the wall.''')
    print('''1 bottle of beer on the wall, 1 bottle of beer.
          Take it down, pass it around, no more bottles of beer on the wall!''')
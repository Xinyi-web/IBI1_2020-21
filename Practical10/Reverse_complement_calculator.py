# set up a function
def f(x):
    # transform all letters to capital
    cap = x.upper()
    # inverse the data
    tra = cap[::-1]
    # use dictionary to transform the DNA to corresponding DNA
    l = list(tra)
    dict = {}
    rev = {'A':'T','T':'A','G':'C','C':'G'}
    os = [rev[a] for a in l]
    output =''.join(os)
    return(output)
# make an example
x = "aacTGcTgcA"
print('here is an example for DNA sequence aacTGcTgcA: ' + f(x))
# code for inputting
x = input('please write the DNA sequence here: ')
print('the result of the transforming: '+f(x))

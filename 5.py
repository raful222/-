'''
refael robinov 311374193
gabi levin  317618346
'''

def Weight(number):
    count=num_of_organs(number)
    max=Max(number,0)

    return count+max

def num_of_organs (n):
    count=1
    if (n < 1):
        return (count-1)
    else:
        return ( count+ num_of_organs(n//10))

def Max (n,max) :

    if(max < n%10):
        max = n % 10
    if (n < 1):
        return (max)
    else:
        return (Max(n // 10,max))




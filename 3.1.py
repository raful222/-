'''
refael robinov 311374193
gabi levin  317618346
'''

def GoodOrder(number):
    count,count1,count2=0,0,0
    while(number!=0):
        count += 1
        if((number % 2)  == 1):
            count1 += 1
        if((number % 2) == 0):
            count2 += 1
        number //= 10
    if(count==count1 or count==count2):
        return True
    else:
        return False




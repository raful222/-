'''
refael robinov 311374193
gabi levin  317618346
'''

def Reduce(num):
    new_num=0
    if num>=0:
        if(num <1):
            return new_num
        elif(num%10==0):
            return Reduce(num//10)
        else:
            return (new_num+num%10) + Reduce(num//10)*10
    else:
        if -1*num <1:
            return (new_num)
        elif (num % 10 == 0):
            return Reduce(num // 10)
        else:
            return ((new_num + (-1*num % 10)) + Reduce(-1*num // 10) * 10)*-1

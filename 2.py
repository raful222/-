'''
refael robinov 311374193
gabi levin  317618346
'''
def Digits(n):
    digits,sum,digit_1,digit_2,num=0,0,0,0,n
    if n < 100000:
        while num!=0:
            digits += 1
            num//=10
        if digits == 1 :
            if n%2 ==0 : print('one digit    -even({0})'.format(n))
            else: print('one digit    -odd({0})'.format(n))

        elif digits == 2:
            digit_2,digit_1=n%10,n//10
            sum=digit_2+digit_1
            if sum%2 == 0: print('two digits    -even({0}+{1}={2})'.format(digit_1,digit_2,sum))
            else: print('two digits    -odd({0}+{1}={2})'.format(digit_1,digit_2,sum))

        elif digits == 3:
            digit_2, digit_1 = n % 10, n // 100
            sum = digit_2 + digit_1
            if sum % 2 == 0:
                print('three digits    -even({0}+{1}={2})'.format(digit_1, digit_2, sum))
            else:
                ('three digits    -odd({0}+{1}={2})'.format(digit_1, digit_2, sum))

        elif digits == 4:
            n//=10
            digit_2=n%10
            n//=10
            digit_1=n%10
            sum = digit_2 + digit_1
            if sum % 2 == 0:
                print('four digits    -even({0}+{1}={2})'.format(digit_1, digit_2, sum))
            else:
                print('four digits    -odd({0}+{1}={2})'.format(digit_1, digit_2, sum))
        elif digits == 5 :
            n//=100
            digit_1=n%10
            if digit_1%2 == 0 : print('five digits    -even({0})'.format(digit_1))
            else: print('five digits    -odd({0})'.format(digit_1))
    else:
        print("Error !")

'''
Home Work number 1:
refael robinov 311374193
gavriel levin  317618346
'''


def Xnor(x,y):
    """
       Question number. 1
       Function returning the anwser of Xnor beteen 2 paramters
       Parameters list. x,y
       Return True or False.
       """
    if(x == True and y==True):
        return True
    if(x == True and y== False):
        return False
    if (x == False and y == True):
        return False
    if (x == False and y == False):
        return True


def Digits(n):
    """
           Question number. 2
           Function  A number is checked if his amount of digit less then 6 then:
            1- If there is only one digit then prints the digit itself
            2-If there are two digits prints its sum
            3- If three digits prints the sum of the digits of the first and last
            4- If four digits prints the sum of the middle digits
            5-If there are five digits, print the middle digit
           Parameters are a number Up to 5 digits
           """
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

def GoodOrder(number):
    """
          Question number. 3
          Function returns true if all digits in the number are even or odd numbers
          Parameters list.  a Integer number
          Return True or False.
          """

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


def Figure(n):
    """
             Question number. 4
             Function Prints a triangle at the top starting with the
             number 1 up to the number itself in the hip shape at the ends of the largest number in the row
             Parameters list. single-digit integer
             """
    for i in range(1,n):


        for j in range(1,n*2):
            if i+j==n+1 or j-i == n-1:
                print(i,end="")
            else:
                print(" ",end="")
        print()
    for j in range(n,0,-1):
        print(j,end="")
    for j in range(2,n+1):
        print(j,end="")
    print()



def Weight(number):
        """
              Question number. 5
              Function Returns the weight of a digit with help of 2 Recursive function
              A weight is defined as the sum of the number of digits and a digit with a maximum value
              Parameters list.  a Integer number
              Return integer.
              """
        count = num_of_organs(number)
        max = Max(number, 0)

        return count + max

def num_of_organs(n):
        """
                  Question number. 5 help
                  Function Recursive Returns the num_of_organs in a digits
                  Parameters list. a Integer number
                  Return integer.
                  """
        count = 1
        if (n < 1):
            return (count - 1)
        else:
            return (count + num_of_organs(n // 10))

def Max(n, max):
        """
                      Question number. 5 help
                      Function Recursive Returns the Max digits in a number
                      Parameters list. a Integer number and maxiuom number
                      Return integer.
                      """
        if (max < n % 10):
            max = n % 10
        if (n < 1):
            return (max)
        else:
            return (Max(n // 10, max))



def IsPrimary(n):
    """
              Question number. 6
              Function Recursive returns true if The number is a prime number
              Parameters list.  a Integer number
              Return True or False.
              """
    def IsPrimery_Help(n,i):
        if i==1:
            return True
        if n%i==0:
            return False
        return IsPrimery_Help(n,i-1)
    return IsPrimery_Help(n,n//2)

def Reduce(num):
    """
              Question number. 7
              Function Recursive returns a number Consisting of the digits of the number without the digit 0
              Parameters list.  Integer number.
              Return a Integer number.
              """
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


def Pascal(n,m):
    """
              Question number. 8
              Function Recursive returns The number that appears in row n and column m in the Pascal triangle
              Parameters list.  2 Integer number
              Return Integer.
              """
    if n < m : return -1
    if n == 0 or n == m or m==0: return 1
    else:
        return Pascal(n-1,m-1) + Pascal(n-1,m)





print('Xnor Docstrings')
print (Xnor.__doc__)

print('Digits Docstrings')
print (Digits.__doc__)


print('GoodOrder Docstrings')
print (GoodOrder.__doc__)

print('Figure Docstrings')
print (Figure.__doc__)

print('Weight Docstrings')
print (Weight.__doc__)
print('num_of_organs Docstrings')
print (num_of_organs.__doc__)

print('Max Docstrings')
print (Max.__doc__)

print('IsPrimary Docstrings')
print (IsPrimary.__doc__)

print('Reduce Docstrings')
print (Reduce.__doc__)

print('Pascal Docstrings')
print (Pascal.__doc__)


print('File Docstrings')
print(__doc__)

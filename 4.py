'''
refael robinov 311374193
gabi levin  317618346
'''

def Figure(n):
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


'''
refael robinov 311374193
gabi levin  317618346
'''

def Pascal(n,m):
    if n < m : return -1
    if n == 0 or n == m or m==0: return 1
    else:
        return Pascal(n-1,m-1) + Pascal(n-1,m)



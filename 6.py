'''
refael robinov 311374193
gabi levin  317618346
'''

def IsPrimary(n):
    def IsPrimery_Help(n,i):
        if i==1:
            return True
        if n%i==0:
            return False
        return IsPrimery_Help(n,i-1)
    return IsPrimery_Help(n,n//2)


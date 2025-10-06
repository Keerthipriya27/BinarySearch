def nthRoot(n,m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n<m):
            low=mid+1
        else:
            high=mid-1
    return -1
m=int(input())
n=int(input())
print(nthRoot(n,m))
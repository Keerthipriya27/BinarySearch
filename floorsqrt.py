def floorSqrt(n):
    ans=0
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid>=n):
            high=mid-1
            ans=mid
        else:
            low=mid+1
            ans=mid
    return ans
n=int(input())
print(floorSqrt(n))



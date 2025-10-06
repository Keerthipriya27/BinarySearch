def lowerBound(arr,target):
        # code
        low=0
        high=len(arr)-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>=target):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
arr=list(map(int,input().split()))
target=int(input())
print(lowerBound(arr,target))

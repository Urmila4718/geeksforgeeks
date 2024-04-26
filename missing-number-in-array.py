#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        array_set = set(array)
        for i in range(1,n+1):
            if i not in array_set:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends

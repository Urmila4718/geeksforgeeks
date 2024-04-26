class Solution:
    def duplicates(self, arr, n):
        seen = set()
        duplicates_set = set()

        for i in arr:
            if i in seen:
                duplicates_set.add(i)
            else:
                seen.add(i)

        # Convert set to list and sort it
        duplicates_list = sorted(duplicates_set)

        if duplicates_list:
            return duplicates_list
        else:
            return [-1]

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends

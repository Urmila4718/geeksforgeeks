def check_status(a, b, flag):
    # print(a>=1 and b>=1)
    if (a>=1 and b>=1) and (flag==False):
        return False
    if ((a>=1) or (b>=1)) and (flag==False):
        # print('1')
        return True
    elif (a<0 and b<0) and (flag==True):
        return True
    else:
        # print('2')
        return False



#{ 
 # Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()

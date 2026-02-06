#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        i = 0
        j = 0
        
        while j < len(b) and i < len(a) and b[j] >= a[i]:
            if b[j] == a[i]:
                j += 1
                
            i += 1
            
        return j == len(b)    
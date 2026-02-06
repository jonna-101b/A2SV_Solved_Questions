class Solution:    
    def findUnion(self, a, b):
        a.sort()
        b.sort()
        union = []
        i = 0
        j = 0
        max_len = len(a) + len(b)
        
        while i + j < max_len:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                if not union or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
                continue
                
            elif j < len(b) and (not union or union[-1] != b[j]):
                union.append(b[j])
            j += 1
            
        return union
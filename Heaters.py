class Solution:
    def findRadius(self, house: List[int], heaters: List[int]) -> int:
        def check(radius):
            i = 0
            for h in house:
                while i < len(heaters) and abs(heaters[i] - h) > radius:
                    if heaters[i] < h:
                        i += 1
                    else:
                        
                        return False
                
                if i == len(heaters):
                    return False
            return True

                
        house.sort()
        heaters.sort()
        l=0
        r=max(house[-1],heaters[-1])
        while l<r:
            mid=((l+r)//2)
            if check(mid):
                print(mid)
                r=mid
            else:
                l=mid+1
        return l
                
            

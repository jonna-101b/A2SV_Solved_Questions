class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        _sum=0
        costs=sorted(costs, key=lambda x:(x[0]-x[1]))
        print(costs)
 
        for i in range(len(costs)//2):
            _sum+=costs[i][0]

        for j in range(len(costs)-1,(len(costs)//2)-1,-1):
            _sum+=costs[j][1]

        return _sum
        

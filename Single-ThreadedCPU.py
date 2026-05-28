import heapq

class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        
        # attach index
        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        tasks.sort()
        
        res = []
        heap = []
        i = 0
        time = 0
        
        while i < n or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            
            while i < n and tasks[i][0] <= time:
                enqueue, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            
            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)
        
        return resSingle-Threaded CPU

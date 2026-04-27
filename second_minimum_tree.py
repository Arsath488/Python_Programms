from collections import deque, defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

      
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        
        queue = deque([(1, 0)])
        
        while queue:
            curr, steps = queue.popleft()
            
            for neighbor in adj[curr]:
                new_steps = steps + 1
                
               
                if new_steps < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = new_steps
                    queue.append((neighbor, new_steps))
          
                elif dist[neighbor][0] < new_steps < dist[neighbor][1]:
                    dist[neighbor][1] = new_steps
                    queue.append((neighbor, new_steps))
        
      
        steps_needed = dist[n][1]
        current_time = 0
        for _ in range(steps_needed):
           
            if (current_time // change) % 2 == 1:
                current_time = (current_time // change + 1) * change
            current_time += time
            
        return current_time

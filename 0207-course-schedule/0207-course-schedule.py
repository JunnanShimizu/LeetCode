class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        visited = set()
        
        for a, b in prerequisites: # Must take b to take a
            if a in prereqs:
                prereqs[a].append(b)
            else:
                prereqs[a] = [b]
            
        def dfs(current):
            if current in visited:
                return False
            if prereqs[current] == []:
                return True
            visited.add(current)
            for prereq in prereqs[current]:
                if not dfs(prereq): return False
            
            visited.remove(current)
            prereqs[current] = []
            return True
                    
        for n in range(numCourses):
            if not dfs(n): return False
            
        return True
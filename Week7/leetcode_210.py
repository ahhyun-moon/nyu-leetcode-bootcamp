class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Thought Process:
        # Use topological sort
        # Build adjacency list
        prereqs = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        # Course can have 3 status : visited, visiting (in path), not visited
        output = []
        visited, visiting = set(), set()
        def dfs(course):
            if course in visiting:
                return False # is a cycle
            if course in visited:
                return True 
            visiting.add(course)
            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []        
        return output
            


from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        postreq = defaultdict(list)
        precount = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            postreq[pre].append(course)
            precount[course] += 1
        
        order = []

        for i in range(numCourses):
            if precount[i] == 0:
                order.append(i)

        curid = 0
        while curid < len(order):
            curcourse = order[curid]
            for nxt in postreq[curcourse]:
                precount[nxt] -= 1
                if precount[nxt] == 0:
                    order.append(nxt)
            curid += 1

        if len(order) < numCourses:
            return []
        return order
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         # I thought you didn't need a queue but I was wrong
#         n = len(students)
#         q = deque(students)
#         sandwiches = deque(sandwiches)

#         count = 0
#         while count < len(q):
#             if q[0] == sandwiches[0]:
#                 q.popleft()
#                 sandwiches.popleft()
#                 count = 0
#             else:
#                 q.append(q.popleft())   # rotate through the students
#                 count += 1
#         return len(q)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # let's try this with a hashmap
        res = len(students)

        # create a hashmap with the counts of sandwiches wanted
        cnt = {}    
        for s in students:
            if not s in cnt:
                cnt[s] = 0
            cnt[s] += 1
        
        # now we have something like {0: 2, 1: 3}
        for sandwich in sandwiches:
            if not (sandwich in cnt) or (cnt[sandwich] == 0):
                break
            cnt[sandwich] -= 1
            res -= 1                
        

        return res


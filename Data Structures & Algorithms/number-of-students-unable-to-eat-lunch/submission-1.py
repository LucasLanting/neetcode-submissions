class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # I thought you didn't need a queue but I was wrong
        n = len(students)
        q = deque(students)
        sandwiches = deque(sandwiches)

        count = 0
        while count < len(q):
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.popleft()
                count = 0
            else:
                q.append(q.popleft())   # rotate through the students
                count += 1
        return len(q)



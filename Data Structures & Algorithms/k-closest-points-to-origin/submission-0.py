class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # do the quicksort algorithm on this bitch

        # no need to take square root since it's monotone increasing
        euclidean = lambda x: x[0]**2 + x[1]**2

        def partition(l,r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l   # i is the left pointer where the pivot ends up
            for j in range(l,r):
                if euclidean(points[j]) <= pivotDist:
                    # swap the values
                    points[j], points[i] = points[i], points[j]
                    i+=1
            # swap the pivot index with the value where the left pointer end up
            points[i], points[r] = points[r], points[i]
            return i

        L,R = 0, len(points)-1
        pivot = len(points)
        
        while pivot != k:
            pivot = partition(L,R)
            if pivot < k:
                L = pivot + 1
            else: # pivot > k
                R = pivot -1


        return points[:k]

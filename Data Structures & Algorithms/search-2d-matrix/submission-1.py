class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this is a matrix version of binary search 
        # just don't mess up edge cases and you're good

        # it would honestly be easiest to just flatten out the list of
        # lists and then run binary search. but we need O(log(m*n))

        # if you think about it there is a one-to-one mapping
        # from 2 index matrix index to 1 digit index
        # that mapping is all we have to master here

        # my convention m is the number of rowns, n is num of cols
        def index_to_num(m: int, n: int, index: List[int]) -> int:
            """Takes in the matrix index and gives which numeric index it corresponds to. Recall 0 indexing"""
            row = index[0]
            col = index[1]

            # note that we are returning a numeric index that starts at 0 too!
            return row*m + col

        def num_to_index (m: int, n: int, num = int) -> List[int]:
            """The numeric input is what linear index we have"""
            col = num % n
            row = (num-col)//n
            return [row, col]

        m = len(matrix)     # number of rows
        n = len(matrix[0])  # number of cols

        # I will do my pointers linearly for ease
        L,R = 0, m*n - 1

        while L<=R:
            M = (L+R)//2       # middle pointer
            row, col = num_to_index(m,n,M)  # pointer to row,col
            if matrix[row][col] < target:
                # search to the right
                L = M + 1
            elif matrix[row][col] > target:
                # search to the left of M
                R = M - 1
            else:
                # we matched it
                return True

        return False


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return_list = []
        a_it, b_it = 0, 0

        while a_it < len(A) and b_it < len(B):
            x, y = max(A[a_it][0], B[b_it][0]), min(A[a_it][1], B[b_it][1])

            if x <= y:
                return_list.append([x,y])
            if A[a_it][1] > B[b_it][1]:
                b_it += 1
            else:
                a_it += 1
        return return_list
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return_list = []

        while A and B:
            print("\nComparing {} and {}".format(A[0], B[0]))
            if A[0][0] >= B[0][0]:
                if B[0][1] >= A[0][0]:
                    return_list.append([A[0][0], min(A[0][1], B[0][1])])
                    print("Adding {}".format([A[0][0], min(A[0][1], B[0][1])]))
                print("Deleting {} from B".format(B[0]))
                B.pop(0)
            else:
                if A[0][1] >= B[0][0]:
                    return_list.append([B[0][0],  min(A[0][1], B[0][1])])
                    print("Adding {}".format([B[0][0], min(A[0][1], B[0][1])]))
                print("Deleting {} from A".format(A[0]))
                A.pop(0)
        return return_list
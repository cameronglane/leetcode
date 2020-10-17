class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negativeNumber = True
            x = abs(x)
        else:
            negativeNumber = False
        
        x = str(x)
        print("Output: " + x)
        x = x[::-1]
        x = int(x)

        if negativeNumber:
            x *= -1

        if x > 2147483647 or x < -2147483647:
            return 0
        return x
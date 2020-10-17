class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negativeNumber = True
            x *= -1
        else:
            negativeNumber = False
        xList = []
        multiplier = 1
        while x > 0:
            xList.append(x % 10)
            x = x // 10
            if x > 0:
                multiplier *= 10
        sum = 0
        xList.reverse()
        while len(xList) != 0:
            sum += xList.pop() * multiplier
            multiplier /= 10
        if negativeNumber:
            sum *= -1
        if sum > 2147483647 or sum < -2147483647:
            return 0
        return int(sum)
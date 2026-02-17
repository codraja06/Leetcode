class Solution(object):
    def reverse(self, x):
        v = str(x)
        if v[0] == "-":
            res = int("-" + v[:0:-1])
        else:
            res = int(v[::-1])

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

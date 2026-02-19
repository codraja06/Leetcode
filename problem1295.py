class Solution(object):
    def findNumbers(self, nums):
        n=[]
        for i in nums:
            if len(str(i)) % 2 == 0:
                n.append(i)
        return len(n)
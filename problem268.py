class Solution(object):
    def missingNumber(self, nums):
        actual=0
        given=0
        s=sorted(nums)
        start=s[0]
        end=len(nums)
        for i in nums:
            actual+=i
        for j in range(start,end+1):
             given+=j
        ans=given-actual
        return ans
class Solution:
    def palindrome(self,x :int)->bool:
        x=input()
        x=str(x)
        return x==x[::-1]


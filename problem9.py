class Solution:
    def palindrome(self,x :int)->bool:
        
        x=str(x)
        return x==x[::-1]


#Add Binary
a=str(input())
b=str(input())
c=int(a,2)+int(b,2)
print(bin(c)[2:])

class Solution(object):
    def addBinary(self, a, b):
         c=int(a,2)+int(b,2)
         return bin(c)[2:]
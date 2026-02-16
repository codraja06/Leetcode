#Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        p=s.split()
        o=p[::-1]
        return " ".join(o)   
#Roman to Integer
a=input()
s={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
b=0
for i in a:
    b+=int(s[i])
    print(b)

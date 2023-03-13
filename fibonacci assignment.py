num=[0,1] 
n=int(input("enter number"))
while num[-1]<=n:
    num.append(num[-1]+num[-2])
if num[-1]>n:
    num.pop()
print(num)

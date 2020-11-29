import math

n=input()
N=n.split(" ")
prices=input()
price = prices.split(" ")
items=math.floor(int(N[0])/2)
if int(price[1])>int(price[0]):
    if int(N[2])>items:
        ans=int(price[1])*items
    elif int(N[1])>items-int(N[2]):
        ans=(int(price[1])*int(N[2]))+(int(price[0])*(items-int(N[2])))
    else:
        ans=(int(price[1])*int(N[2]))+(int(price[0])*int(N[1]))
else:
    if int(N[1])>items:
        ans=int(price[0])*items
    elif int(N[2])>items-int(N[1]):
        ans=(int(price[0])*int(N[1]))+(int(price[1])*(items-int(N[1])))
    else:
        ans=(int(price[0])*int(N[1]))+(int(price[1])*int(N[2]))
print(ans)

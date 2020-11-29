import math

lst=[]
n=int(input())
input_string=input()
userList = input_string.split(" ")
for i in range(0,len(userList)):
    if(int(userList[i])<50):
        n=math.floor(n/2)
    else:
        n=2*n+1
#print(userList)
print(n)
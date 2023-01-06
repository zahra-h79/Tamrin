a=input()
temp=0
while(temp>10):
 for i in range(len(a)):
  temp +=int(a[i])
a=temp
temp=0
print(a)       

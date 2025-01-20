#  arr=[2,10,1,15,6]
# after sort [15,10,6,2,1]
# (15-10)+(10-6)+(6-2)+(2-1)
# sum =14



arr=[2,10,1,15,6]
length=len(arr)
for i in range(length):
    for j in range(0,length-1-i):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]        

print(arr)
su=0
new=0
for x in range(len(arr)-1):
    new=(arr[x]-arr[x+1])
    su=su+new 
print(su)
# 0 
# 2 4 
# 4 8 8
# 8 16 16 16

num=0
for x in  range(1,6):
    for i in range(x):
        if num==6:
            continue
        if i==0:
           print(" ")
           print(num, end=' ')
        else:
           print(num*2, end=' ') 
           
    num=num+2      
        
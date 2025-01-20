# print the character and count in a dictionary for repeated characters only
Strings = "Malayalam"
counts={}
output={}
for x in Strings:
    if x in counts:
        counts[x]+=1    
    elif x == 'm':
        counts['M']+=1
    else:
        counts[x]=1 

for i in counts:
    if  counts[i]==1:
        continue
    else:
        output[i]=counts[i]      
print(output)          
            
'''
Insertion sort
Sharath H N 
'''
n=list(map(int,input().split()))
p=len(n)
for i in range(1,p):
    k=n[i] #Store the current element
    j=i-1
    while(j>=0 and k<n[j]):# compare with all the previous elements. I f you find any element smaller than the current element, place the current element infront of it.
        n[j+1]=n[j]
        j-=1 
    n[j+1]=k 
    
print(n)

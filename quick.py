def Partition(L,l,r):
    temp=L[l]
    i=l 
    j=l+1 
    while(j<r):
        if L[j]>temp:
            j+=1 
        else:
            i+=1 
            temp1=L[i]
            L[i]=L[j]
            L[j]=temp1
            j+=1
    temp1=L[l] 
    L[l]=L[i]
    L[i]=temp1
    return i 
    
def quick(L,l,r):
    if l<r:
        p=Partition(L,l,r)
        quick(L,l,p)
        quick(L,p+1,r)
        
n=list(map(int,input().split()))
quick(n,0,len(n))
print(n)
import numpy as np
a=[10,6,7,9,15,11]
#a=[3,5,1,2,9,10,8,6,7]
#a=[5,3,9,7,8,6,12,11]
n=len(a)

opt=np.zeros((n+1,n+1))



for i in range(1,n+1):
    for j in range(i,n+1):
        opt[i][j]=max(opt[i-1][j],opt[i][j-1])
        if(opt[i][j]%2==0):
            if(a[i-1]>a[j-1]):
                opt[i][j]+=1
                break;
        else:
            if(a[i-1]<a[j-1]):
                opt[i][j]+=1
                break;

print opt[n][n]+1

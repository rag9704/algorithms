#merge sort
import numpy as np
def merge(A,q,r):
       n1=q+1
       n2=r-q
       L=np.zeros[n1]
       R=np.zeros[n2]
       for i in range(n1):
          L[i]=A[i]
       for j in range(n2):
          R[j]=A[q+j]
       L[n1+1]=1000*max(A)
       R[n2+1]=1000*max(A)
       i=0
       j=0
       for k in len(A):
          if L[i] <= R[j]:
              A[k]=L[i]
              i=i+1
          else :
              A[k]=R[j]
              j=j+1 

A=[1,2,25,13,46,89,36]
r=len(A)
q=int(input("from useer"))
merge(A,q,r);
    

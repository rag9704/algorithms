A=[1,5,99,4,8,89,36]
x=int(input("value"))
y=0
for i in range(0,len(A)):
    if ( A[i]== x) :
        print('x found at ',i+1)
        y=1

if y != 1 :
    print('nil')
    


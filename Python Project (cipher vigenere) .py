print("enter a divisor")
a=int(input())
arr=list()
i=0
while i<10:
    print("Please enter a number:")
    b=int(input())
    if((b%a)==0):
        arr.append(b)
    i=i+1;
c=len(arr)
for x in range(c):
    print(arr[x])





def hsum(n):
    sum=0
    i=1
    while i<=n:
        sum+=1/i
        i=i+1
    return sum
p = float(input("Enter the desired accuracy "))
i=1
while hsum(i+1)-hsum(i)>p:
    i=i+1
print("The sum upto {0} accuracy is {1}".format(p,hsum(i+1)))
print("The number of terms we need to add is",i+1)

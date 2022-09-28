# Write a python script to print first N odd natural numbers
i=1
n=int(input("Enter the number :"))
while i<=n:
    if i%2:
     print(i)
    i+=1 
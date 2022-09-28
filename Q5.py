# Write a python script to print first N odd natural numbers in reverse order
n=int(input("Enter the number :"))
i=n
while i>=1:
    if i%2:
        print(i)
    i-=1    
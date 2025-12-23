print("Factorial of a number")
n = int(input('Enter a number: '))
fact = 1
if(n < 0):
    print("Enter a postive number")
elif(n == 0):
    print(1)
else:
    for i in range(1, n+1):
        fact = fact * i
print(f"Factorial of {n} is: {fact} ")
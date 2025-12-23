print("Multiplication table of a number")
n = int(input('Enter a number: '))
mul = 0
for i in range(1 , 11):
    mul = n * i
    print(f"{n} X {i} = {mul}")
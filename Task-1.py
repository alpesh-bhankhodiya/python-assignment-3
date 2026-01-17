# using loop
a = int(input("Enter a Number : "))
b = 1

for i in range(1, a + 1):
    b = i * b

print(f"Factorial of {a} is {b}")





#using recursion
def fac(a1):
    if a1==0:
        return 1
    return a1*fac(a1-1)

x=int(input("Enter a Number : "))
a2=fac(x)
print(f"Factorial of {x} is {a2} ")
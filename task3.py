def swap(x,y):
    x,y = y,x
    return x,y

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
print("Values before swapping:-\n")
print("a=",a)
print("b=",b)

a,b=swap(a,b)

print("Values after Swapping:-\n")

print("a=",a)
print("b=",b)


# Main.py

from calc import calc

print("\n Choose an option")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("enter choice(1,2,3,4):")

a =float(input("enter number(a):"))
b =float(input("enter number(b):"))


if choice == "1":
    print(f"result: {calc.add(a,b)}")

elif choice == "2":
    print(f"result: {calc.subtract(a,b)}")

elif choice == "3":
    print(f"result:{calc.multiply(a,b)}")
    
elif choice == "4":
    print(f"result:{calc.devide(a,b)}")
else:
    print("invalid operation")
    
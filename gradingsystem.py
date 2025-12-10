print("welcome To Gradingsystem")
try:
    marks= int(input("Enter your marks (0-100):"))
except ValueError:
    print("enter number valid number")

if marks >=100:
    print("grade A+,Excellent")
elif marks >= 90:
    print("grade A,Excellent")
elif marks >= 80:
    print("grade B, very good")
elif marks >= 70:
    print("grade C,good")
elif marks >= 60:
    print("grade D,not bad put more effort")
else:
    print("grade F, can do better,put more effort")




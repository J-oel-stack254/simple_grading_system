#calc.py

class calc:

    def __init__(self):
        pass

    def add(self,a,b):
        return a+b
       
    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if a ==0:
            return "ZeroDivisionError cannot devide by zero"
        return a/b
    
    
calc =calc()
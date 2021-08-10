"""This is our first module about doc"""
Message = 'welcome to your own module'
f = 34
print(Message)
def multiply_two(a,b):
    """This is a multiply_two function which multiplies two numbers"""
    return('Multiplication is', a * b) 

def addition(*numbers):
    count = 0
    for i in numbers:
        count += i
    return 'addition is ' + str(count)
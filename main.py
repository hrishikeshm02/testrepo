import operation as ops

# from operation import Addition
# from operation import Substract
# from operation import Multiply
# from operation import Divide

input_a = int(input("Input a: "))
input_b = int(input("Input b: "))

print(f'Sum of a and b is:',ops.Addition(input_a,input_b))
print(f'Subtraction of a and b is:',ops.Substract(input_a,input_b))
print(f'Product of a and b is:',ops.Multiply(input_a,input_b))
print(f'Division of a and b is:',ops.Divide(input_a,input_b))

# print(f'Sum of a and b is:',Addition(input_a,input_b))
# print(f'Sum of a and b is:',Substract(input_a,input_b))
# print(f'Sum of a and b is:',Multiply(input_a,input_b))
# print(f'Sum of a and b is:',Divide(input_a,input_b))
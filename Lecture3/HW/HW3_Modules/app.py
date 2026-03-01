import calculator as cal

input_1 = 20
input_2 = 105

print('Hola! Lets test the calculator basic ops')
print(f'The addition: {cal.add(input_1,input_2)}')
print(f'The subtraction: {cal.subtract(input_1,input_2)}')
print(f'The multiplication: {cal.multiply(input_1,input_2)}')
print(f'The division: {cal.divide(input_1,input_2)}')

print('Hola! Lets test the calculator statistical ops')
print(f'The mean: {cal.mean([1,2,3,4,5,6,7,8,9,10])}')
print(f'The median: {cal.median([1,2,3,4,5,6,7,8,9,10])}')

# Menggunakan Higher Order Function
def apply(func, value):
    return func(value)

def add_five(value):
    return value + 5

result = apply(add_five, 10)
print(result) # Output: 15


# Menggunakan Lambda Function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]


# Menggunakan List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

import random

def generate_example():
    
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(['+', '-'])
    
    if operation == '+':
        result = a + b
    else:
        result = a - b
    
    example = f"{a} {operation} {b} = {result}"
    return example

num_examples = random.randint(5, 10)
examples = [generate_example() for _ in range(num_examples)]

for example in examples:
    print(example)
import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(number_list, quantity = 1):
    
    numbers_add = 0 
    new_list = []
    while numbers_add < quantity:
        new_number = random.uniform(0.0, 100.0)
        new_list.append(round(new_number, 1))
        numbers_add += 1
    number_list.extend(new_list)

main();
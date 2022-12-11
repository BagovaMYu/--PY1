from random import randint

def get_unique_list_numbers(req_length=15) -> list[int]:
    unique_list_numbers = []
    while len(unique_list_numbers) < req_length + 1:
        number = randint(-10, 10)
        if number not in unique_list_numbers:
            unique_list_numbers.append(number)

    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

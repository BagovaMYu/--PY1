def delete(list_, index=None):
    if str(index).isdigit():
        list_result = list_[:index] + list_[index+1:]
    else:
        list_result = list_[:-1]

    return list_result

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

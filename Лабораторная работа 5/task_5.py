import random
import string

def get_random_password(length=8) -> str:
    all_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(random.sample(all_symbols, length))
    return password


print(get_random_password())

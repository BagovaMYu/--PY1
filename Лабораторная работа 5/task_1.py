from pprint import pprint

max_num = 15

dict_systems = [{
    "bin": bin(num),
    "dec": int(num),
    "hex": hex(num),
    "oct": oct(num)} for num in range(max_num + 1)]

pprint(dict_systems)

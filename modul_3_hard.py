data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(*args):
    calculate_sum = 0
    for info in args:
        if isinstance(info, int):
            calculate_sum += info
        elif isinstance(info, str):
            calculate_sum += len(info)
        elif isinstance (info,(tuple, set, list)):
            calculate_sum += calculate_structure_sum(*info)
        elif isinstance(info, dict):
            calculate_sum += calculate_structure_sum(*info.items())
        elif info is None:
            pass
    return calculate_sum

result = calculate_structure_sum(data_structure)

print(result)







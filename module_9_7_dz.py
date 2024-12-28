def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        sum_ = sum(args)
        if sum_ % 2 == 0:
            print("Простое")
        else:
            print("Состовное")
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
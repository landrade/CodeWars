def is_prime(num):
    return len([x for x in range(1, num + 1) if num % x == 0]) == 2
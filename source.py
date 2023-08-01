def is_ascending(n: int) -> bool:
    while n > 0:
        if n % 10 <= (n // 10) % 10:
            return False
        n //= 10
    return True

def no_zeros(n: int) -> bool:
    return '0' not in str(n)

def is_odo_num(n: int) -> bool:
    return is_ascending(n) and no_zeros(n)

smallest = [0, 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678]
largest = [0, 9, 89, 789, 6789, 56789, 45789, 3456789, 23456789]
smallest_and_largest = list(zip(smallest, largest))

def all_odo_num(num_dig: int) -> list[int]:
    smallest, largest = smallest_and_largest[num_dig - 1]
    return [i for i in range(smallest, largest + 1) if is_odo_num(i)]

def next_reading(n: int) -> int:
    odo_nums = all_odo_num(len(str(n)))
    return odo_nums[odo_nums.index(n) + 1]

def prev_reading(n: int) -> int:
    odo_num = all_odo_num(len(str(n)))
    return odo_num[odo_num.index(n) - 1]

def nth_reading_before(num: int, r: int):
    n = len(str(num))
    odo_num = all_odo_num(n)
    return odo_num[odo_num.index(num) - r]

def nth_reading_after(num: int, r: int):
    n = len(str(num))
    odo_num = all_odo_num(n)
    return odo_num[odo_num.index(num) + r]

def distance(a: int, b: int) -> int:
    odos = all_odo_num(len(str(a)))
    if odos.index(b) > odos.index(a):
        return odos.index(b) - odos.index(a)
    return (odos.index(b) + odos.index(a) + 2) % len(odos)

def revert_int_option_1(num):
    return int("".join(list(reversed(str(num)))))


def revert_int_option_2(num):
    return int(str(num)[::-1])


print(revert_int_option_1(12345))
print(revert_int_option_2(12345))

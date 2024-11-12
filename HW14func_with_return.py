print('2.a:')


def my_avg(a: int = 0, b: int = 0):
    """A function that accepts 2 parameters and returns their average"""
    average = a + b / 2
    return average


help(my_avg)
avg1 = my_avg(90, 99)
print(f'the average is: {avg1}')

print('b:')


def my_headline(wort: str):
    return wort.upper() + '!'


head1 = my_headline('python has concurred the world')
print(head1)

print('c:')


def concat_list(a_list: list[int], b_list: list[int], c_list: list[int]):
    all_list: list[int] = a_list + b_list + c_list
    return all_list


res_con = concat_list([1, 2], [3, 4, 5, 6, ], [7, 8, 9, ])
print(f'the list is: {res_con} end her len is: {len(res_con)}')

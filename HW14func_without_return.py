print('1.a:')


def my_ascending(x: int = 1, y: int = 1):
    for i in range(x, y + 1):
        print(i, end=' ')


my_ascending(-12, 7)

print('b:')


def my_details(string: str):
    center: int = len(string) // 2
    middle = string[center]
    end: int = string[-1]
    start: int = string[0]
    print(f'the first len: {start} ,the middle len: {middle} ,and the last len: {end}')


my_details("AI is the best")

print('c:')


def say_bool(a: bool = bool):
    if a == True:
        print('yes')
    else:
        print('no')


say_bool(True)
say_bool(False)

print('d:')


def print_zugi(list_zugi: list[int]):
    for num in list_zugi:
        if num % 2 == 0:
            print('even')
        else:
            print('odd')


print_zugi([5, 3, 2, 10, 15, 14, 14])

print('e:')


def my_statistics(grads: list[int]):
    print('the highest score:', max(grads))
    print('the lowest score', min(grads))
    print('the amount of grades:', sum(grads))
    print('The grade point average:', sum(grads) / len(grads))


stem_list: list[int] = []
while True:
    x: int = int(input('grade:'))
    if x == -99:
        break
    if 0 < x < 100:
        stem_list.append(x)

    else:
        continue
my_statistics(stem_list)

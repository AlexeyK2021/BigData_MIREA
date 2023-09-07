access = dict()


def add_access(file, mode):
    mode_num = 0
    for i in mode:
        if i == "r":
            mode_num += 1
        elif i == "w":
            mode_num += 2
        elif i == "x":
            mode_num += 4
    access[file] = mode_num


def check_access(file, mode):
    mode_num = 0
    if mode == "read" and access[file] % 2 == 1:
        return "OK"
    elif mode == "write" and access[file] // 2 % 2 == 1:
        return "OK"
    elif mode == "execute" and access[file] // 4 == 1:
        return "OK"

    return "Access denied"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        data = input().split(" ")
        add_access(data[0], data[0:])

    m = int(input())
    for i in range(m):
        data = input().split(" ")
        print(check_access(data[1], data[0]))

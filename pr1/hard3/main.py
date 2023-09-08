access = dict()


def add_access(file, mode):
    access[file] = mode


def check_access(file, mode):
    if access.get(file, 0) == 0:
        return "Access denied"

    if mode == "read" and "r" in access[file]:
        return "OK"
    elif mode == "write" and "w" in access[file]:
        return "OK"
    elif mode == "execute" and "x" in access[file]:
        return "OK"
    return "Access denied"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        data = input()
        file = data[:data.find(" ")]
        mode = data[data.find(" ") + 1:]
        add_access(file, mode)

    m = int(input())
    for i in range(m):
        data = input()
        op = data[:data.find(" ")]
        file = data[data.find(" ") + 1:]
        print(check_access(file, op))

user_db = dict()


def check_name(name):
    if user_db.get(name) is None:
        user_db[name] = 0
        return "OK"
    else:
        user_db[name] += 1
        new_name = name + str(user_db[name])
        user_db[new_name] = 0
        return new_name


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        username = input()
        print(check_name(username))

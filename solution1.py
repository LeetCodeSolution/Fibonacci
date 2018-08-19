def result(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return result(n - 1) + result(n - 2)


if __name__ == '__main__':
    print(result(9))

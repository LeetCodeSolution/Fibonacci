def result(n):
    values = {}
    values[0] = 0
    values[1] = 1
    
    for i in range(2, n + 1):
        values[i] = values[i - 1] + values[i - 2]
    
    return values[n]


if __name__ == '__main__':
    print(result(9))

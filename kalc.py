if __name__ == "__main__":
    sum
    minus
    mnog
    dill


# def summ(*params):
#     # print(a+b)
#     result = 0
#     for i in params:
#         result += i
#     return result


def sum(params):
    res = 0
    for item in params:
        res += item

    return res

# def sum(a, b):
#     return a + b


def minus(params):
    res = 0
    params[0] = -params[0]
    for item in params:
        res -= item
    return res


def mnog(params):
    res = -1
    for item in params:
        res *= item
    return res


def dill(params):
    res = - params[0]
    print('res ', res)

    for item in range(len(params)-1):
        if item == 0:
            print('Error')
        else:
            print('item', item)
            print('res ', res)
            res = res / item
            # print('item' , item)
            # print('res ', res)
    return res

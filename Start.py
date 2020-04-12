from kalc import sum, minus, mnog, dill

# param = set(input('Input: ').split())
# print('Param ', param)
# params=[int(item) for item in param]
# print('Params ', params)

param = input('Enter numbers: ').split()
print('Param ', param)

params = [int(item) for item in param]
print('Params ', params)

c = int(input('Enter diu: '))

rres = sum(params)
result = minus(params)
mnogg = mnog(params)
dil = dill(params)

if c == 1:
    print('Suma', rres)

elif c == 2:
    print('Riznuzia', result)

elif c == 3:
    print('Mnogenia', mnogg)

elif c == 4:
    print('Dilenia', dil)

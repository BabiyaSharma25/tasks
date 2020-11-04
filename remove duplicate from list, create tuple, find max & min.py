list_in = [87, 77, 42, 88, 87, 77, 42]
list_inp = list(set(list_in))
print('unique list :', str(list_inp))


def convert(list_in):
    return tuple(list_in)

i = convert(list_inp)
print('tuple :',str(i))

minimum = min(list_inp)
print('min',str(minimum))

maximum = max(list_inp)
print('max',str(maximum))





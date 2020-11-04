def outer(a, b):
    def inner(a,b):
        return a+b
    add = inner(a, b)
    return add+5

result = outer(70, 100)
print(result)
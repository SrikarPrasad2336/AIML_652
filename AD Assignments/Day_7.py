def dev_dec(func):
    def inner(a,b):
        if b==0:
            return "Division By Zero is not Possible"
        return func(a,b)
    return inner
@div
def ans(a,b):
    return a/b
print(ans(8,0))


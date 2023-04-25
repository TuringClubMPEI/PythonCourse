
def deco(): # <- фабрика декораторов
    def _wrapper(func): # <-- Cам декоратора
        def __wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return __wrapper
    return _wrapper

class A:

    @deco()
    def meth(self, a):
        print(a)


if __name__ == '__main__':
    a = A()
    a.meth(11)

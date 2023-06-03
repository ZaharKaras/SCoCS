class DefenerVector:
    def __init__(self, v):
        self.__v = v
 
    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return True


v1 = [1, 2, 3]
with DefenerVector(v1) as dv:
    for i in enumerate(dv):
        dv[0] += 1
 
print(v1)

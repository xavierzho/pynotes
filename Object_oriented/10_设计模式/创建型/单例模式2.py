class SingLeTon:
    # _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingLeTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


d = SingLeTon
print(id(d))
print(id(d))
print(id(d))
print(id(d))

class ONone:
    def __getattribute__(self, *args, **kwargs):
        return ONone()

    def __getitem__(self, key):
        return ONone()

    def __str__(self):
        return ''

    def __repr__(self):
        return ''

    def __bool__(self):
        return False


class OInt(int):
    def __getattribute__(self, key):
        try:
            value = super(OInt, self).__getattribute__(key)
        except AttributeError as ae:
            value = ONone()
        return value


class OString(str):
    def __getattribute__(self, key):
        try:
            value = super(OString, self).__getattribute__(key)
        except AttributeError as ae:
            value = ONone()
        return value


class ODict(dict):
    def __init__(self, d: dict, **kwargs):
        for key, value in d.items():
            setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __getattribute__(self, key):
        try:
            value = super(ODict, self).__getattribute__(key)
        except AttributeError as ae:
            value = ONone()
        return value

    def __setattr__(self, key, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(ODict, self).__setattr__(key, value)


class OList(list):
    def __getitem__(self, key):
        try:
            value = super(OList, self).__getitem__(key)
        except IndexError as ie:
            value = ONone()
        if type(value) is int:
            value = OInt(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        return value

    def __getattribute__(self, key):
        try:
            value = super(OList, self).__getattribute__(key)
        except AttributeError as ae:
            value = ONone()
        if type(value) is int:
            value = OInt(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        return value

    def __setattr__(self, key, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(ODict, self).__setattr__(key, value)

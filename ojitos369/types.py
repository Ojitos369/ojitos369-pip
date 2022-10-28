import uuid
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


class OFloat(float):
    def __getattribute__(self, key):
        try:
            value = super(OFloat, self).__getattribute__(key)
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
    __helper__ = {}
    
    def __init__(self, d: dict = {}, **kwargs):
        unique_key = str(uuid.uuid4())
        self.__helper__[unique_key] = {}
        self.__unique_key__ = unique_key
        for key, value in d.items():
            setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __to_dict__(self):
        me = self.__dict__
        h = self.__helper__[self.__unique_key__]
        sum = {}
        sum.update(me)
        sum.update(h)
        del sum['__unique_key__']
        return sum
    
    def __add__(self, val):
        r_val = None
        try:
            r_val = self.__to_dict__() + val
        except:
            r_val = val
        return r_val

    def __sub__(self, val):
        r_val = None
        try:
            r_val = self.__to_dict__() - val
        except:
            r_val = -val
        return r_val

    def __str__(self):
        return str(self.__to_dict__())

    def __repr__(self):
        return str(self.__to_dict__())

    def __getattribute__(self, key):
        try:
            value = super(ODict, self).__getattribute__(key)
        except AttributeError as ae:
            try:
                value = self.__helper__[self.__unique_key__][key]
            except:
                value = ODict()
                self.__setattr__(key, value)
        return value
    
    def __bool__(self):
        if len(self.__to_dict__()) == 0:
            return False
        return True

    def __setattr__(self, key, value):
        number = False
        try:
            r = float(key)
            number = True
        except:
            pass
        
        if number:
            self.__helper__[self.__unique_key__][key] = value
            return
        
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(ODict, self).__setattr__(key, value)
    
    def keys(self):
        return self.__to_dict__().keys()
    
    def update(self, d: dict):
        for key, value in d.items():
            self.__setattr__(key, value)
    
    def dict(self):
        from ast import literal_eval
        mystr = str(self)
        this_dict = literal_eval(mystr)
        return this_dict


class OList(list):
    def __getitem__(self, key):
        try:
            value = super(OList, self).__getitem__(key)
        except IndexError as ie:
            value = ONone()
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
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
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        return value

    def append(self, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(OList, self).append(value)
    
    def insert(self, index, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(OList, self).insert(index, value)

    def __setitem__(self, key, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(OList, self).__setitem__(key, value)

    def __setattr__(self, key, value):
        if type(value) is int:
            value = OInt(value)
        elif type(value) is float:
            value = OFloat(value)
        elif type(value) is str:
            value = OString(value)
        elif type(value) is list:
            value = OList(value)
        elif type(value) is dict:
            value = ODict(value)
        super(OList, self).__setattr__(key, value)


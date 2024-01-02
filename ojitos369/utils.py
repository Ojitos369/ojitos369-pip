import uuid
import json
import datetime
import functools
from inspect import currentframe


def printwln(*args, **kwargs):
    """Print with the origin line number"""
    cf = currentframe()
    line = cf.f_back.f_lineno
    print(f"ln {line}: ", *args, **kwargs)


def print_line_center(text: str) -> str:
    print()
    print(text)
    print()
    return f'\n{text}\n'


def get_unique_key():
    return str(uuid.uuid4())


def print_prev(*args, **kwargs):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(CURSOR_UP_ONE, end='')
    print(ERASE_LINE, end='')
    print(*args, **kwargs)


def print_json(object: dict):
    # with datetime objects
    json_object = json.dumps(object, indent=4, default=str)
    print(json_object)


def valida_dato(dato: any):
    if str(dato).lower == 'nan' or str(dato).lower == 'none' or str(dato).lower == 'undefined' or str(dato).lower == 'null' or str(dato).lower == '':
        return None
    else:
        return dato


def get_d(d: dict, key: str, none=False, to_parse=None, *args, **kwargs) -> any:
    """Validate field in dict and return it or a certain value"""
    if key in d and d[key] is not None:
        if to_parse:
            try:
                return to_parse(d[key])
            except:
                return d[key]
        return d[key]
    elif 'default' in kwargs:
        return kwargs['default']
    elif none:
        return None
    else:
        raise Exception(f'Error: "{key}" not found')


def get_separated_number(n: any) -> str:
    """Return a separated number string"""
    n = str(n).replace(' ', '')
    try:
        n = float(n)
    except:
        raise Exception('Cannot convert to number')
    return f'{n:,.2f}'


def get_currency(n: any) -> str:
    """Return a currency string"""
    n = str(n).replace(' ', '')
    try:
        n = float(n)
    except:
        raise Exception('Cannot convert to number')

    n_final = round(n, 2)
    n_final = ('-' if n_final < 0 else '') + \
        f'$ {get_separated_number(abs(n_final))}'
    return n_final


def destructure_d(*args, **kwargs):
    """get value from names varialbes if exist in dictionary else get None
    Args: 
        1.- position de dict to get values
        2.- a list with variables names or values separated with ,
    
    Examples:
        d_1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
        a,b,g,c = destructure_d(d_1, 'a','b','g','c')
        a >> 1
        b >> 2
        g >> None
        c >> 3

        a,e,d1,d2 = destructure_d(d_1, ['a','e','d1','d2'])
        a >> 1
        e >> 5
        d1 >> None
        d2 >> None
    """
    args = list(args)
    the_dict = args.pop(0)
    
    values = []
    if type(args[0]) == list:
        for key in args[0]:
            values.append(get_d(the_dict, key, default=None))
    else:
        for key in args:
            values.append(get_d(the_dict, key, default=None))
    return values


def generate_token(length: int = 225, exclude: list = []) -> str:
    """Generate a random token with a certain length and excluding some characters
        Args:
            length (int, optional): Length of the token. Defaults to 225.
            exclude (list, optional): List of characters to exclude. Defaults to [].
        Returns:
            str: Token
    """
    if type(exclude) == str:
        exclude = list(exclude)
    exclude += ['"', "'", '\\', '`', ';', ',', ' ', '']
    # Import lyrics, numbers and symbols
    from string import ascii_letters, digits, punctuation
    import random
    
    for e in exclude:
        ascii_letters = ascii_letters.replace(e, '')
        digits = digits.replace(e, '')
        punctuation = punctuation.replace(e, '')
    
    max_length = max(len(ascii_letters), len(digits), len(punctuation))
    ascii_letters = (ascii_letters * (int(max_length // len(ascii_letters) ) + 1))[0:max_length]
    digits = (digits * (int(max_length // len(digits) ) + 1))[0:max_length]
    punctuation = (punctuation * (int(max_length // len(punctuation) ) + 1))[0:max_length]
    
    options = ascii_letters + digits + punctuation
    options = options
    # pln(f'options: {options}')
    
    token = ''
    for _ in range(length):
        token += random.choice(options)
    # pln(token)
    return token


@functools.lru_cache()
def str_to_date(date_str: str) -> datetime.datetime:
    if not date_str:
        return None
    # Convertir fecha en formato ISO 8601 a un formato legible por datetime.datetime.strptime
    if date_str.endswith("Z"):
        date_str = date_str[:-1] + "+00:00"
    date_str = date_str.replace("T", " ")
    formats = [
        "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d",
        "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y",
        "%Y/%m/%d %H:%M:%S", "%Y/%m/%d %H:%M", "%Y/%m/%d",
        "%d-%m-%Y %H:%M:%S", "%d-%m-%Y %H:%M", "%d-%m-%Y",
    ]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError("No se pudo convertir la fecha")



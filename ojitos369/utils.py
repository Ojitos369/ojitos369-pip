import uuid
import json
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


def get_d(d: dict, key: str, default = None, none = False, to_parse = None) -> any:
    """Validate field in dict and return it or a certain value"""
    if key in d and d[key] is not None:
        if to_parse:
            return to_parse(d[key])
        return d[key]
    elif default != None:
        return default
    elif none:
        return None
    else:
        raise Exception(f'Error: "{key}" not found')


def get_separated_number(n: any) -> str:
    """Return a separated number string"""
    try:
        n = float(n)
    except:
        raise Exception('Cannot convert to number')
    return f'{n:,.2f}'


def get_currency(n: any) -> str:
    """Return a currency string"""
    try:
        n = float(n)
    except:
        raise Exception('Cannot convert to number')
    
    n_final = round(n, 2)
    n_final = ('-' if n_final < 0 else '') + f'$ {get_separated_number(abs(n_final))}'
    return n_final


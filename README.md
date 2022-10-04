### Errors Catch

```py

from ojitos369.errors import CatchErrors as CE
email_settings = {
    "smtp_server": "your.server-smtp.com",
    "port": port_from_your_server,
    "sender": "email_from_by_sender@email.com",
    "receiver": "email_to_recive@email.com",
    "password": "the_sender_password",
}

ce = CE(name_project = "your project's name", email_settings = email_settings)


try:
    # your code
except Exception as e:
    ce.show_error(e, send_email = True)

```

### Utils

```py
from ojitos369.utils import (
    printwln,
    print_line_center,
    get_unique_key,
    print_json,
    valida_dato,
    get_d
)


```

#### printwln
```py

# printwln -> print with the current line at the start
printwln("Hello world")
# >> ln 1: Hello world

```

#### print_line_center
```py

# print_line_center -> print your text between spaces
# and get de text
print('start')
text = print_line_center("Hello world")
print('end')
# >> start
# >> 
# >> Hello world
# >> 
# >> end
print('start')
print('hi')
print(text)
print('end')
# >> start
# >> hi
# >>
# >> Hello world
# >>
# >> end

```

#### get_unique_key
```py

# get_unique_key -> get a unique key base on uuid4
key = get_unique_key()
# >> key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

```

#### print_json
```py

# print_json -> print a json with indent
print_json({"name": "ojitos369"})
# >> {
# >>     "name": "ojitos369"
# >> }

```

#### valida_dato
```py

# valida_dato -> if dato is NaN, None, null, '' or undefined return None else return dato
dato = valida_dato(None)
# >> dato
# >> None
dato = valida_dato('undefined')
# >> dato
# >> None
dato = valida_dato('ojitos369')
# >> dato
# >> 'ojitos369'

```

#### get_d
```py

# get_d -> validate field in dict or return a certain value
data = {
    "name": "ojitos369",
    "single": True
}

print(get_d(data, 'name'))
# >> ojitos369

print(get_d(data, 'single', to_parse = str))
# >> "True" # type str

print(get_d(data, 'single'))
# >> True # type bool


print(get_d(data, 'age', default = 18))
# >> 18

print(get_d(data, 'age', none = True))
# >> None

print(get_d(data, 'age'))
# Exception
# Error: "age" not found

```

### Databases

#### Oracle

```py

from ojitos369.db_connections import ConexionOracle

db_data = {
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'scheme': 'your_scheme_name',
}
conexion = ConexionOracle(db_data)

conexion.consulta(query, params=None) # return a list of list with the result of the query
# >> [["ojitos369", 18], ["ojitos369", 18]]
conexion.consulta_asociativa(query, params=None) # return a list of dict with the result of the query
# >> [{"name": "ojitos369", "age": 18}, {"name": "ojitos369", "age": 18}]
conexion.preparar_transaccion(query) # prepare transaction with query
# >> Bool
conexion.ejecutar(parametros = None) # execute transaction prepared with preparar_transaccion
# >> Bool

conexion.paginador(query, registros_pagina = 1, pagina = 2, params = None) # return de n resutls of query
# >> {
# >>     'registros': [{"name": "ojitos369", "age": 18, "rnum": 2}],
# >>     'num_registros': 2,
# >>     'paginas': 2,
# >>     'pagina': 2,
# >> }

conexion.commit() # commit transaction
conexion.rollback() # rollback transaction
conexion.close() # close connection

```
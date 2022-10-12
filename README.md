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
    print_json,
    print_prev,
    get_unique_key,
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


#### print_json
```py

# print_json -> print a json with indent
print_json({"name": "ojitos369"})
# >> {
# >>     "name": "ojitos369"
# >> }

```


#### print_prev
```py

# print_prev -> print in the previous line
print_prev("Hello world")
print_prev("Bye world")
# Firts
# >>
# >> Hello world
# >>

# Second
# >>
# >> Bye world
# >>




```


#### get_unique_key
```py

# get_unique_key -> get a unique key base on uuid4
key = get_unique_key()
# >> key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

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
pip install ojitos369_oracle_db
```
[REPO: https://github.com/Ojitos369/ojitos369_oracle_db](https://github.com/Ojitos369/ojitos369_oracle_db)


```py

from ojitos369_oracle_db.oracle_db import ConexionOracle

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


### FTP  

```py
pip install ojitos369_ftp
```
[REPO: https://github.com/Ojitos369/ojitos369_ftp](https://github.com/Ojitos369/ojitos369_ftp)

```py


from ojitos369_ftp.ftp import ConnectionFtp

ftp_data = {
    'host': 'your_ftp_host',
    'port': 'your_ftp_port',
    'user': 'your_ftp_user',
    'password': 'your_ftp_password',
}
ftp = ConnectionFtp(ftp_data)

ftp.mkdir('some_path')
ftp.cd('some_path')

ftp.upload('~/files/your.file', '.'): # upload your.file into some_path (ftp)
ftp.ls()
# >> ['your.file']
ftp.cd('..')
ftp.clear_dir('some_path')
ftp.ls('some_path')
# >> []

ftp.rmdir('some_path')


ftp.rm('some.file')

ftp.pwd()
# >> 'actual_ftp_dir

ftp.rename('your.file', 'your_2.file')
ftp.mv('your.file', 'some_path')

ftp.ls('some_path')
# >> ['your.file', 'your_2.file']
ftp.ls('some_path_2')
# >> []

ftp.mv_files('some_path', 'some_path_2')
ftp.ls('some_path')
# >> []
ftp.ls('some_path_2')
# >> ['your.file', 'your_2.file']

ftp.cp('some_path/your.file', '~/files/your.file')

ftp.close()


```

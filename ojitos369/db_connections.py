import math
import cx_Oracle

class ConexionOracle:
    def __init__(self, db_data):
        db_conn = cx_Oracle.connect(db_data['user'] + '/' + db_data['password'] + '@' + db_data['host'] + '/' + db_data['scheme'])
        print('##### Activando DB #####')

        self.cursor = db_conn.cursor()
        self.db_conn = db_conn

    def consulta(self, query, params=None):
        self.query = query
        self.parametros = params
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def consulta_asociativa(self, query, params=None):
        self.query = query
        self.parametros = params
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        descripcion = [d[0].lower() for d in self.cursor.description]
        # print(descripcion)
        resultado = [dict(zip(descripcion, linea)) for linea in self.cursor]
        # print(resultado)
        return resultado

    def preparar_transaccion(self, query):
        self.query = query
        try:
            self.cursor.prepare(query)
            #print(self.cursor.statement)
            return True
        except Exception as e:
            # ex = Exception(f'{print_line_center(str(e))}{print_line_center(self.query)}{print_line_center(self.parametros)}')
            # print(str(ex))
            # show_error(ex, send_email = True)
            print(e)
            self.db_conn.rollback()
            return False

    def ejecutar(self, parametros = None):
        self.parametros = parametros
        try:
            if not parametros:
                self.cursor.execute(None)
                # print(self.cursor.bindvars)
                return True
            else:
                if isinstance(parametros, dict):
                    self.cursor.execute(None, parametros)
                    # print(self.cursor.bindvars)
                elif isinstance(parametros, list):
                    self.cursor.executemany(None, parametros)
                    # print(self.cursor.bindvars)
                else:
                    raise Exception('Parametros: tipo no valido')
                return True
        except Exception as e:
            # ex = Exception(f'{print_line_center(str(e))}{print_line_center(self.query)}{print_line_center(self.parametros)}')
            # print(str(ex))
            # show_error(ex, send_email = True)
            print(e)
            self.db_conn.rollback()
            return False

    def commit(self):
        try:
            self.db_conn.commit()
            return True
        except Exception as e:
            # ex = Exception(f'{print_line_center(str(e))}{print_line_center(self.query)}{print_line_center(self.parametros)}')
            # print(str(ex))
            # show_error(ex, send_email = True)
            print(e)
            self.db_conn.rollback()
            return False

    def rollback(self):
        self.db_conn.rollback()
        return True
    
    def close(self):
        self.db_conn.close()
        return True

    def paginador(self, query, registros_pagina = 10, pagina = 1, params = None):
        try:
            # print(query)
            if params:
                num_registros = len(self.consulta_asociativa(query, params))
            else:
                num_registros = len(self.consulta_asociativa(query))
            paginas = math.ceil(num_registros/registros_pagina)
            if paginas < pagina: pagina = paginas
            limite_superior = registros_pagina * pagina
            limite_inferior = limite_superior - registros_pagina + 1

            query = ''' SELECT *
                        FROM (SELECT a.*, ROWNUM rnum
                                FROM ({0}) A)
                        WHERE rnum BETWEEN {2} AND {1}
                    '''.format(query,
                            limite_superior,
                            limite_inferior)
            self.query = query
            self.parametros = params
            if params:
                registros = self.consulta_asociativa(query, params)
            else:
                registros = self.consulta_asociativa(query)

            if num_registros < registros_pagina:
                pagina = 1
            return {
                'registros': registros,
                'num_registros': num_registros,
                'paginas': paginas,
                'pagina': pagina,
            }
        except Exception as e:
            # ex = Exception(f'{print_line_center(str(e))}{print_line_center(self.query)}{print_line_center(self.parametros)}')
            # print(str(ex))
            # show_error(ex, send_email = True)
            print(e)
            return False



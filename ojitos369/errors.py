import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class ErrorEmail:
    def __init__(self, message, email_settings, name_project='No hay nombre del projecto'):
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP_SSL(email_settings['smtp_server'])
        self.server.login(email_settings['user'], email_settings['password'])
        self.message = message
        self.sender = email_settings['sender']
        self.subject = f'ERROR EN {name_project}'
        self.receiver = email_settings['receiver']

    def send(self):
        self.msg['From'] = self.sender
        self.msg['Subject'] = self.subject
        self.msg['To'] = self.receiver
        self.msg.attach(MIMEText(self.message, 'plain'))
        self.server.sendmail(
            self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()


class CatchErrors:
    def __init__(self, name_project: str = 'No hay nombre del projecto', email_settings: dict = None, root_path: str = None):
        self.name_project = name_project
        self.email_settings = email_settings
        self.root_path = str(root_path)
        if not self.email_settings:
            self.email_available = False
        else:
            self.email_available = True

    def show_error(self, e: Exception, send_email: bool = False, root_path: str = None, extra: str = '') -> str:
        import os
        import datetime
        if root_path:
            self.root_path = str(root_path)

        com_path = '' if not self.root_path else self.root_path
        if com_path.endswith('/'):
            com_path = com_path[:-1]

        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        info_exc = os.sys.exc_info()
        et, eo, et = info_exc
        errs = []
        errs.append(['file', 'line', 'function', 'code'])
        paths = []
        codes = []
        max_len = 0
        max_file = 0
        max_func = 0
        while (et):
            file = et.tb_frame.f_code.co_filename
            line = et.tb_lineno
            function_data = str(et.tb_frame).split()
            function_data = function_data[-1][:-1]
            
            class_data = et.tb_frame.f_locals
            class_data = class_data['self'] if 'self' in class_data else ''
            if class_data:
                class_data = str(class_data.__class__)
                class_data = class_data.split("'")[1]

            code = ''
            with open(file, 'r') as f:
                Lines = f.readlines()
                code_text = Lines[line - 1].replace('\n', '')
                try:
                    ant = Lines[line - 2].replace('\n', '')
                except:
                    ant = ''
                try:
                    aft = Lines[line].replace('\n', '')
                except:
                    aft = ''
                codes.append(
                    f'{line - 1}: {ant}\n{line}: {code_text}\n{line + 1}: {aft}')

            # Validate root path
            p = file.split('/')[:-1]
            ac_path = '/'.join(p)
            if not self.root_path:
                if not com_path:
                    com_path = ac_path

                if ac_path != com_path and ac_path not in paths:
                    paths.append(ac_path)
                    ant = com_path.split('/')
                    new = []
                    for a, b in zip(p, ant):
                        if a != b:
                            break
                        else:
                            new.append(a)
                    com_path = '/'.join(new)

            code_text = code_text.replace('\n', '')
            max_len = max(len(code_text), max_len)
            max_file = max(len(file), max_file)
            max_func = max(len(function_data), max_func)
            errs.append([f'{file}:{line}', class_data, function_data, code_text])
            et = et.tb_next

        traceback = ''
        tb = ''
        max_file = max_file - len(com_path)

        i = 0
        for row in errs:
            p = row.pop(0)
            p = p.replace(com_path + '/', '')
            if i > 0:
                row[len(row) - 1] = codes[i-1]
                tb += 'file: {}\tclass: {}\tfunc: {}\tcode: \n{}\n\n'.format(
                    p, *row)
            else:
                tb += '\n'
            i += 1

        extra = f'Extra: {extra}\n' if extra else ''
        error = f'ERROR INFO\nTipo: {et}\nCommon Path: {com_path}\n{tb}\nError: {e}\n{extra}Fecha: {now}'
        if send_email:
            if not self.email_available:
                return 'No hay configuración de email'
            email = ErrorEmail(error, self.email_settings, self.name_project)
            try:
                email.send()
            except:
                return 'Revise los datos del email'

        return error

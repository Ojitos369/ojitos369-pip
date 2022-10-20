import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class ErrorEmail:
    def __init__(self, message, email_settings, name_project = 'No hay nombre del projecto'):
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
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()


class CatchErrors:
    
    def __init__(self, name_project = 'No hay nombre del projecto', email_settings = None):
        self.name_project = name_project
        self.email_settings = email_settings
        if not self.email_settings:
            self.email_available = False
        else:
            self.email_available = True

    def show_error(self, e: Exception, send_email: bool = False)->str:
        import os
        import datetime
        info_exc = os.sys.exc_info()
        exc_type, exc_obj, exc_tb = info_exc
        file = exc_tb.tb_frame.f_code.co_filename
        function_data = str(exc_tb.tb_frame).split()
        function_data = function_data[-1][:-1]
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        
        error = f'ERROR INFO\nTipo: {exc_type}\nArchivo: {file}\nFuncion: {function_data}\nLinea: {exc_tb.tb_lineno}\nError: {e}\nFecha: {now}'
        
        if send_email:
            if not self.email_available:
                raise Exception('No hay configuración de email')
            email = ErrorEmail(error, self.email_settings, self.name_project)
            email.send()
        
        return error

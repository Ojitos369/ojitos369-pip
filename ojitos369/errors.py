import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


EMAIL_SETTINGS = {
    'smtp_server': os.environ.get('SMTP_SERVER'),
    'port': int(os.environ.get('SMTP_PORT')),
    'sender': os.environ.get('SMTP_SENDER'),
    'receiver': os.environ.get('SMTP_RECEIVER'),
    'password': os.environ.get('SMTP_PASSWORD')
}


class ErrorEmail:
    def __init__(self, message, name_project = 'No hay nombre del projecto', email_settings = None):
        if not email_settings:
            email_settings = EMAIL_SETTINGS
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP_SSL(email_settings['smtp_server'], email_settings['port'])
        self.server.login(email_settings['sender'], email_settings['password'])
        self.message = message
        self.sender = EMAIL_SETTINGS['sender']
        self.subject = f'ERROR EN {name_project}'
        self.receiver = EMAIL_SETTINGS['receiver']

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
            email = ErrorEmail(error, self.name_project, self.email_settings)
            email.send()
        
        return error

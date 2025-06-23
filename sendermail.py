import smtplib, ssl
from os.path import basename
from os.path import isfile
from os.path import dirname
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE
from email.mime.text import MIMEText

#Configuração das credenciais do servidor de email
EMAIL_SERVER = 'mail.evil.com'
FROM_EMAIL = 'cto@evil.com'
PASSWORD = 'kkk n posso te dar a senha'
DESTINATION_EMAILS = ["your-employee@gmail.com"]
WORK_DIRECTORY = '/opt/bot'

class SenderEmailFile:
    def __init__(self):
        self.WORK_DIRECTORY = WORK_DIRECTORY
        self.bk_file_name = f'{WORK_DIRECTORY}/backup_file_to_send.txt'
        self.mode_open_file = 'w'
        self.client_name = 'IONA'
        self.log_message = None
        self.log_file_name = f'{WORK_DIRECTORY}/event_messages.log'
        self.string_data_time = None
    
    def checkConfig(self):
        if not isfile(self.bk_file_name):
            with open(self.bk_file_name, 'w'):
                pass
            return False
        else:
            return isfile(self.bk_file_name)
    
    def writeLogMessage(self, message):
        with open(self.log_file_name, 'a') as log_file:
            log_file.writelines(message+'\n')

    def addBackupFile(self, bk_file_name):
        if self.checkConfig():
            with open(self.bk_file_name, self.mode_open_file) as file:
                file.writelines(bk_file_name+'\n')
            return True
        else:
            self.checkConfig()
            return False
        
    def getBackupFile(self):
        if self.checkConfig():
            with open(self.bk_file_name) as bk_file:
                bk_cleaned_list = []
                for unique_file in bk_file.readlines():
                    bk_cleaned_list.append(unique_file.strip())
                if len(bk_cleaned_list) == 1:
                    return f'{dirname(self.bk_file_name)}/{bk_cleaned_list[0]}'
                return bk_cleaned_list
        return []
                        
    def sendEmail(self):
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = COMMASPACE.join(DESTINATION_EMAILS)
        msg['Date'] = self.string_data_time
        msg['Subject'] = f'Backup Automático do Banco de Dados do cliente {self.client_name} | {msg["Date"]}'
        body_message = "Não Responda!\n\nSaudações!\nSou o Bot da SOCOMPSER LDA, este é o backup do banco de dados.\n\nAnexo o arquivo do Banco de Dados.\nAntenciosamente,\n\nBot | Socompser Lda."

        context=ssl.create_default_context()
        bk_file_to_send = self.getBackupFile()
        
        try:
            with smtplib.SMTP(EMAIL_SERVER, port=587) as smtp:
                msg.attach(MIMEText(body_message))
                try:
                    if not isinstance(bk_file_to_send, list):
                        with open(bk_file_to_send, 'rb') as b_file:
                            part = MIMEApplication(b_file.read(), Name=basename(bk_file_to_send))
                            msg.attach(part)
                    else:
                        for file in bk_file_to_send:
                            file = f'{dirname(self.bk_file_name)}/{file}'
                            with open(file, 'rb') as b_file:
                                part = MIMEApplication(b_file.read(), Name=basename(file))
                                msg.attach(part)     
                    smtp.starttls(context=context)
                    smtp.login(msg['From'], PASSWORD) # login: email, password
                   
                    smtp.send_message(msg)
                    self.mode_open_file = 'w'
                    self.log_message = 'Arquivo enviado com sucesso!'
                    return True
                except FileNotFoundError:
                    self.mode_open_file = 'w'
                    self.log_message = 'Arquivo de lista de backups inexistente!'
                    return False
        except Exception as error:
            self.mode_open_file = 'a'
            self.log_message = f'Falha na internet: {error}!'
            return False
        
        

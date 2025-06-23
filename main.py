#!/usr/bin/env python3

from time import ctime
from time import sleep
from time import strptime
from subprocess import getoutput
from sendermail import SenderEmailFile
from os.path import isdir
from os import mkdir
DATABASE_NAME = 'test'

def getDateTime():
    datetime = strptime(ctime())
    return {
        "string_date": "-".join([str(datetime.tm_mday), str(datetime.tm_mon), str(datetime.tm_year)]),
        "string_time": ':'.join([str(datetime.tm_hour), str(datetime.tm_min)]),
        "day": datetime.tm_mday,
        "month": datetime.tm_mon,
        "year": datetime.tm_year,
        "hours": datetime.tm_hour,
        "minutes": datetime.tm_min,
        "seconds": datetime.tm_sec
    }

def main():
    date_dict = getDateTime()
    handler_send_mail = SenderEmailFile()
    handler_send_mail.writeLogMessage(f"\n[{date_dict['string_time']} {date_dict['string_date']}] Iniciando o programa ...")
    while True:
        date_dict = getDateTime()
        date_time_event = f"[{date_dict['string_time']} {date_dict['string_date']}]"
        
        if date_dict['hours'] == 10 or date_dict['hours'] == 14 or date_dict['hours'] == 20 or True:
            bk_file_name = ''.join([str(date_dict["day"]), str(date_dict["month"]), str(date_dict['year'])])+'_'.join(['_'+str(date_dict["hours"]),str(date_dict['seconds']),'iona'])+'.backup'
            handler_send_mail.writeLogMessage(f'{date_time_event} [ARQUIVO: {bk_file_name}] Iniciando o backup do banco de dados...')
            is_error_backup = getoutput(f'pg_dump --dbname=postgresql://postgres:s%40c0m9s3rsistemas@localhost:5432/{DATABASE_NAME} -F c --file {handler_send_mail.WORK_DIRECTORY}/{bk_file_name}')
            
            if len(is_error_backup) != 0:
                handler_send_mail.writeLogMessage(f"{date_time_event} [ERRO] {is_error_backup}") 
            else:
                handler_send_mail.writeLogMessage(f'{date_time_event} [SUCESSO] [ARQUIVO: {bk_file_name}] Backup do banco feito com sucesso!')
                handler_send_mail.writeLogMessage(f'{date_time_event} Preparando o backup para o envio ...')
                if handler_send_mail.addBackupFile(bk_file_name):
                    handler_send_mail.string_data_time = f"{date_dict['string_date']} {date_dict['string_time']}"
                    if handler_send_mail.sendEmail():
                        handler_send_mail.writeLogMessage(f'{date_time_event} [SUCESSO] {handler_send_mail.log_message}')
                        if not isdir(f'{handler_send_mail.WORK_DIRECTORY}/enviados'):
                            mkdir(f'{handler_send_mail.WORK_DIRECTORY}/enviados')
                            getoutput(f'mv {handler_send_mail.WORK_DIRECTORY}/{bk_file_name} {handler_send_mail.WORK_DIRECTORY}/enviados/')
                        else:
                            if isinstance(bk_file_name, list):
                                print(bk_file_name)
                                for bk_file in bk_file_name:
                                    bk_file = f'{handler_send_mail.WORK_DIRECTORY}/{bk_file}'
                                    getoutput(f'mv {bk_file} {handler_send_mail.WORK_DIRECTORY}/enviados/')
                            else:
                                getoutput(f'mv {handler_send_mail.WORK_DIRECTORY}/{bk_file_name} {handler_send_mail.WORK_DIRECTORY}/enviados/')

                    else:
                        handler_send_mail.writeLogMessage(f'{date_time_event} [ERRO] {handler_send_mail.log_message}')
                else:
                    handler_send_mail.log_message = '[AVIZO] Sem arquivo de configuração, configurando ...'
                    handler_send_mail.writeLogMessage(f'{date_time_event} {handler_send_mail.log_message}')
            sleep(5)
    
if __name__ == '__main__':
    main()

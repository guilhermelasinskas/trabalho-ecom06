import Util.constants as constants
from datetime import datetime

def parse(string_main, stopc):
    token = []
    for c in string_main:
        if (c in stopc):
            break
        else:
            token.append(c)
            string_main = string_main[1:]
    
    return token, string_main

def get_time_as_string():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def write_to_file(log_message):
    f = open(constants.LOG_FILE_NAME, 'a')
    timestamp = "\n[" + get_time_as_string() + "]: "
    f.write(timestamp + log_message)

def compilation_finished_message():
    message = "A compilacao terminou com sucesso"
    write_to_file(message)

def command_validation_error_message(command):
    message = "O comando \'" + command + "\' e invalido"
    write_to_file(message)
    return message

def token_validation_error_message(token):
    message = "O token \'" + token + "\' e invalido para este comando"
    write_to_file(message)
    return message

def keyword_recognized(keyword):
    message = "A palavra \'" + keyword + "\' foi reconhecida como palavra-chave"
    write_to_file(message)

def token_recognized(token):
    message = "O token \'" + token + "\' foi reconhecido como um tipo valido"
    write_to_file(message)

def create_action_error(exception_message):
    message = "Erro de execucao: Verifique se o caminho especificado e valido.\n"
    message += "(Voce lembrou de deletar os arquivos criados na execucao anterior?)\n"
    write_to_file(message + exception_message)

def store_action_error(exception_message):
    message = "Erro de execucao: Verifique se a pasta e arquivo especificados ja existem.\n"
    message += "(Voce lembrou de deletar os arquivos criados na execucao anterior?)\n"
    write_to_file(message + exception_message)

def create_action_stepin(folder_or_path):
    message = "Tentando CRIAR \'" + folder_or_path + "\'"
    write_to_file(message)

def store_action_stepin(file, folder):
    message = "Tentando GUARDAR \'" + file + "\' em \'" + folder + "\'"
    write_to_file(message)

def action_stepout():
    message = "Acao concluida com sucesso"
    write_to_file(message)

def parse_error(exception_message):
    message = "Erro de parsing: Verifique o programa esta formatado corretamente.\n"
    write_to_file(message + exception_message)

def end_compilation():
    message = "(Erro fatal de compilacao)"
    write_to_file(message)
    quit()

def end_execution():
    message = "(Erro fatal de execucao)"
    write_to_file(message)
    quit()
import constants

def parse(string_main, stopc):
    token = []
    for c in string_main:
        if (c in stopc):
            break
        else:
            token.append(c)
            string_main = string_main[1:]
    
    return token, string_main

def write_to_file(log_message):
    f = open(constants.LOG_FILE_NAME, 'w')
    f.write(log_message)

def invalid_command_error_message(command):
    message = "O comando \'" + command + "\' é inválido"
    write_to_file(message)
    return message

def token_validation_error_message(token):
    message = "O token \'" + token + "\' é inválido para este comando"
    write_to_file(message)
    return message

def action_code_error():
    quit()

def parse(string_main, stopc):

    token = []

    for c in string_main:
        if (c in stopc):
            break
        else:
            token.append(c)
            string_main = string_main[1:]
    
    return token, string_main

def invalid_command_error_message(command):
    return ("O comando \'" + command + "\' é inválido")

def token_validation_error_message(token):
    return ("O token \'" + token + "\' é inválido para este comando")

def action_code_error():
    quit()
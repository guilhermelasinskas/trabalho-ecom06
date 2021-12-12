import Util.constants as constants
import Util.util

def validate_command(command):

    if (command == constants.keyword_CRIAR):
        Util.util.keyword_recognized(command)
        return 0
    if (command == constants.keyword_GUARDAR):
        Util.util.keyword_recognized(command)
        return 1

    return -1


def validate_folder(token):

    separated_token = token.split('/')

    for tk in separated_token:
        if(not validate_file(tk)):
            return False

    if (token[-1] != '/'):
        return False

    Util.util.token_recognized(token)
    return True


def validate_path(token):

    reverse_token = token[::-1]
    if (reverse_token[0] == '/'):
        return False

    separated_token = reverse_token.split('/')
    first_name = separated_token[0]
    first_name = first_name[::-1]

    if (not validate_file(first_name, True)):
        return False

    for tk in separated_token[1:]:
        if(not validate_file(tk)):
            return False
    
    Util.util.token_recognized(token)
    return True


def validate_file(token, isFile=False):

    for c in token:
        ok = False
        if 'a' <= c and c <= 'z':
            ok = True
        elif 'A' <= c and c <= 'Z':
            ok = True
        elif '0' <= c and c <= '9':
            ok = True
        elif c == '_':
            ok = True
        elif c == '.' and isFile:
            ok = True
        if (not ok):
            return ok

    if isFile:
        Util.util.token_recognized(token)
    
    return True

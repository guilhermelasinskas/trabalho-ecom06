import constants

def validate_command(command):

    if (command == constants.keyword_CRIAR):
        return 0
    if (command == constants.keyword_GUARDAR):
        return 1

    return -1


def validate_folder(token):

    separated_token = token.split('/')

    for tk in separated_token:
        if(not validate_file(tk)):
            return False

    if (token[-1] != '/'):
        return False

    return True


def validate_path(token):

    reverse_token = token[::-1]
    if (reverse_token[0] == '/'):
        return False

    separated_token = reverse_token.split('/')
    if (not validate_file(separated_token[0], True)):
        return False

    for tk in separated_token[1:]:
        if(not validate_file(tk)):
            return False

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
        # MEXER NISSO AQUI#
        elif c == '.' and isFile:
            ok = True
        # MEXER NISSO AQUI#
        if (not ok):
            return ok

    return True

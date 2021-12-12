import os
import shutil
from pathlib import Path
import constants

def validate_command(command):

    if (command == "CRIAR"):
        return 0
    elif (command == "GUARDAR"):
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

def validate_file(token, isFile = False):

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


def create(token1, token2):

    try:
        assert not token2
        file_name = ''
        path = ''

        if(validate_path(token1)): # Caminho
            pos = token1.rfind('/')
            if(pos == -1): # Caminho é um único arquivo
                file_name = token1
            else: # Caminho não é um único arquivo
                path = token1[0:pos]
                file_name = token1[pos+1:]
        else: # Pasta
            pos = token1.rfind('/')
            path = token1[0:pos]
        
        directory = constants.DIRECTORY
        path = directory + "/" + path

        # Cria o caminho e o arquivo no sistema operacional
        os.makedirs(path, exist_ok=True)
        
        if(file_name):
            f = open(path + "/" + file_name, 'x')

        return True
    except:
        return False

def store(token1, token2):

    try:
        path = constants.DIRECTORY
        shutil.move(path + '/' + token1, path + '/' + token2)
        return True
    except Exception as e:
        return False
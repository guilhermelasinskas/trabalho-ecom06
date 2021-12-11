import os
import shutil
from pathlib import Path

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
    for tk in separated_token:
        if(not validate_file(tk)):
            return False

    return True

def validate_file(token):

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
        if (not ok):
            return ok
    
    return True


def create(token1, token2):

    try:
        assert not token2
        if(validate_path(token1)):
        #Caminho
            pos = token1.rfind('/')
            path = token1[0:pos]
            file_name = token1[pos+1:]
        
        directory = 'E:/Users/guilh/Programacao/Python/trabalho-ecom06'
        path = directory + "/" + path

        #Cria o caminho e o arquivo no sistema operacional
        os.makedirs(path, exist_ok=True)
        f = open(path + "/" + file_name, 'x')

        return True
    except:
        return False

def store(token1, token2):
    shutil.move(original,target)
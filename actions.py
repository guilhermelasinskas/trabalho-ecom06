import os
import Util.constants as constants
import shutil
from Analyzers.entity_validator import validate_path

def create(token1): # CRIAR

    try:
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
    except Exception as e:
        return False

def store(token1, token2): # GUARDAR

    try:
        path = constants.DIRECTORY
        shutil.move(path + '/' + token1, path + '/' + token2)
        return True
    except Exception as e:
        return False
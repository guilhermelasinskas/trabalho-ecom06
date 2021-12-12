import os
import Util.constants as constants
import shutil
import Util.util
from Analyzers.entity_validator import validate_path

def create(token1): # CRIAR

    Util.util.create_action_stepin(token1)

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
        
        os.makedirs(path, exist_ok=True)
        
        if(file_name):
            f = open(path + "/" + file_name, 'x')
        
        Util.util.action_stepout()

    except Exception as e:
        Util.util.create_action_error(str(e))
        Util.util.end_execution()

def store(token1, token2): # GUARDAR

    Util.util.store_action_stepin(token1, token2)

    try:
        path = constants.DIRECTORY
        shutil.move(path + '/' + token1, path + '/' + token2)
        Util.util.action_stepout()
        
    except Exception as e:
        Util.util.store_action_error(str(e))
        Util.util.end_execution()
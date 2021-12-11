import os

def validate_command(command):

    if (command == "CRIAR"):
        return 0
    elif (command == "GUARDAR"):
        return 1
    else:
        return -1

def validate_folder(token):

    return True


def validate_path(token):

    return True

def validate_file(token):

    return True


def create(token1, token2):

    assert not token2
    if(validate_path(token1)):
       #Caminho
        pos = token1.rfind('/')
        path = token1[0:pos]
        file_name = token1[pos+1:]
    
    directory = 'E:/Users/guilh/Programacao/Python/trabalho-ecom06'
    path = directory + "/" + path

    #Cria o caminho e o arquivo no sistema operacionaç
    os.mkdir(path)
    f = open(path + "/" + file_name, 'x')

def store(token1, token2):
    print("AAAAAAA")
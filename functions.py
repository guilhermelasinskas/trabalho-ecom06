import middle_layer

def filter_input(text):

    text = text.rstrip().lstrip()
    return text

def lexical_analyzer(string_main, stopc):

    token = []

    for c in string_main:
        if (c in stopc):
            break
        else:
            token.append(c)
            string_main = string_main[1:]
    
    return token, string_main

def entity_lexical_analyser(command, token1, token2):

    if(middle_layer.validate_command(command) == 0): # CRIAR
        # TODO: log de comando reconhecido
        assert (middle_layer.validate_folder(token1) or middle_layer.validate_path(token1))

        if middle_layer.create(token1, token2):
            print("O caminho ou pasta foi criado")
        else:
            print("O caminho ou pasta não foi criado")

    elif(middle_layer.validate_command(command) == 1): # GUARDAR
        # TODO: log de comando reconhecido
        assert (middle_layer.validate_file(token1, True) and middle_layer.validate_folder(token2))
        
        if middle_layer.store(token1, token2):
            print("O arquivo foi guardado")
        else:
            print("Não foi possível guardar o arquivo")

    else:
        print("Erro de compilação: Comando não reconhecido")
        quit()
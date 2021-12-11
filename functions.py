import middle_layer

def filter_input(text):

    text = text.rstrip().lstrip()
    return text

def lexical_analyzer(string_main, stopc):

    token = []

    for c in string_main:
        if (c != stopc):
            token.append(c)
            string_main = string_main[1:]
        else:
            break
    
    return token, string_main;

def entity_lexical_analyser(command, token1, token2):

    if(middle_layer.validate_command(command) == 0):
        assert (middle_layer.validate_folder(token1) or middle_layer.validate_path(token1))

        if middle_layer.create(token1, token2):
            print("O arquivo foi criado")
        else:
            print("O arquivo não foi criado")

    elif(middle_layer.validate_command(command) == 1):
        print("GUARDAR")
        assert (middle_layer.validate_file(token1) and middle_layer.validate_folder(token2))
        middle_layer.store(token1, token2)

    else:
        print("Erro de compilação")
        quit()
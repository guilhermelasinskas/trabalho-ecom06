import functions

file_name = 'teste.txt'

with open(file_name) as file_handle:
    for line in file_handle:
        #ANALISADOR LÉXICO --------------------------------------------------------
        
        #Comando
        line = line.lstrip()
        command, line = functions.lexical_analyzer(line, ' ')
        command = ''.join(str(i) for i in command)

        #Token 1
        line = line.lstrip()
        token1, line = functions.lexical_analyzer(line, ' ')
        token1 = ''.join(str(i) for i in token1)

        #Token 2
        line = line.lstrip()
        token2, line = functions.lexical_analyzer(line, '\n')
        token2 = ''.join(str(i) for i in token2)

        #Teste
        print("Command: ", command, "Token 1: ", token1, "Token 2: ", token2)
    
        #ANALISADOR LÉXICO DE ENTIDADES -----------------------------------------

        functions.entity_lexical_analyser(command, token1, token2)
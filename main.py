from Util.constants import TARGET_FILE_NAME
from Util.constants import LOG_FILE_NAME
from Util.constants import obj_key_inst as inst
from Util.constants import obj_key_arg_A as arg1
from Util.constants import obj_key_arg_B as arg2
from Util.util import compilation_finished_message
import Analyzers.lexical_analyzer as lexical_analyzer
import Analyzers.syntactic_analyzer as syntactic_analyzer
import os
from actions import create, store

os.remove(LOG_FILE_NAME)
file_name = TARGET_FILE_NAME

# FILA DE AÇÕES
all_actions = []

# COMPILACAO
with open(file_name) as file_handle:

    for line in file_handle:
        
        # ANALISADOR LÉXICO
        command, token1, token2 = lexical_analyzer.Analyze(line)
        
        # ANALISADOR SINTÁTICO
        action_code = syntactic_analyzer.Analyze(command, token1, token2)

        if (action_code == 0): # CRIAR
            all_actions.append(
                {
                    inst: action_code,
                    arg1: token1,
                    arg2: ''
                }
            )
        
        if (action_code == 1): # GUARDAR
            all_actions.append(
                {
                    inst: action_code,
                    arg1: token1,
                    arg2: token2
                }
            )

compilation_finished_message()

# EXECUÇÃO DO PROGRAMA
for action_object in all_actions:
    command = action_object[inst]
    token1 = action_object[arg1]
    token2 = action_object[arg2]
    if command == 0:
        create(token1)
    else:
        store(token1, token2)

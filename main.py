from constants import TARGET_FILE
from constants import obj_key_inst as inst
from constants import obj_key_arg_A as arg1
from constants import obj_key_arg_B as arg2
import lexical_analyzer
import syntactic_analyzer
from actions import create, store

file_name = TARGET_FILE

with open(file_name) as file_handle:

    # Fila de ações
    all_actions = []

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
    
    for action_object in all_actions:
        command = action_object[inst]
        token1 = action_object[arg1]
        token2 = action_object[arg2]
        if command == 0:
            create(token1)
        else:
            store(token1, token2)

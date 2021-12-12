from constants import TARGET_FILE
import lexical_analyzer
import syntactic_analyzer
import util
from actions import create, store

file_name = TARGET_FILE

with open(file_name) as file_handle:
    for line in file_handle:
        
        # ANALISADOR LÉXICO
        command, token1, token2 = lexical_analyzer.Analyze(line)
        
        # ANALISADOR SINTÁTICO

        action_code = syntactic_analyzer.Analyze(command, token1, token2)

        if (action_code == 0):
            create(token1)
        if (action_code == 1):
            store(token1, token2)
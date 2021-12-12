from Analyzers.entity_validator import validate_command
from Analyzers.entity_validator import validate_file
from Analyzers.entity_validator import validate_folder
from Analyzers.entity_validator import validate_path
from Util.util import command_validation_error_message as command_error, end_compilation
from Util.util import token_validation_error_message as token_error
from Util.util import end_execution

def Analyze(command, token1, token2):
    
    try:
        assert validate_command(command) != -1, command_error(command)

        if(validate_command(command) == 0): # CRIAR
            assert validate_folder(token1) or validate_path(token1), token_error(token1)
            assert not token2
            return 0

        if(validate_command(command) == 1): # GUARDAR
            assert validate_file(token1, True), token_error(token1)
            assert validate_folder(token2), token_error(token2)
            return 1
    
    except Exception as e:
        end_compilation()
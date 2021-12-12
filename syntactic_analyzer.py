from entity_validator import validate_command
from entity_validator import validate_file
from entity_validator import validate_folder
from entity_validator import validate_path
from util import invalid_command_error_message as command_error
from util import token_validation_error_message as token_error

def Analyze(command, token1, token2):

    assert validate_command(command) != -1, command_error(command)

    if(validate_command(command) == 0): # CRIAR
        # TODO: logar comando reconhecido
        assert validate_folder(token1) or validate_path(token1), token_error(token1)
        assert not token2
        return 0

    if(validate_command(command) == 1): # GUARDAR
        # TODO: logar de comando reconhecido
        assert validate_file(token1, True), token_error(token1)
        assert validate_folder(token2), token_error(token2)
        return 1
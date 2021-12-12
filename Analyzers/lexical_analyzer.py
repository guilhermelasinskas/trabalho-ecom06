import Util.util as util

def Analyze(line):

    try:
        # Comando
        line = line.lstrip()
        command, line = util.parse(line, [' '])
        command = ''.join(str(i) for i in command)

        # Token 1
        line = line.lstrip()
        token1, line = util.parse(line, [' ', '\n'])
        token1 = ''.join(str(i) for i in token1)

        # Token 2
        line = line.lstrip()
        token2, line = util.parse(line, ['\n'])
        token2 = ''.join(str(i) for i in token2)
        token2 = token2.rstrip()

        return command, token1, token2
    
    except Exception as e:
        util.parse_error(str(e))
        util.end_compilation()

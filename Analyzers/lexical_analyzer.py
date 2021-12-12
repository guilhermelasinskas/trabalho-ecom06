from Util.util import parse

def Analyze(line):
    # Comando
    line = line.lstrip()
    command, line = parse(line, [' '])
    command = ''.join(str(i) for i in command)

    # Token 1
    line = line.lstrip()
    token1, line = parse(line, [' ', '\n'])
    token1 = ''.join(str(i) for i in token1)

    # Token 2
    line = line.lstrip()
    token2, line = parse(line, ['\n'])
    token2 = ''.join(str(i) for i in token2)
    token2 = token2.rstrip()

    return command, token1, token2

import codecs
import cStringIO
import encodings
from encodings import utf_8
from tokenize import *

def translate(readline):
    result = [(NAME, 'import'),
              (NAME, 'unittest'),
              (NEWLINE, '\n')]
    last_token = None
    for tokenum, value, _, _, _ in generate_tokens(readline):
        if tokenum == NAME and value == 'describe':
            result.append([tokenum, 'class'])
        elif tokenum == NAME and value == 'it':
            result.append([tokenum, 'def'])
        elif tokenum == NAME and value == 'before_each':
            result.extend([(tokenum, 'setUp'),
                           (OP, '('),
                           (NAME, 'self'),
                           (OP, ')')])
        elif tokenum == NAME and value == 'after_each':
            result.extend([(tokenum, 'tearDown'),
                           (OP, '('),
                           (NAME, 'self'),
                           (OP, ')')])
        elif tokenum == STRING and last_token == 'it':
            result.extend(([tokenum, value.replace(' ', '_')[1:-1],],
                           [OP, '('],
                           [NAME, 'self'],
                           [OP, ')'],))
        elif tokenum == NAME and last_token == 'describe':
            result.extend(([NAME, value+'Spec'],
                           [OP, '('],
                           [NAME, 'unittest'],
                           [OP, '.'],
                           [NAME, 'TestCase'],
                           [OP, ')'],))
        else:
            result.append([tokenum, value])
        last_token = value
    return result


class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = untokenize(translate(self.stream.readline))
        self.stream = cStringIO.StringIO(data)

def search_function(s):
    if s!='spec': return None
    utf8=encodings.search_function('utf8') # Assume utf8 encoding
    return codecs.CodecInfo(
        name='spec',
        encode=utf8.encode,
        decode=utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=StreamReader,
        streamwriter=utf8.streamwriter)

codecs.register(search_function)

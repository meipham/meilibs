import re
import FileUtils
from tf.keras.preprocessing.sequence import pad_sequences

def clean(text, corpus, split=False):
    """
    Lowercase the text 
    Split text by '\n'
    Only keep chars which is in corpus, remove other things
    Remove leading & trailing spaces of the text  
    """
    text = text.lower()
    lines = ''.join([c for c in text if c in corpus])
    lines = lines.replace('  ', ' ')

    if split:
        lines = lines.split('\n')
        lines = [l.strip() for l in lines if l.strip() != ""]
    
    return lines

def addOpenEndToken(lines):
    """
    Return the input list with a { at the begining of each string item
    and the } at the end
    """
    return ["{"+line+"}" for line in lines]

def createSequences(strings, length, remove_tail = True):
    string = ''.join(strings)
    seq = list(string[0+i:length+i] for i in range(0, len(string)))
    if remove_tail: 
        seq = [s for s in seq if len(s) == length]
    return seq

def revertAll(lines):
    return list(line[::-1] for line in lines)

def getCorpus(path):
    """
    Return a set of valid characters as a corpus
    """
    cp = FileUtils.read(path)
    return set(cp)

def encode(seq):
    to_num = [[mapper[char] for char in seq]]
    padding = pad_sequences(to_num, maxlen=SEQ_LENGTH, padding='pre', truncating='pre', value=-1)
    return padding

def decode_char(num): 
    return [k for (k,v) in mapper.items() if v==num][0]

def decode(seq):
    l = [decode_char(num) for num in seq]
    return l
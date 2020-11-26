import re
import bz2
import pickle
import _pickle as cPickle

def read(path):
    """
    Return the text read from the filepath 'path'
    """
    try:
        file = open(path, 'r', encoding='utf-8')
        text = file.read()
        file.close()
        return text
    except Exception as e: 
        print(e)
        # print("Something went wrong when reading the file")

def readlines(path, strip = True):
    """
    Return the text read from the filepath 'path'
    """
    try:
        file = open(path, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        if strip: lines = [l.strip('\n') for l in lines]
        return lines
    except Exception as e: 
        print(e)
        # print("Something went wrong when reading the file")

# Test 
# read('name_data.txt')

def getCorpus(path):
    """
    Return a set of valid characters as a corpus
    """
    cp = read(path)
    return set(cp)

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

#Test: clean
# clean('  sdf TYUAnfl !\n uweyr\n *&(, abcd')
# > ['sdf tyuanfl', 'uweyr', 'abcd']


def write(namepath, lines):
    """
    Write 'text' to file at 'namepath'
    """
    try:
        f = open(namepath, 'w', encoding='utf-8')
        for line in lines:
            f.write("%s\n" % line)
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()

        
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


# Saves the "data" with the "title" and adds the .pickle
def dump_pkl(title, data):
    pikd = open(title + '.pickle', 'wb')
    pickle.dump(data, pikd)
    pikd.close()
    
# loads and returns a pickled objects
def load_pkl(file):
    pikd = open(file, 'rb')
    data = pickle.load(pikd)
    pikd.close()
    return data
    
# Pickle a file and then compress it into a file with extension 
def dump_pickle_compress(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f: 
        cPickle.dump(data, f)
    
# Load any compressed pickle file
def load_compressed_pkl(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data

def encode(seq):
    to_num = [[mapper[char] for char in seq]]
    padding = pad_sequences(to_num, maxlen=SEQ_LENGTH, padding='pre', truncating='pre', value=-1)
    return padding

def decode_char(num): 
    return [k for (k,v) in mapper.items() if v==num][0]

def decode(seq):
    l = [decode_char(num) for num in seq]
    return l
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


def dump_pkl(title, data):
    """ 
    Saves the "data" with the "title" and adds the .pickle 
    """
    pikd = open(title + '.pickle', 'wb')
    pickle.dump(data, pikd)
    pikd.close()
    

def load_pkl(file):
    """
    Loads and returns a pickled objects
    """
    pikd = open(file, 'rb')
    data = pickle.load(pikd)
    pikd.close()
    return data
    
 
def dump_pickle_compress(title, data):
    """
    Pickle a file and then compress it into a file with extension
    """
    with bz2.BZ2File(title + '.pbz2', 'w') as f: 
        cPickle.dump(data, f)
    

def load_compressed_pkl(file):
    """
    Load any compressed pickle file
    """
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data

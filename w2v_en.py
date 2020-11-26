import os

# for word encoding 
import codecs

#for concurrency
import multiprocessing

#for reading files
import utils as ut

#regular expression
import re

#word 2 vec
import gensim.models.word2vec as w2v

# For argument parsing
import argparse


def main(args): 
    print("-"*20, "START", "-"*20)
    DATA_PATH, MODEL_PATH = args.i, args.o 
    # Variables
    num_feature = args.nfeature if args.nfeature else 256
    min_word_count = args.mincount if args.mincount else 2
    window_size = args.window if args.window else 2
    num_epochs = args.nepoch if args.nepoch else 50
    window_size = args.ngram if args.ngram else 2
    num_worker = multiprocessing.cpu_count()

    print("Reading data file...")
    # Read corpus
    sentences = ut.readlines(DATA_PATH)
    
    print("Tokenizing...")
    sentences_tokenized = [s.lower().split() for s in sentences]
    
    print('Building model...')
    model = w2v.Word2Vec(size = num_feature,
                     min_count = min_word_count,
                     workers = num_worker, 
                     window = window_size)
                     
    model.build_vocab(sentences_tokenized)
    print("Vocabularies count is: %d" % len(model.wv.vocab))
    
    print("Training word2vec...")
    model.train(sentences = sentences_tokenized, total_examples=model.corpus_count, epochs = num_epochs)
    print('Build model successfully')
    print('Saving model...')
    
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
    
    model.save(os.path.join(MODEL_PATH, 'word2vec.w2v'))
    
    print('Done')
    
def parse_arg():
	parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
	parser.add_argument('--i', metavar='path', required=True,
		        help='the path to input corput file')
	parser.add_argument('--o', metavar='path', required=True,
		        help='path to schema')
	parser.add_argument('--nfeature', type=int, required=False,
		        help='number of hidden features')
	parser.add_argument('--window', type=int, required=False,
				help='window size')
	parser.add_argument('--nepoch', type=int, required=False,
				help='number of epoch')
	parser.add_argument('--ngram', type=int, required=False,
				help='for n-gram model')
	parser.add_argument('--mincount', type=int, required=False,
				help='number of word count to be concerned')
				
	return parser.parse_args()

	

if __name__ == '__main__':
    args = parse_arg()
    main(args)
    
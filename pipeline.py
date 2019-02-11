from main.utiles.preprocessing import *
from main.utiles.weighting import t_frequency , tf_idf
from os import listdir , path
from nltk.tokenize import word_tokenize
import time


def load_corpus(corpus_path , remove_html=True):
	corpus_dict_ = {}
	for f_name in listdir(corpus_path):
		with open(path.join(corpus_path,f_name), 'r') as f_data:
			raw_text = f_data.read()
			if remove_html:
				raw_text = remove_html_tags(raw_text)

			corpus_dict_[f_name] = word_tokenize(raw_text)
	return corpus_dict_


def pre_processing(funlist , corpus):
	flist = ['lowercase', 'remove_special_characters','removeStops' ,'text_lemmatization' , 'case_folding' , 'text_stemming']
	_corpus = {}
	start = time.time()
	for f in funlist:
		if f in flist:
			_corpus = globals()[f](corpus)

	pre_processing_time = (time.time() - start)
	return _corpus , pre_processing_time


def weighting(corpus , inverse = False):
	if corpus:
		start = time.time()
		for i in corpus:
			corpus[i] = " ".join(corpus[i])

		term_frequency = t_frequency(corpus)
		_x , __xx , avr_tfidf  = tf_idf(corpus)

		weighting_time = (time.time() - start)
		return term_frequency , avr_tfidf , weighting_time
	else:
		raise ValueError('Empty corpus')


'''
if __name__ == '__main__':
	
	corpus_dict = load_corpus('/media/i933k/Data/code/projects/vc_nlp/corpus')

	funlist = ['lowercase', 'case_folding' , 'removeStops' , 'remove_special_characters' , 'text_lemmatization' , 'text_stemming']
	new_corpus = pre_processing(funlist , corpus_dict)
	_tf , _tfidf = weighting(new_corpus)

	print(_tf)
	print(_tfidf)
'''
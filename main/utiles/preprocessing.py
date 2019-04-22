import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

def remove_html_tags(raw_html) :
	#cleantext = BeautifulSoup(raw_html, "lxml").text
	if isinstance(raw_html, str):
			raw_text = BeautifulSoup(raw_html , "lxml").text
	else:
		raise "error remove_html_tags "

	return raw_text

def removeStops(corpus_dict , lang ='english') :
	"""
	This method removes stopwords from text
	:param text: req
	:lang:(optional) 
	:return:
	"""
	stops = set(stopwords.words(lang))
	if "The" in stops:
		print("The removeStops")
	for i in corpus_dict:
		if isinstance(corpus_dict[i], list):
			corpus_dict[i] = [w for w in corpus_dict[i] if not w.lower() in stops]
		else:
			raise "error removeStops "

	return corpus_dict

def remove_special_characters(corpus_dict):
	"""
	This method removes any special characters from text
	:param text:
	:return:
	"""
	for i in corpus_dict:
		if isinstance(corpus_dict[i], list):
			corpus_dict[i] = [re.sub('[^a-zA-z0-9\s]', '', w) for w in corpus_dict[i]]
		else:
			raise "error remove_special_characters "
	return corpus_dict


def lowercase(corpus_dict):
	"""
	This method reducing all letters to lower case
	:param text:
	:return:
	"""
	for i in corpus_dict:

		if isinstance(corpus_dict[i], list):
			corpus_dict[i] =  [w.lower() for w in corpus_dict[i]]
		else:
			raise "error lowercase "
	return corpus_dict



def case_folding(corpus_dict):
	"""
	This method reducing all letters to lower case
	:param text:
	:return:
	"""

	for i in corpus_dict:
		if isinstance(corpus_dict[i], list):
			corpus_dict[i] =  [w.casefold() for w in corpus_dict[i]]
		else:
			raise "error case_folding "
	return corpus_dict


def text_lemmatization(corpus_dict , lang='english'):
	"""
	This method conevert the text or list of str to the lemm form
	:param text:
	:return:
	"""
	for i in corpus_dict:
		if isinstance(corpus_dict[i], list):
			lemma = []
			w_lemma = WordNetLemmatizer()
			for w in corpus_dict[i]:
				lemma.append(w_lemma.lemmatize(w))	
			corpus_dict[i] = lemma
		else:
			raise "error text_lemmatization "
	return corpus_dict


def text_stemming(corpus_dict , lang='english'):
	"""
	This method conevert the text or list of str to its stemm form
	:param stemm list:
	:return:
	"""
	for i in corpus_dict:
		if isinstance(corpus_dict[i], list):
			stemm = []
			w_stemm = SnowballStemmer('english')
			for w in corpus_dict[i]:
				stemm.append(w_stemm.stem(w))
			
			corpus_dict[i] =  stemm
		else:
			raise "error text_stemming "
	return corpus_dict


'''
#todo
def remove_numbers(text, all_int=True):
	"""
	This method remove the numbers from the text
	:param text:
	:return:
	"""
	for i in corpus_dict:
		if all_int:
			return(re.sub("\d+", "", text))
		else:
			return(re.sub(r"(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b","" , text))

'''
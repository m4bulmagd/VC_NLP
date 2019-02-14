from nltk.stem.snowball import SnowballStemmer

def term_limit(tf , tfidf , max_terms=0):
	new_tf, new_tfidf = [] ,[]
	
	for e in tf[:int(max_terms)]:
		new_tf.append({"key":e[0] , "value":e[1] })
		

	for e in tfidf[:int(max_terms)]:
		new_tfidf.append({"key":e[0] , "value":e[1] })

	return new_tf , new_tfidf


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_word_class(tf , tfidf):
	w_stemm = SnowballStemmer('english')
	for term in tf:
		term["wclass"] = w_stemm.stem(term["key"])
	
	for term in tfidf:
		term["wclass"] = w_stemm.stem(term["key"])

	return tf , tfidf


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

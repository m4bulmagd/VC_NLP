from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
from operator import itemgetter
import numpy as np 
def t_frequency(corpus):
	if not bool(corpus):
		return []
	vectorizer = CountVectorizer()
	corpus_vectorizer = vectorizer.fit_transform(corpus.values())
	terms = vectorizer.get_feature_names()
	term_freq = [ sum(f) for f in zip(*corpus_vectorizer.toarray()) ]
	return sorted(zip(terms, term_freq),key=itemgetter(1) , reverse=True)

def tf_idf(corpus , keywords = None):
	if not bool(corpus):
		return []
	tfidfvectorizer = TfidfVectorizer()
	if keywords:
		corpus_tfidfvectorizer = tfidfvectorizer.fit(keywords)
	else:
		corpus_tfidfvectorizer = tfidfvectorizer.fit(corpus.values())

	doc_ids = [ i for i in corpus.keys()  ]
	corpus_tfidfvectorizer = tfidfvectorizer.transform(corpus.values())
	terms = tfidfvectorizer.get_feature_names()
	corpus_tfidf = dict(zip(doc_ids, corpus_tfidfvectorizer.toarray()))
	avr_tfidf = sorted(zip(terms , np.amax(corpus_tfidfvectorizer.toarray(), axis=0) ),key=itemgetter(1) , reverse=True)


	return [corpus_tfidf , terms , avr_tfidf]

def G_test(corpus):
	pass
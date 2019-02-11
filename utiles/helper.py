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
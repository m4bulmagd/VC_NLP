from flask import Blueprint, flash, g, redirect, render_template, request, url_for ,current_app
from werkzeug.exceptions import abort
from main.db import get_db
from main.pipeline import *
from main.utiles.helper import *
from werkzeug.utils import secure_filename
import os


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
	upload_path = str(os.getcwd()+current_app.config['UPLOAD_FOLDER'])
	if not os.path.exists(upload_path):
		print(upload_path)
		os.makedirs(upload_path)

	corpora_db = []
	for dir_name in os.listdir(upload_path):
		corpora_db.append(dir_name)
	return render_template('index.html' , corpora_db= corpora_db)


@bp.route('/corpora')
def corpora():
	corpus_url = str(os.getcwd()+current_app.config['UPLOAD_FOLDER'])
	print("corpus_url")
	corpora_db = {}
	for dir_name in os.listdir(corpus_url):
		print(os.path.join(corpus_url , dir_name))
		corpora_db[dir_name] = len(os.listdir(os.path.join(corpus_url , dir_name)))

	print(corpora_db)
	return render_template('corpora.html' , corpora_db= corpora_db )


@bp.route('/processing' , methods=['POST'])
def processing():
	

	corpus_name = request.form['new_corpus_name']
	if corpus_name !='':
		corpus_url = str(os.getcwd()+current_app.config['UPLOAD_FOLDER']+corpus_name)
	else:
		corpus_name = request.form['selected_corpus_name']
		corpus_url = str(os.getcwd()+current_app.config['UPLOAD_FOLDER']+corpus_name)

	#corpus_name
	print(corpus_url)
	if not os.path.exists(corpus_url):
		print(corpus_url)
		os.makedirs(corpus_url)
	else:
		pass
		#raise "ALready exist dir" 

	if request.method == 'POST':
		# check if the post request has the file part
		files = request.files.getlist("files_input[]")


		if files:
			for file in files:
				filename = secure_filename(file.filename)
				f = os.path.join( corpus_url,str(filename))
				file.save(f)

	fns1 = request.form['fns_input1']
	remove_html = request.form.get('remove_html_chbox')
	tf_chbox = request.form.get('tf_chbox')
	tfidf_chbox = request.form.get('tfidf_chbox')
	#fileeeeeeeeeeeeees = request.form['files_input']
	#print(fileeeeeeeeeeeeees)
	fns2 = request.form['fns_input2']
	max_terms = request.form['max_terms']
	fns1 = list(fns1.split(","))
	fns2 = list(fns2.split(","))
	print("fns2 : ",fns2)

	#fns = ['lowercase', 'remove_special_characters','removeStops' ,'text_lemmatization']
	corpus_dict = load_corpus(corpus_url , remove_html=remove_html)
	new_corpus1 ,pre_processing_time1 = pre_processing(fns1 , corpus_dict)
	_tf1 , _tfidf1 , weighting_time1 = weighting(new_corpus1)
	new_tf1 , new_tfidf1  = term_limit(_tf1 , _tfidf1 , max_terms=max_terms)
	new_tf1 , new_tfidf1  = add_word_class(new_tf1 , new_tfidf1)
	time1 =[pre_processing_time1 ,weighting_time1 , weighting_time1+pre_processing_time1]

	corpus_dict = load_corpus(corpus_url , remove_html=remove_html)
	new_corpus2 ,pre_processing_time2= pre_processing(fns2 , corpus_dict)
	_tf2 , _tfidf2 , weighting_time2 = weighting(new_corpus2)
	new_tf2 , new_tfidf2  = term_limit(_tf2 , _tfidf2 , max_terms=max_terms)
	new_tf2 , new_tfidf2  = add_word_class(new_tf2 , new_tfidf2)
	time2 =[pre_processing_time2 ,weighting_time2 , weighting_time2+pre_processing_time2]


	return render_template('vis.html' ,  tf1 = new_tf1, tfidf1=new_tfidf1  , fns1 = fns1 ,tf2 = new_tf2, tfidf2=new_tfidf2, fns2=fns2,  time1=time1 , time2=time2, single_chart = False)
	#return redirect(url_for('main.vis', _method='POST', tf=_tf , tfidf = _tfidf ))
	
@bp.route('/vis' , methods=['POST'])
def vis():
	return render_template('vis.html')

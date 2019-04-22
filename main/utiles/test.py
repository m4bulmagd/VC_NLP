from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

from preprocessing import *

from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer

from preprocessing import *
from weighting import t_frequency , tf_idf




text = {"1.txt":"The Dog Dog Dog Dog Dog <br> a good good good animaL animaL", "2.txt":"this is as dog"}

for t in text:
	text[t] = word_tokenize(text[t])

print(remove_html_tags(text))

'''
print(t_frequency(text))

keywords  = list(list(zip(*t_frequency(text)))[0])[:3]
print(keywords)
print(tf_idf(text , keywords = keywords))
'''

'''
text = word_tokenize(text)
funlist = ['lowercase', 'case_folding' , 'removeStops']

for f in funlist:
	text = locals()[f](text)

print(text)

x =frequency(text)
curpos = {"c1":dict(x)}
print(curpos)
print(x['dog'])

'''


'''

text = 'The Dog Dog Dog Dog Dog IS a good good good animaL animaL'
text = word_tokenize(text)
funlist = ['lowercase', 'case_folding' , 'removeStops']

for f in funlist:
	text = locals()[f](text)

print(text)

x =frequency(text)
curpos = {"c1":dict(x)}
print(curpos)
print(x['dog'])

'''
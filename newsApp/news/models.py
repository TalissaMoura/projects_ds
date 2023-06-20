from bson import ObjectId
from flask.json import JSONEncoder

import re,contractions,string,pickle,os
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


tf_vect = pickle.load(open(os.path.join(".","news","model","save","tf_vec.sav"),"rb"))
pca = pickle.load(open(os.path.join(".","news","model","save","pca.sav"),"rb"))

class MongoJSONEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        
        return super().default(o)

class BasicPreprocess():
    def __init__(self,text):
        self.text = text

    def to_lowercase(self):
        new_text = self.text.lower()
        return new_text
    
    def fix_contractions(self):
       for k,v in contractions.contractions_dict.items():
          self.text = self.text.replace(k,v)
       new_text = self.text
       return new_text

    def punct_repetition(self,default_replace=""):
       new_text = re.sub(r"[\.\,\?\!]+(?=[\.\,\?\!])",default_replace,self.text)
       return new_text
    
    def word_repetition(self):
        new_text = re.sub(r'(.)\1+',r'\1\1',self.text)
        return new_text 

    def custom_tokenize(self,keep_punct=False,keep_alnum=False,keep_stop=False):
        new_text = self.text
        token_list = word_tokenize(new_text)
        if not keep_punct:
            token_list = [ token for token in token_list if token not in string.punctuation]
    
        if not keep_alnum:
            token_list = [ token for token in token_list if token.isalpha()]
    
        if not keep_stop:
            stop_words = set(stopwords.words("english"))
            #remove no from stop words
            stop_words.discard("not")
            stop_words.discard("no")
            token_list = [token for token in token_list if not token in stop_words]
            
        return token_list

    
    

class NewsTitleEncoder(BasicPreprocess):
    def __init__(self,title=None):
        self.news_title =title
        super().__init__(title)


    def process_text(self):
    #clean the text
       self.news_title = super().to_lowercase()
       self.news_title = super().fix_contractions()
       self.news_title = super().punct_repetition()
       self.news_title = super().word_repetition()
    
       #tokenize the text and returns stems 
       tokens = super().custom_tokenize(self.news_title,keep_stop=True,keep_alnum=True)
       snowball_stemmer = SnowballStemmer("english")
       
       stems_tokens = []
       for token in tokens:
           stems_tokens.append(snowball_stemmer.stem(token))
       
       return stems_tokens
    
    @staticmethod
    def text_to_vec(tokens):
       tfidf_text = tf_vect.transform([tokens])
       tfidf_text = np.array(tfidf_text.todense())
       new_vec = pca.transform(tfidf_text)
       return new_vec

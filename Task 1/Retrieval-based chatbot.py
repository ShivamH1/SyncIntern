import nltk
import numpy as np
import random 
import string

import bs4 as bs
import requests 
import re

import warnings
warnings.filterwarnings = False

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

r = requests.get('https://en.wikipedia.org/wiki/Cuisine')
raw_html = r.text

corpus_html = bs.BeautifulSoup(raw_html)

corpus_paras = corpus_html.find_all('p')
corpus_text = ''

for para in corpus_paras:
    corpus_text += para.text
    
corpus_text = corpus_text.lower()

corpus_text = re.sub(r'\[[0-9]*\]',' ',corpus_text)
corpus_text = re.sub(r'\s+',' ',corpus_text)

corpus_sentences = nltk.tokenize.sent_tokenize(corpus_text)
corpus_words = nltk.tokenize.word_tokenize(corpus_text) 

greeting_inputs = ("hey","good morning","good evening","morning","evening","hi","whatsup",)
greeting_responses = ["hey","hey hows you?","*nods*","hello, how you doing","hello","Welcome I am good",]

def greet_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)
        
wn_lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_corpus(tokens):
    return [wn_lemmatizer.lemmatize(token) for token in tokens]

punct_removal_dict = dict((ord(punctuation),None) for punctuation in string.punctuation)

def get_processed_text(document):
    return lemmatize_corpus(nltk.tokenize.word_tokenize(document.lower().translate(punct_removal_dict)))


def respond(user_input):
    global corpus_sentences
    bot_response = ''
    corpus_sentences.append(user_input)
    
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    corpus_word_vectors = word_vectorizer.fit_transform(corpus_sentences)
    
    cos_sim_vectors = cosine_similarity(corpus_word_vectors[-1], corpus_word_vectors)
    similar_response_idx = cos_sim_vectors.argsort()[0][-2]
    
    matched_vector = cos_sim_vectors.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]
    
    if vector_matched == 0:
        bot_response = bot_response + "I am sorry, what is it, again?"
        return bot_response
    else:
        bot_response = bot_response + corpus_sentences[similar_response_idx]
        return bot_response
    
chat = True
print("Hello, What do you want to learn about Cuisines today?")
while (chat == True) :
    user_query=input()
    user_query = user_query.lower()
    if user_query != 'quit':
        if user_query == 'thanks' or user_query == 'thank you':
            chat = False
            print("CuisineBot: You are welcome!")
        else:
            if greet_response (user_query) != None:
                print("CuisineBot:" + greet_response (user_query))
            else:
                print("CuisineBot: ", end="")
                print (respond (user_query))
                corpus_sentences.remove(user_query)
    else:
        chat = False
        print("CuisineBot: Good bye!")


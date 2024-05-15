import streamlit as st
import pickle
import nltk 
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords

model = pickle.load(open('C:\\Users\\siddh\\OneDrive\\Desktop\\Machine_learning\\ml_learning_pr\\spam_classifier\\model.pkl' , 'rb'))
tfidf = pickle.load(open('C:\\Users\\siddh\\OneDrive\\Desktop\\Machine_learning\\ml_learning_pr\\spam_classifier\\vectorizer.pkl' , 'rb'))


st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the msg")



import string
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y  = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
           y.append(i)
    
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)


if st.button('Predict'):
    #1.preprocess   
    transformed_sms = transform_text(transform_text)
    
    #2.vectorize
    vect_input = tfidf.transform([transformed_sms])
    
    #3.predict
    result = model.predict(vect_input)[0]
    
    #4.display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
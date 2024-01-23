import pickle
from unidecode import unidecode
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd

def lemmatisation(text, nlp):
    # Analyser le texte avec le modèle SpaCy
    doc = nlp(text)
    # Créer une liste de lemmes pour chaque token dans le document
    lemmas = [unidecode(token.lemma_ ) for token in doc]
    # Joindre les lemmes pour former un nouveau texte lemmatisé
    new_text = " ".join(lemmas)
    # Retourner le nouveau texte lemmatisé
    return new_text


#  Text to vector (load the faetures names and vectorize the data)
def textToVect(text):
    # Load the features names for our model  
    with open(r'RP_to_text\Ressources\Bag_of_words\fr_featuresNames_v3.txt', "rb") as file:
        bag_words = pickle.load(file)
        transformer = TfidfTransformer()
        vectorizer = CountVectorizer()
        vectorizer.fit(bag_words)
        text = vectorizer.transform(text)
        X = transformer.fit_transform(text)
        X = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
        return X
    
    
def prepare_text(text,nlp):
    text = lemmatisation(text,nlp)

    return textToVect([text])

from googletrans import Translator
from textblob import TextBlob

def translate(text):
    try:
        translator = Translator()
        translated = translator.translate(text, src='ar', dest='en')
        return translated.text
    except Exception as e:
        print(f"Translation Error: {str(e)}")
        return " "

def predict_arabic(text):
    text = translate(text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.05:
      result = 'Positif'

    elif sentiment < -0.05:
      result = 'Negatif'
    else:
      result = 'Neutre'
    
    return result 

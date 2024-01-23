import pickle
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

#  Make prediction using the two models and combine them
def predict(vect,texte):
  Text = []
  Text.append(texte)
  with open(r'RP_to_text\Ressources\Models\fr_model_v3.pkl', 'rb') as file:
    model = pickle.load(file)
  # Load  the nlp pre-trained model
  tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

  model_predict = model.predict(vect)[0]
  tb_predict = tb(texte).sentiment[0]
  # Donner la prediction finale
  if model_predict == -1 :
    model_predict = "Négatif"
    if tb_predict > 0.2:
        fPrediction = "Positif"
    elif tb_predict == 0:
        fPrediction = "Neutre"
    else :
        fPrediction = "Negatif"
    return fPrediction

  elif model_predict == 1 :
    model_predict = "Positif"
    if tb_predict <= -0.2:
        fPrediction = "Negatif"
    elif tb_predict <= 0.1 :
        fPrediction = "Neutre"
    else : 
        fPrediction = "Positif"
    return fPrediction
    
  else :
    model_predict = "Neutre"
    if tb_predict <-0.25:
        fPrediction = "Negatif"
    elif tb_predict < 0.3:
        fPrediction = "Neutre"
    else:
        fPrediction = "Positif"
    return fPrediction
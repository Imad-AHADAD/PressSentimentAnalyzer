import spacy
import re
from langdetect import detect
from .gpt_api import predict_gpt
from .data_preparation import prepare_text
from .model_prediction import predict
from ..models import ExtractedInformation, ExtractedInformationTamwilcom , PageLabels, ArticleInformation
from .arabic_prediction import predict_arabic



def parle_tamwilcom(page):
    clean_page = re.sub(r'[^\w\s]', '', page)
    parle_sentence_fr = ['tamwilcom', 'ccg', 'sngfe', 'damane express', 'damane atassyir', 'damane istitmar', 
             'ligne française', 'mdm invest', 'renovotel', 'green invest', 'caisse centrale de garantie',
             "société nationale de garantie et de financement", "damane oxygène", "damane relance",
             "intelaka", 'enseignement plus'
             'on a parlé de la ccg'

            ]

    parle_sentence_ar = ["تمويلكم","تمويلكم", "الشركة الوطنية للضمان ولتمويل المقاولة",
    'تمَؤَيِلكِمَ', 'صندوق الضمان المركزي','صندوق الضمان', ' لصتدوق الصمان المركزي',
    'ضمان إقلاع',   'دمان إكسبريس', 'دمان التأمين على السفر', 'دمان الاستثمار', 
    'الخط الفرنسي',  'رينوفوتيل', 'الاستثمار الأخضر', 'الصندوق الوطني للضمان الاجتماعي', 
    'الشركة الوطنية للضمان والتمويل', 'دمان أكسجين', 'دمان ريلانس', 
    'برنامج إنطلاقة', 'أنسينمون بلوس'  ]
    
    for sentence in parle_sentence_ar:
        if sentence in clean_page:
            return True
        
    clean_page = clean_page.lower()
    for sentence in parle_sentence_fr:
        if sentence in clean_page:
            return True   
    
    return False


def extract_paragraphs(page):
    paragraphs = page.strip().split('.')
    return paragraphs

#  test du validation d'un paragraphe et le nettoyage
def is_valid_string(s):
    # Remove leading and trailing whitespace from the string
    s = s.strip()
    # Check if the string has at least 3 non-empty words and contains some non-space characters
    return len(s.split()) >= 3 and any(c for c in s)

def clean_paragraphs(input_list):
    return [s for s in input_list if is_valid_string(s)]



#  combiner toute les fonctions et tranferer les résultats à notre data base
def storeInTheDataBase(pages, dateRevuePresse):
   
    # Charger le modèle spaCy en français (la version moyenne)
    nlp = spacy.load("fr_core_news_md")

    # Insert the data into the database table
    for page_num, page_text in enumerate(pages):
        
        lang = detect(page_text)
        
        if not parle_tamwilcom(page_text):
           ExtractedInformation.objects.create(
               date_revue_presse = dateRevuePresse,
               num_page = page_num+1,
               langue = lang,
               page = page_text
           )
           continue
        
        #  l'article parle de tamwilcom
            
        if lang == 'ar':
           label = predict_arabic(page_text)
           
           if label == 'negative':
               label = "Négatif"
           elif label == 'positive':
               label = 'Positif'
           else:
               label = "Neutre"
        
           ExtractedInformationTamwilcom.objects.create(
               date_revue_presse=dateRevuePresse,
                num_page=page_num+1,
                langue='ar',
                num_paragraph=1,
                paragraph=page_text,
                label=label
            )
           PageLabels.objects.create(
                date_revue_presse = dateRevuePresse,
                num_page = page_num + 1,
                label = label      
            ) 
           continue


        paragraphs = extract_paragraphs(page_text)
        paragraphs = clean_paragraphs(paragraphs)
        
        for para_num, para in enumerate(paragraphs):
            # Sample label; replace with actual labels or get the label from user input
            para =  para.strip()   
            vect = prepare_text(para, nlp)
            label = predict(vect, para)
            ExtractedInformationTamwilcom.objects.create(
                date_revue_presse=dateRevuePresse,
                num_page=page_num+1,
                langue='fr',
                num_paragraph=para_num+1, 
                paragraph=para,
                label=label
            )
            pos = 0
            neg = 0 
            if label == 1: 
                pos += 1
            if label == -1 :
                neg += 1
        storeInPagesLabels( dateRevuePresse, page_num , pos , neg  )


# Prendre les donnees de la table 
def getDataFromTheDataBase(newDateRevuePresse):
    tamwilcom_rows = ExtractedInformationTamwilcom.objects.filter(date_revue_presse=newDateRevuePresse)
    # Convert the queryset to a list of tuples
    tamwilcom_list = [(row.id, row.date_revue_presse, row.num_page, row.langue, row.num_paragraph, row.paragraph, row.label) for row in tamwilcom_rows]

    return tamwilcom_list


def storeInPagesLabels( date_revue_presse, num_page , pos , neg  ):
    dif = pos - neg
    if  dif > 0: 
        label = 1
    elif dif == 0 :
        label =  0
    else :
        label = -1 
    
    PageLabels.objects.create(
        date_revue_presse = date_revue_presse,
        num_page = num_page + 1,
        label = label      
    )  
   
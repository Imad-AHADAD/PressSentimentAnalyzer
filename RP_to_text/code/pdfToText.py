from pytesseract import pytesseract
from pdf2image import convert_from_bytes 
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from ..models import ArticleInformation
# from .DataBase import parle_tamwilcom



def extract_text(uploaded_file, dateRevuePresse):
    images = convert_from_bytes(uploaded_file)
    # path vers tesseract OCR exe
    path_to_tesseract = r'RP_to_text\Ressources\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract

    # Parcourir les pages du PDF à partir de la page 2 jusqu'à l'avant-dernière page
    # Remarque : les numeros des pages commencent par 0 et les deux premiers pages ne contient pas d'information importante
    extracted_text = []
    for page_num, image_path in enumerate( images[2:len(images)-1] ):
        text = pytesseract.image_to_string(image_path, lang = 'eng')  # Apply OCR
        try: 
            lang = detect(text)
            if lang != 'fr':
                text = pytesseract.image_to_string(image_path, lang='ara+eng')
        except LangDetectException as e:
            continue
        extracted_text.append(text)

        # Staockage des information de l'article 
        # if parle_tamwilcom(text) :
        rows = text.strip().split('\n')
        rows = [row for row in rows if row.strip()]
        if rows[0].split()[0] == 'Support' and rows[1].split()[0] == 'Titre' :
            try : 
                a = rows[0].split('Type')
                type_journal = a[0].split(':')[1].replace("|", "").strip()
                b = a[1].split('Tags')
                type_article = b[0].replace(":", "").replace("|", "").strip()
                
                tag = b[1].replace(":", "").replace("|", "").strip()

                titre_article = rows[1].replace("Titre :", "")
                titre_article = titre_article.replace("Titre:", "").strip()

                nom_journal = rows[2].replace("Journal :", "")
                nom_journal = nom_journal.replace("Journal:", "").strip()
                # Create a list representing a row of data
                row_data = [titre_article, nom_journal, type_journal, type_article, tag]
                
                ArticleInformation.objects.create(
                    date_revue_presse = dateRevuePresse,
                    num_page = page_num + 1,
                    article_title = row_data[0],
                    journal_name = row_data[1],
                    journal_type = row_data[2],
                    article_type = row_data[3],
                    tags = row_data[4]
                )
               
            except Exception as e:
                print(e)
                continue     

    return extracted_text



def extract_text_v2(uploaded_file):
    images = convert_from_bytes(uploaded_file)
    # path vers tesseract OCR exe
    path_to_tesseract = r'RP_to_text\Ressources\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract

    extracted_text = []
    for image_path in images[0:len(images)]:
        text = pytesseract.image_to_string(image_path, lang = 'ara+eng')  # Apply OCR 
        extracted_text.append(text)

    return extracted_text


from django.shortcuts import render, redirect
from django.urls import reverse
from .code.pdfToText import extract_text ,  extract_text_v2
from .code.DataBase import storeInTheDataBase , getDataFromTheDataBase
from .code.cleaning import cleanText
from .code.data_preparation import prepare_text
from .code.model_prediction import predict
from .code.arabic_prediction import predict_arabic
from .code.imgToText import extract_text_img
import spacy


def reveu_de_presse(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        pdf_bytes = uploaded_file.read()

        # Store the Rp date in the session
        dateRevuePresse = uploaded_file.name
        dateRevuePresse = dateRevuePresse.replace(".pdf", "")
        dateRevuePresse = dateRevuePresse.replace("Revue de presse", "").strip()
        request.session['dateRevuePresse'] = dateRevuePresse

        extracted_text = extract_text(pdf_bytes, dateRevuePresse)

        # Store the extracted text in the session
        request.session['extracted_text'] = extracted_text


        # Store Artical informations in the session
        # request.session['extracted_data'] = extracted_data 
 
        return redirect(reverse('file_uploaded'))
    return render(request, 'upload_file.html')


def file_uploaded(request):
    # Retrieve the extracted text from the session
    extracted_text = request.session.get('extracted_text', "")
    return render(request, "file_uploaded.html", {'extracted_text': "".join(extracted_text)})


def apply_model(request):
    if request.method == 'POST':
        extracted_text =  request.session.get('extracted_text', "")
        dateRevuePresse =  request.session.get('dateRevuePresse', "")
        # extracted_data =  request.session.get('extracted_data', "")
        storeInTheDataBase(extracted_text, dateRevuePresse )
        data = getDataFromTheDataBase(dateRevuePresse)
        return render(request, 'result_page.html', {'data': data})
 

def clean_text(request):
    if request.method == 'POST':
        # Retrieve the extracted text from the session
        extracted_text = request.session.get('extracted_text', "")
        extracted_text = [ cleanText(page, num_page) for num_page, page in enumerate(extracted_text) ]
        return render(request, 'cleaned_text.html', {'extracted_text': "".join(extracted_text)})


def french_sentiment_analysis(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        # Charger le modèle spaCy en français (la version moyenne)
        nlp = spacy.load("fr_core_news_md")
        vect = prepare_text(text, nlp)
        result = predict(vect, text)

    return render(request, 'sentiment_analysis.html', {'result': result})


def arabic_sentiment_analysis(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        result = predict_arabic(text)

    return render(request, 'sentiment_analysis.html', {'result': result})


def menu(request):
    return render(request, 'menu.html')

    
def OCR_img(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        extracted_text = extract_text_img(uploaded_file)
        # Store the extracted text in the session
        request.session['extracted_text_img'] = extracted_text
        return redirect(reverse('img_uploaded'))
    
    return render(request, 'img_to_text.html')


def img_uploaded(request):
    # Retrieve the extracted text from the session
    extracted_text = request.session.get('extracted_text_img', "")
    # extracted_text = clean_text("".join(extracted_text))
    return render(request, "image_uploaded.html", {'extracted_text': extracted_text})


def OCR_pdf(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        pdf_bytes = uploaded_file.read()
        extracted_text = extract_text_v2(pdf_bytes)
        # Store the extracted text in the session
        request.session['extracted_text_v2'] = extracted_text
        return redirect(reverse('pdf_uploaded'))
    return render(request, 'upload_file.html')


def pdf_uploaded(request):
    # Retrieve the extracted text from the session
    extracted_text = request.session.get('extracted_text_v2', "")
    # extracted_text = clean_text("".join(extracted_text))
    return render(request, "image_uploaded.html", {'extracted_text': "".join(extracted_text)})

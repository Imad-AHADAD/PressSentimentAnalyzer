from django.urls import path
from .views import menu ,img_uploaded, pdf_uploaded, file_uploaded , apply_model , clean_text,OCR_pdf, reveu_de_presse, arabic_sentiment_analysis, french_sentiment_analysis, OCR_img

urlpatterns = [ path('', reveu_de_presse, name="reveu_de_presse"),
                path('menu/', menu, name="upload_file"),
               
                path('Reveu_de_presse/', reveu_de_presse, name='reveu_de_presse'),
                path('file_uploaded/', file_uploaded, name="file_uploaded"), 
                path('apply_model/', apply_model, name='apply_model'),
                path('clear-text/', clean_text, name='clean_text'),

                path('OCR_pdf/', OCR_pdf, name='ocr_pdf'),
                path('pdf_uploaded/', pdf_uploaded, name='pdf_uploaded'),


                path('arabic_sentiment_analysis/', arabic_sentiment_analysis, name='arabic_sentiment_analysis'),
                path('french_sentiment_analysis/', french_sentiment_analysis, name='french_sentiment_analysis'),
                
                path('OCR_img/', OCR_img, name='ocr_img'),
                path('img_uploaded/', img_uploaded, name='img_uploaded'),
              ]


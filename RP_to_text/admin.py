from django.contrib import admin
from .models import ExtractedInformationTamwilcom, ExtractedInformation, PageLabels, ArticleInformation

admin.site.register(ExtractedInformationTamwilcom)
admin.site.register(ExtractedInformation)
admin.site.register(PageLabels)
admin.site.register(ArticleInformation)



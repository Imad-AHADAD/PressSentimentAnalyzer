from django.db import models
    
class ExtractedInformationTamwilcom(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    date_revue_presse = models.CharField(max_length=255)
    num_page = models.IntegerField()
    langue = models.CharField(max_length=10)
    num_paragraph = models.IntegerField(null=True)
    paragraph = models.TextField(null=True)
    label = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.date_revue_presse} / page {self.num_page} / paragraphe {self.num_paragraph}"

    class Meta:
        db_table = 'Extracted_informations_Tamwilcom'  


class ExtractedInformation(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    date_revue_presse = models.CharField(max_length=255)
    num_page = models.IntegerField()
    langue = models.CharField(max_length=10)
    page = models.TextField(null=True) 

    def __str__(self):
        return f"{self.date_revue_presse} / page {self.num_page}"
    class Meta:
        db_table = 'Extracted_informations'  


class PageLabels(models.Model):
    id = models.AutoField(primary_key=True)
    date_revue_presse = models.CharField(max_length=255)
    num_page = models.IntegerField()
    label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date_revue_presse} / page {self.num_page}"

    class Meta:
        managed = False  # Tell Django not to manage this table
        db_table = 'pagelabels'  




class ArticleInformation(models.Model):
    id = models.AutoField(primary_key=True)
    date_revue_presse = models.CharField(max_length=255)
    num_page = models.IntegerField()
    article_title = models.CharField(max_length=255)
    journal_name = models.CharField(max_length=255)
    journal_type = models.CharField(max_length=255)
    article_type = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date_revue_presse} / {self.journal_name}"
    
    class Meta:
        managed = False
        db_table = 'article_informations'  # Specify the exact table name





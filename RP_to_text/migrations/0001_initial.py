# Generated by Django 4.2.4 on 2023-09-02 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractedInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_revue_presse', models.CharField(max_length=255)),
                ('num_page', models.IntegerField()),
                ('langue', models.CharField(max_length=10)),
                ('page', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Extracted_informations',
            },
        ),
        migrations.CreateModel(
            name='ExtractedInformationTamwilcom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_revue_presse', models.CharField(max_length=255)),
                ('num_page', models.IntegerField()),
                ('langue', models.CharField(max_length=10)),
                ('num_paragraph', models.IntegerField(null=True)),
                ('paragraph', models.TextField(null=True)),
                ('label', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Extracted_informations_Tamwilcom',
            },
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='author',
            field=models.CharField(default='Auteur inconnu', help_text='Auteur du livre', max_length=128),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, help_text='Décrivez brièvement le livre à critiquer, indiquez son auteur, son éditeur, son année de publication et éventuellement indiquez le type de critique que vous souhaitez.', max_length=2048),
        ),
    ]

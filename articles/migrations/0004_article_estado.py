# Generated by Django 2.1.2 on 2018-10-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='estado',
            field=models.CharField(blank=True, choices=[('Disponible', 'Disponible'), ('Rescatado', 'Rescatado'), ('Adoptado', 'Adoptado')], max_length=100, null=True),
        ),
    ]
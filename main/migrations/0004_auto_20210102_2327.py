# Generated by Django 3.1.4 on 2021-01-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_voting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='image',
            field=models.ImageField(null=True, upload_to='votings'),
        ),
    ]

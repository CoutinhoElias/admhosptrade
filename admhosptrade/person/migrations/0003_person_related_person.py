# Generated by Django 2.2.2 on 2019-06-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20190609_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='related_person',
            field=models.ManyToManyField(related_name='_person_related_person_+', to='person.Person'),
        ),
    ]
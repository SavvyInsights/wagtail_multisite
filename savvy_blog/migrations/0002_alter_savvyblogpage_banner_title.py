# Generated by Django 4.0.4 on 2022-06-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savvy_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savvyblogpage',
            name='banner_title',
            field=models.CharField(default='This is a savvy blog', max_length=100),
        ),
    ]

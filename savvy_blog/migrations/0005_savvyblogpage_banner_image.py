# Generated by Django 4.0.4 on 2022-06-03 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('savvy_blog', '0004_rename_snipit_savvyblogpage_snippit'),
    ]

    operations = [
        migrations.AddField(
            model_name='savvyblogpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-03 02:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('savvy_blog', '0010_alter_savvyblogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savvyblogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=None),
        ),
    ]

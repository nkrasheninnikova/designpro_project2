# Generated by Django 5.1.3 on 2024-11-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='avatars/def-avatar.jpg', upload_to='avatars/'),
        ),
    ]
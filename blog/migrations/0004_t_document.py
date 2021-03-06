# Generated by Django 2.0.6 on 2018-06-27 13:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180619_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('dateUp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date upload')),
                ('uploader', models.CharField(max_length=100, null=True)),
                ('doc', models.FileField(upload_to='PJ/')),
                ('IG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.T_IG')),
            ],
            options={
                'verbose_name': 'Pièces jointes',
                'ordering': ['dateUp'],
            },
        ),
    ]

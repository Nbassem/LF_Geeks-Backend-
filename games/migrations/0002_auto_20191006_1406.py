# Generated by Django 2.2.6 on 2019-10-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
   

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Playstation 4', 'Playstation 4 ')], max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='genre',
            name='platform',
        ),
        migrations.AddField(
            model_name='games',
            name='platform',
            field=models.ManyToManyField(to='games.Platform'),
        ),
    ]

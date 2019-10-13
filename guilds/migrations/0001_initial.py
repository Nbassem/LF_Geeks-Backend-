# Generated by Django 2.2.6 on 2019-10-07 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
   

    initial = True

    dependencies = [
        ('games', '0004_auto_20191007_1642'),
        ('accounts', '0007_auto_20191007_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('tag', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=5000)),
                ('games', models.ManyToManyField(to='games.Games')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
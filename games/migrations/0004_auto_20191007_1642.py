# Generated by Django 2.2.6 on 2019-10-07 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20191006_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='games',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Developer'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform',
            field=models.CharField(max_length=150),
        ),
    ]

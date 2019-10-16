# Generated by Django 2.2.6 on 2019-10-15 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_country'),
        ('guilds', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='tag',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applicant', 'applicant'), ('application', 'application'), ('trial', 'trial'), ('final', 'final')], max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guilds.Question')),
                ('recruitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guilds.Recruitment')),
            ],
        ),
    ]
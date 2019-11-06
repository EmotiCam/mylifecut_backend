# Generated by Django 2.2.7 on 2019-11-06 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('MALE', '남자'), ('FEMALE', '여자'), ('OTHER', 'OTHER'), ('SECRET', 'SECRET')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=10)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anger', models.FloatField()),
                ('contempt', models.FloatField()),
                ('disgust', models.FloatField()),
                ('fear', models.FloatField()),
                ('happiness', models.FloatField()),
                ('neutral', models.FloatField()),
                ('sadness', models.FloatField()),
                ('surprise', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
    ]
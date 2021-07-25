# Generated by Django 3.2.5 on 2021-07-16 13:30

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('location', models.URLField()),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('food', models.IntegerField(blank=True, choices=[(1, 'north_indian'), (2, 'south_indian'), (3, 'both')], default=2, null=True)),
                ('pgtype', models.IntegerField(blank=True, choices=[(1, 'GENTS'), (2, 'LADIES')], default=1, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.area')),
                ('city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.city')),
            ],
        ),
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharing_cap', models.IntegerField(choices=[(1, 'Single'), (2, 'Doulbe'), (3, 'Triple'), (4, 'Four')])),
                ('price', models.IntegerField()),
                ('pg', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.pg')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('pg', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.pg')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.city'),
        ),
    ]

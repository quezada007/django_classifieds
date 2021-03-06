# Generated by Django 3.0.3 on 2020-04-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('auto', 'Auto'), ('free', 'Free'), ('furniture', 'Furniture'), ('household', 'Household'), ('other', 'Other'), ('room-for-rent', 'Room For Rent'), ('sporting', 'Sporting'), ('wanted', 'Wanted')], max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('submission_date', models.DateTimeField()),
                ('days_listed', models.CharField(choices=[('7', '7 Days'), ('14', '14 Days'), ('21', '21 Days')], max_length=2)),
                ('pictures', models.ManyToManyField(blank=True, to='classifieds.Pictures')),
            ],
        ),
    ]

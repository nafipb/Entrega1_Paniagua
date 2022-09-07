from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blusas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('talla', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(default='anything', upload_to=None)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Busos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('talla', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(default='anything', upload_to=None)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('talla', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(default='anything', upload_to=None)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pantalones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('talla', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(default='anything', upload_to=None)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]

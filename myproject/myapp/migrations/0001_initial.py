# Generated by Django 3.2.7 on 2021-11-25 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basetable',
            fields=[
                ('base_id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('original_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image_name', models.CharField(max_length=20)),
                ('is_listimage', models.BooleanField(default=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('original_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('base_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Properties', to='myapp.basetable')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('is_listimage', models.BooleanField()),
                ('url', models.CharField(max_length=100)),
                ('base_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='myapp.basetable')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.properties')),
            ],
        ),
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('base_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dimensions', to='myapp.basetable')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.properties')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-15 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_haircategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('observation', models.CharField(max_length=400, null='True')),
                ('haircategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hairs', to='api.haircategory')),
            ],
            options={
                'db_table': 'Hair',
            },
        ),
    ]

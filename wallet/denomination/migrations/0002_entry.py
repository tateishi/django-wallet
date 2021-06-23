# Generated by Django 3.2.4 on 2021-06-23 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denomination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('y10k', models.IntegerField(default=0)),
                ('y5k', models.IntegerField(default=0)),
                ('y2k', models.IntegerField(default=0)),
                ('y1k', models.IntegerField(default=0)),
                ('y500', models.IntegerField(default=0)),
                ('y100', models.IntegerField(default=0)),
                ('y50', models.IntegerField(default=0)),
                ('y10', models.IntegerField(default=0)),
                ('y5', models.IntegerField(default=0)),
                ('y1', models.IntegerField(default=0)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denomination.wallet')),
            ],
        ),
    ]
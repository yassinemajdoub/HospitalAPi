# Generated by Django 4.0.4 on 2023-01-02 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Provider', '0001_initial'),
        ('patients', '0008_resource_alter_labresult_test_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Provider.provider')),
            ],
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]

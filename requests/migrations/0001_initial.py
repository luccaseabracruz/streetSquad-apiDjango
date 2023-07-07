# Generated by Django 4.2.2 on 2023-07-07 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('realizado', 'Realizado'), ('em andamento', 'Em Andamento'), ('concluido', 'Concluido')], default='realizado', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seller', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('seller', models.IntegerField(default=None, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.request')),
            ],
        ),
    ]
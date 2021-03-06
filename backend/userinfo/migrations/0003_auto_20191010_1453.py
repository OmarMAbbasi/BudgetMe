# Generated by Django 2.2 on 2019-10-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20191010_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microloan',
            old_name='amount',
            new_name='borrower_amount',
        ),
        migrations.RenameField(
            model_name='microloan',
            old_name='duration',
            new_name='borrower_duration',
        ),
        migrations.RenameField(
            model_name='microloan',
            old_name='interest',
            new_name='borrower_interest',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='noemail@noemail.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='microloan',
            name='borrower_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='microloan',
            name='creditor',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='microloan',
            name='creditor_status',
            field=models.BooleanField(default=False),
        ),
    ]

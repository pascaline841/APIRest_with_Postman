# Generated by Django 3.2.4 on 2021-07-09 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0013_rename_username_id_contributor_username'),
        ('issues', '0013_alter_issue_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='contributors.contributor'),
        ),
    ]

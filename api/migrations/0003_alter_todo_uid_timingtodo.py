# Generated by Django 4.1.3 on 2022-11-04 10:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_created_at_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('40dddeea-3a15-46aa-9021-d92ccc3aa5ce'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('40dddeea-3a15-46aa-9021-d92ccc3aa5ce'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
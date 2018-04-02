# Generated by Django 2.0 on 2018-01-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('reply_mark', models.IntegerField(blank=True, null=True)),
                ('reply_idea', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='班级名称')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='选项名称')),
                ('score', models.IntegerField(verbose_name='选项对应的分值')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='问题内容')),
                ('type', models.IntegerField(choices=[(1, '评分'), (2, '描述'), (3, '单选')])),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='问卷标题')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('password', models.CharField(max_length=32)),
                ('grade', models.ForeignKey(on_delete=None, to='dc.Grade', verbose_name='班级')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='班主任姓名')),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='create_user',
            field=models.ForeignKey(on_delete=None, to='dc.UserInfo', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='grade',
            field=models.ForeignKey(on_delete=None, to='dc.Grade', verbose_name='班级'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=None, to='dc.Questionnaire', verbose_name='问卷'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=None, to='dc.Question', verbose_name='问题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=None, to='dc.Question', verbose_name='问题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='reply_radio',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='dc.Option', verbose_name='单选选项'),
        ),
        migrations.AddField(
            model_name='answer',
            name='stu',
            field=models.ForeignKey(on_delete=None, to='dc.Student', verbose_name='学生'),
        ),
    ]

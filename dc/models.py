
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """
    班主任表
    """
    nid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=32,verbose_name='班主任姓名')

    def __str__(self):
        return self.username

class Grade(models.Model):
    """
    班级表
    """
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='班级名称')
    # stu_count=models.IntegerField()
    def __str__(self):
        return self.name

class Student(models.Model):
    """
    学生表
    和班级表是一对多的关系
    """
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='学生姓名')
    password = models.CharField(max_length=32)
    grade=models.ForeignKey(verbose_name='班级', to='Grade', to_field='nid',on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Questionnaire(models.Model):
    """
    问卷表
    和班主任表是一对多的关系
    和班级表是一对多的关系
    """
    nid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=32,verbose_name="问卷标题")
    create_user=models.ForeignKey(verbose_name='创建者', to='UserInfo', to_field='nid',on_delete=models.CASCADE)
    grade=models.ForeignKey(verbose_name='班级', to='Grade', to_field='nid',on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class Question(models.Model):
    """
    问题表
    和问卷表是一对多的关系
    """
    nid = models.AutoField(primary_key=True)
    choices = (
        (1, "评分"),
        (2, "描述"),
        (3, "单选"),
    )
    title=models.CharField(max_length=50,verbose_name='问题内容')
    type=models.IntegerField(choices=choices)

    questionnaire=models.ForeignKey(verbose_name='问卷', to='Questionnaire', to_field='nid',on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Option(models.Model):
    """
    单选选项表
    和问题表是一对多的关系
    """
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,verbose_name="选项名称")
    score=models.IntegerField(verbose_name='选项对应的分值')

    question=models.ForeignKey(verbose_name='问题', to='Question', to_field='nid',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Answer(models.Model):
    """
    回答表
    和学生表是一对多的关系
    和问题表是一对多的关系
    """
    nid = models.AutoField(primary_key=True)
    # 针对评分的回答
    reply_mark=models.IntegerField(null=True,blank=True)
    # 针对描述的回答
    reply_idea=models.CharField(max_length=255,null=True,blank=True)
    # 针对单选的回答
    reply_radio=models.ForeignKey(verbose_name='单选选项',null=True,blank=True, to='Option', to_field='nid',on_delete=models.CASCADE)

    stu=models.ForeignKey(verbose_name='学生', to='Student', to_field='nid',on_delete=models.CASCADE)
    question=models.ForeignKey(verbose_name='问题', to='Question', to_field='nid',on_delete=models.CASCADE)
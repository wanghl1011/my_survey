from django.db import models

# Create your models here.

from django.db import models

# Create your models here.



from django.db import models

class UserInfo(models.Model):
    """
    员工表
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class ClassInfo(models.Model):
    """
    班级表
    """
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Student(models.Model):
    """
    学生表
    """
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    cls = models.ForeignKey(to=ClassInfo)
    def __str__(self):
        return self.user


class Questionnaire(models.Model):
    """
    问卷表

    """
    title = models.CharField(max_length=64)
    cls = models.ForeignKey(to=ClassInfo)
    creator = models.ForeignKey(to=UserInfo)

    def __str__(self):
        return self.title

class Question(models.Model):
    """
    问题表
    """
    caption = models.CharField(max_length=64)

    question_type = (
        (1,'打分'),
        (2,'单选'),
        (3,'评价'),
    )
    question_type = models.IntegerField(choices=question_type)

    questionnaire = models.ForeignKey(Questionnaire,default=1)
    def __str__(self):
        return self.caption

class Option(models.Model):
    """
    单选题的选项
    """
    option_name = models.CharField(verbose_name='选项名称',max_length=32)
    score = models.IntegerField(verbose_name='选项对应的分值')
    question = models.ForeignKey(to=Question)
    def __str__(self):
        return self.option_name
class Answer(models.Model):
    """
    回答
    """
    student = models.ForeignKey(to=Student)
    question = models.ForeignKey(to=Question)

    # 三选一
    option = models.ForeignKey(to="Option",null=True,blank=True)
    val = models.IntegerField(null=True,blank=True)
    content = models.CharField(max_length=255,null=True,blank=True)















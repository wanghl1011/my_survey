from django.shortcuts import render, redirect, HttpResponse
from dc.forms import *
from dc.models import *
import json
from django.db import transaction
# Create your views here.
def edit_question(request,keyword):
    # question_form=Ques_form()
    if request.method=='POST':

        old_question_list=Question.objects.filter(questionnaire_id=keyword).values("nid","title","type")
        post_question_list = json.loads(request.body.decode())

        post_question_dict = {item.get("nid"): item for item in post_question_list}
        old_question_dict = {item.get("nid"): item for item in old_question_list}

        # print("post_question_dict",post_question_dict)
        # print("old_question_dict",old_question_dict)

        post_question_id_set=set([i for i in post_question_dict])
        old_question_id_set=set([i for i in old_question_dict])


        # print("post_question_id_set",post_question_id_set)
        # print("old_question_id_set",old_question_id_set)

        # 删除问题
        del_question_id=list(old_question_id_set - post_question_id_set)
        # print("del_question_id",del_question_id)
        with transaction.atomic():
            Option.objects.filter(question__nid__in=del_question_id).delete()
            Question.objects.filter(nid__in=del_question_id).delete()


        # 添加问题
        add_question_id = list(post_question_id_set - old_question_id_set)
        # print("add_question_id : ", add_question_id)
        with transaction.atomic():
            for question_id in add_question_id:
                add_question_dict = post_question_dict.get(question_id)
                question=Question.objects.create(title=add_question_dict.get("title"),type=add_question_dict.get("type"),questionnaire_id=keyword)
                if question.type == 3:
                    add_option_list=add_question_dict.get("option_list")
                    for add_option_dict in add_option_list:
                        # print("add_option_dict",add_option_dict)
                        Option.objects.create(name=add_option_dict.get("name"),score=add_option_dict.get("score"), question_id =question.nid)



        # 编辑问题
        edit_question_id = list(post_question_id_set & old_question_id_set)
        # print("edit_question_id : ",edit_question_id)

        for edit_id in edit_question_id:

            # 当前问题的前端数据
            post_edit_question_dict=post_question_dict.get(edit_id)
            # 当前问题的数据库数据
            old_edit_question_dict=old_question_dict.get(edit_id)


            # 当前问题的单选选项列表
            post_edit_question_option_list=post_edit_question_dict.pop("option_list")
            # 当前问题的数据库中的单选选项列表
            old_edit_question_option_list=list(Option.objects.filter(question__nid=edit_id).values("nid","name","score"))

            # print("post_edit_question_dict",post_edit_question_dict)
            # print("old_edit_question_dict",old_edit_question_dict)

            # print("post_edit_question_option_list",post_edit_question_option_list)
            # print("old_edit_question_option_list",old_edit_question_option_list)

            if post_edit_question_dict == old_edit_question_dict and post_edit_question_option_list == old_edit_question_option_list:
                print(post_edit_question_dict.get("title"),"该问题没有进行任何修改")
            else:

                # 问题的名称和类型被修改
                Question.objects.filter(nid=edit_id).update(title=post_edit_question_dict.get("title"),type=post_edit_question_dict.get("type"))

                # 选项的增删改

                # 当前问题的单选选项字典
                post_option_dict = {item.get("nid"): item for item in post_edit_question_option_list}
                # 当前问题的单选选项数据库字典
                old_option_dict = {item.get("nid"): item for item in old_edit_question_option_list}

                print("post_option_dict", post_option_dict)
                print("old_option_dict", old_option_dict)

                post_option_id_set = set([i for i in post_option_dict])
                old_option_id_set = set([i for i in old_option_dict])


                # 删除选项
                del_option_id = list(old_option_id_set - post_option_id_set)
                with transaction.atomic():
                    Option.objects.filter(nid__in=del_option_id).delete()

                # 添加选项
                add_option_id = list(post_option_id_set - old_option_id_set)
                with transaction.atomic():
                    for option_id in add_option_id:
                        add_option_dict = post_option_dict.get(option_id)
                        option = Option.objects.create(name=add_option_dict.get("name"),score=add_option_dict.get("score"),question_id=edit_id)


                # 编辑选项
                edit_option_id = list(post_option_id_set & old_option_id_set)
                with transaction.atomic():
                    for o_id in edit_option_id:
                        # 单个选项
                        post_edit_option_dict=post_option_dict.get(o_id)
                        old_edit_option_dict=old_option_dict.get(o_id)
                        if post_edit_option_dict == old_edit_option_dict:
                            print(post_edit_option_dict.get("name"),"该选项没有更改")
                        else:
                            # 选项的内容和分值被修改
                            Option.objects.filter(nid=o_id).update(name=post_edit_option_dict.get("name"),score=post_edit_option_dict.get("score"))
        return HttpResponse("OK")
    else:
        question_list = Question.objects.filter(questionnaire_id=keyword)
        def generate_question_modelform_info():
            for question in question_list:
                question_modelform = Ques_modelform(instance=question)
                if question.type == 3:

                    # option_modelform_list=[]t
                    def generate_option_modelform_info(question):
                        option_list = question.option_set.all()
                        for option in option_list:
                            option_modelform=Option_modelform(instance=option)
                            yield {"option":option,"option_modelform":option_modelform}
                    yield {"question":question,"question_modelform":question_modelform,"generate_option_modelform_info":generate_option_modelform_info(question)}
                            # option_list = question.option_set.all()
                            # for option in option_list:
                            #     option_modelform = Option_modelform(instance=option)
                    #     option_modelform_list.append(option_modelform)
                    # yield {"question":question,"question_modelform":question_modelform,"option_modelform_list":option_modelform_list}

                else:
                    yield {"question":question, "question_modelform": question_modelform}

        return render(request, 'edit_question_yield.html', {"naire_id":keyword, "generate_question_modelform_info": generate_question_modelform_info()})









    # option_form_list = []
    # question_option_info=[]
    # for question in question_list:
    #     question_dict = {}
    #     question_dict["question"]=question
    #     question_form = Ques_modelform(instance=question)
    #     question_dict["question_form"] = question_form
    #     if question.type == 3:
    #         option_list=question.option_set.all()
    #         for option in option_list:
    #             option_form = Option_modelform(instance=option)
    #             option_form_list.append(option_form)
    #         question_dict["option_form_list"] = option_form_list
    #     question_option_info.append(question_dict)
    # return render(request,'edit_question.html',{"question_option_info":question_option_info})























































def index(request):

    naire_list=Questionnaire.objects.all()
    return render(request,'index.html',locals())

def edit_questionnaire(request,id):
    if request.method=='POST':
        questionnaire = Questionnaire.objects.get(nid=id)
        questionnaire_form = Questionnaire_modelform(instance=questionnaire,data=request.POST)
        questionnaire_form.save()
        return redirect("/dc/index")
    else:
        questionnaire_id=id
        questionnaire=Questionnaire.objects.get(nid=id)
        questionnaire_form=Questionnaire_modelform(instance=questionnaire)
        return render(request, 'edit_naire.html', locals())

def add_questionnaire(request):
    if request.method=='POST':
        questionnaire_form = Questionnaire_modelform(data=request.POST)
        questionnaire_form.save()
        return redirect("/dc/index")
    else:
        questionnaire_form=Questionnaire_modelform()

        return render(request, 'add_naire.html', locals())

def del_naire(request,id):
    Questionnaire.objects.filter(nid=id).delete()
    return redirect("/dc/index")



def add_edit_naire(request,id):
    if request.method=='POST':
        if id.isdigit():
            questionnaire = Questionnaire.objects.get(nid=id)
            questionnaire_form = Questionnaire_modelform(instance=questionnaire, data=request.POST)
            questionnaire_form.save()
            return redirect("/dc/index")
        else:
            questionnaire_form = Questionnaire_modelform(data=request.POST)
            questionnaire_form.save()
            return redirect("/dc/index")
    else:
        if id.isdigit():
            questionnaire_id = id
            questionnaire = Questionnaire.objects.get(nid=id)
            questionnaire_form = Questionnaire_modelform(instance=questionnaire)
            return render(request, 'add_edit_naire.html', locals())
        else:
            questionnaire_id = "afdsd"
            questionnaire_form = Questionnaire_modelform()
            return render(request, 'add_edit_naire.html', locals())


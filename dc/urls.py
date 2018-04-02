from django.conf.urls import url,include
from dc import views
urlpatterns = [
    url(r'^edit/question/(?P<keyword>\d+)',views.edit_question),
    url(r'^index',views.index),
    url(r'^add/naire',views.add_questionnaire),
    url(r'^edit/naire/(?P<id>\d+)',views.edit_questionnaire),
    url(r'^del/naire/(?P<id>\d+)',views.del_naire),
    url(r'^add_edit/naire/(?P<id>\w+)',views.add_edit_naire),
]
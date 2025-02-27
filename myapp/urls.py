"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_subject_settings_add', views.admin_subject_settings_add,name='admin_subject_settings_add'),
    path('admin_subject_settings_delete', views.admin_subject_settings_delete,name='admin_subject_settings_delete'),
    path('admin_subject_settings_view', views.admin_subject_settings_view,name='admin_subject_settings_view'),

    path('admin_user_details_view', views.admin_user_details_view,name='admin_user_details_view'),


    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_doc_pool_add', views.user_doc_pool_add,name='user_doc_pool_add'),
    path('user_doc_pool_delete', views.user_doc_pool_delete, name='user_doc_pool_delete'),
    path('user_doc_pool_view', views.user_doc_pool_view,name='user_doc_pool_view'),

    path('user_question_bank_view', views.user_question_bank_view,name='user_question_bank_view'),
    path('user_question_bank_question_view', views.user_question_bank_question_view, name='user_question_bank_question_view'),


    path('user_schedule_master_add', views.user_schedule_master_add,name='user_schedule_master_add'),
    path('user_schedule_master_delete', views.user_schedule_master_delete,name='user_schedule_master_delete'),
    path('user_schedule_master_view', views.user_schedule_master_view,name='user_schedule_master_view'),

    path('user_marklist_details_add', views.user_marklist_details_add,name='user_marklist_details_add'),
    path('user_marklist_details_delete', views.user_marklist_details_delete, name='user_marklist_details_delete'),
    path('user_marklist_details_view', views.user_marklist_details_view, name='user_marklist_details_view'),

    path('user_schedule_details_add', views.user_schedule_details_add,name='user_schedule_details_add'),
    path('user_schedule_details_view', views.user_schedule_details_view,name='user_schedule_details_view'),
    path('user_schedule_details_delete', views.user_schedule_details_delete,name='user_schedule_details_delete'),

    path('user_module_details_add', views.user_module_details_add,name='user_module_details_add'),
    path('user_module_details_view', views.user_module_details_view,name='user_module_details_view'),
    path('user_module_details_delete', views.user_module_details_delete,name='user_module_details_delete'),

    path('user_generate_planner_view', views.user_generate_planner_view,name='user_generate_planner_view'),
]

from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

#################ADMIN##################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

# subject_settings - id, subject_name
from .models import subject_settings
def admin_subject_settings_add(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        dm = subject_settings(subject_name=subject_name)
        dm.save()
        context ={'msg':'Record added'}
        return render(request, 'myapp/admin_subject_settings_add.html', context)

    else:
        return render(request, 'myapp/admin_subject_settings_add.html')


def admin_subject_settings_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = subject_settings.objects.get(id=int(id))
    nm.delete()

    nm_l = subject_settings.objects.all()
    context ={'subject_list':nm_l}
    return render(request,'myapp/admin_subject_settings_view.html',context)

def admin_subject_settings_view(request):
    nm_l = subject_settings.objects.all()
    context ={'subject_list':nm_l}
    return render(request,'myapp/admin_subject_settings_view.html',context)

def admin_user_details_view(request):
    ul_l = user_login.objects.filter(u_type='user')

    tm_l = []
    for u in ul_l:
        if u.id ==1:
            continue
        ud = user_details.objects.get(user_id=u.id)
        tm_l.append(ud)
    context = {'user_list':tm_l,'type':'User Details'}
    return render(request, './myapp/admin_user_details_view.html',context)
#################################################################################
############################USER####################################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, dob=dob,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)



from datetime import datetime
from .models import doc_pool, question_bank1,question_bank2,question_bank3
from django.core.files.storage import FileSystemStorage
from .pdf_handler import get_content
import os
from project.settings import BASE_DIR
# doc_pool - id, user_id, doc_file, dt, tm , status
from .bert_handler import *
from .question_pool_generator import generate_all_questions
def user_doc_pool_add(request):
    if request.method == 'POST':
        u_file = request.FILES['document']
        fs = FileSystemStorage()
        doc_file = fs.save(u_file.name, u_file)
        user_id = request.session['user_id']
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'
        ud_obj = doc_pool(user_id=int(user_id), doc_file=doc_file, 
                           dt=dt, tm=tm, status=status )
        ud_obj.save()

        doc_id = doc_pool.objects.all().aggregate(Max('id'))['id__max']
        user_id = request.session['user_id']
        ########### Document Processing ###################
        fpath = os.path.join(BASE_DIR, f'myapp\\static\\myapp\\media\\{doc_file}')
        doc_contents = get_content(fpath)
        question_bank1_list, question_bank2_list, question_bank3_list = generate_all_questions(doc_contents=doc_contents)
        #print(question_bank1_list, question_bank2_list, question_bank3_list)
        for qb1 in question_bank1_list:
            qb1_obj = question_bank1(user_id=int(user_id), doc_id=doc_id, 
                                      question=qb1['question1'], answer=qb1['answer1'], mark=1)
            qb1_obj.save()
        
        for qb2 in question_bank2_list:
            qb2_obj = question_bank2(user_id=int(user_id), doc_id=doc_id,                                 question=qb2['question2'], answer=qb2['answer2'], mark=3)
            qb2_obj.save()

        for qb3 in question_bank3_list:
            qb3_obj = question_bank3(user_id=int(user_id), 
                                      doc_id=doc_id, 
                                      op1=qb3['op1'], op2=qb3['op2'], op3=qb3['op3'], op4=qb3['op4'],
                                      question=qb3['question3'], answer=qb3['answer'],                          mark=1)
            qb3_obj.save()
            
        #####################################################
        # print(results)
        # # question_bank1 - id, user_id, doc_id, question, answer, mark
        # # question_bank2 - id, user_id, doc_id, question, answer, mark
        # # question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark
        # i = 1
        # for result in results:
        #     keywords=get_keywords(result)
        #     keywords_str = ','.join(keywords)
        #     question2 = 'Write a short description on what is '+ keywords_str
        #     answer2 = result
        #     question3 = 'Question '+ str(i)
        #     summary_list=get_summary(result)
        #     for s in summary_list:
        #         question1 = ''
        #         answer1 = ''
        #         try:
        #             temp_key = get_keywords(s)                
        #             question1 = s
        #             for t in temp_key:
        #                 question1 = question1.replace(t,'_')
        #             answer1 = ','.join(temp_key)
            
        #             # question_bank1 - id, user_id, doc_id, question, answer, mark
        #             qb1_obj = question_bank1(user_id=int(user_id), 
        #                              doc_id=doc_id, 
        #                              question=question1, answer=answer1, 
        #                              mark=1)
        #             qb1_obj.save()
        #         except:
        #             continue

        #     # question_bank2 - id, user_id, doc_id, question, answer, mark
        #     qb2_obj = question_bank2(user_id=int(user_id), 
        #                              doc_id=doc_id, 
        #                              question=question2, answer=answer2, 
        #                              mark=3)
        #     qb2_obj.save()
        #     # question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark
        #     qb3_obj = question_bank3(user_id=int(user_id), 
        #                              doc_id=doc_id, 
        #                              op1='op1', op2='op2', op3='op3', op4='op4',
        #                              question=question3, answer='op1', 
        #                              mark=1)
        #     qb3_obj.save()
            
        #     i +=1
        # ################################
        context = {'msg':'New document uploaded and questions generated'}
        return render(request, 'myapp/user_doc_pool_add.html',context)

    else:
        context = {'msg':''}
        return render(request, 'myapp/user_doc_pool_add.html',context)

def user_doc_pool_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ud_obj = doc_pool.objects.get(id=int(id))
    ud_obj.delete()

    user_id = request.session['user_id']
    ud_list = doc_pool.objects.filter(user_id=int(user_id))
    print(len(ud_list))
    context = {'doc_list':ud_list, 'msg': 'Document Deleted'}
    return render(request, 'myapp/user_doc_pool_view.html', context)

def user_doc_pool_view(request):
    user_id = request.session['user_id']
    ud_list = doc_pool.objects.filter(user_id=int(user_id))
    print(len(ud_list))
    context = {'doc_list':ud_list, 'msg': ''}
    return render(request, 'myapp/user_doc_pool_view.html', context)

def user_question_bank_view(request):
    user_id = request.session['user_id']
    doc_id = request.GET.get('doc_id')
    # question_bank1 - id, user_id, doc_id, question, answer, mark
    # question_bank2 - id, user_id, doc_id, question, answer, mark
    # question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark
    
    qb1_list = question_bank1.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    qb2_list = question_bank2.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    qb3_list = question_bank3.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    
    
    context = {
        'qb1_list':qb1_list,
        'qb2_list':qb2_list,
        'qb3_list':qb3_list,
        'msg': ''}
    return render(request, 'myapp/user_question_bank_view.html', context)

def user_question_bank_question_view(request):
    user_id = request.session['user_id']
    doc_id = request.GET.get('doc_id')
    # question_bank1 - id, user_id, doc_id, question, answer, mark
    # question_bank2 - id, user_id, doc_id, question, answer, mark
    # question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark
    
    qb1_list = question_bank1.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    qb2_list = question_bank2.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    qb3_list = question_bank3.objects.filter(user_id=int(user_id), doc_id=int(doc_id))
    
    
    context = {
        'qb1_list':qb1_list,
        'qb2_list':qb2_list,
        'qb3_list':qb3_list,
        'msg': ''}
    return render(request, 'myapp/user_question_bank_question_view.html', context)



# schedule_master - id, user_id, subjects, total_duration, dt, tm, status
from .models import schedule_master
def user_schedule_master_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']

        subjects = request.POST.get('subjects')
        total_duration = request.POST.get('total_duration')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'pending'

        sm_obj = schedule_master( user_id=int(user_id), subjects=subjects,  
                                 total_duration=int(total_duration),
                              dt=dt, tm=tm, status=status)
        sm_obj.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/user_schedule_master_add.html', context)
    else:
        context = {}
        return render(request, './myapp/user_schedule_master_add.html',context)

def user_schedule_master_delete(request):

    id = request.GET.get('id')
    print('id = '+id)
    pp = schedule_master.objects.get(id=int(id))
    pp.delete()
    msg = 'Record Deleted'
    user_id = request.session['user_id']
    schedule_master_list = schedule_master.objects.filter(user_id=int(user_id))
    
    context = {'schedule_master_list': schedule_master_list,'msg':msg}
    return render(request, './myapp/user_schedule_master_view.html', context)

def user_schedule_master_view(request):
    user_id = request.session['user_id']
    schedule_master_list = schedule_master.objects.filter(user_id=int(user_id))
    context = {'schedule_master_list': schedule_master_list}
    return render(request, './myapp/user_schedule_master_view.html', context)


# marklist_details - id, schedule_master_id, sub1_id, sub1_mark, sub2_id, sub2_mark, sub3_id, sub3_mark, sub4_id, sub4_mark, sub5_id, sub5_mark 
from .models import marklist_details

def user_marklist_details_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        
        schedule_master_id = int(request.POST.get('schedule_master_id'))
        sub1_id = int(request.POST.get('sub1_id'))
        sub1_mark = float(request.POST.get('sub1_mark'))
        sub2_id = int(request.POST.get('sub2_id'))
        sub2_mark = float(request.POST.get('sub2_mark'))
        sub3_id = int(request.POST.get('sub3_id'))
        sub3_mark = float(request.POST.get('sub3_mark'))
        sub4_id = int(request.POST.get('sub4_id'))
        sub4_mark = float(request.POST.get('sub4_mark'))
        sub5_id = int(request.POST.get('sub5_id'))
        sub5_mark = float(request.POST.get('sub5_mark'))
        
        # dt = datetime.today().strftime('%Y-%m-%d')
        # tm = datetime.today().strftime('%H:%M:%S')
        # status = 'ok'

        md_obj = marklist_details(schedule_master_id=schedule_master_id, 
                                  sub1_id=sub1_id, sub1_mark=sub1_mark, 
                                  sub2_id=sub2_id, sub2_mark=sub2_mark, 
                                  sub3_id=sub3_id, sub3_mark=sub3_mark, 
                                  sub4_id=sub4_id, sub4_mark=sub4_mark, 
                                  sub5_id=sub5_id, sub5_mark=sub5_mark)
        md_obj.save()
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_master_id':schedule_master_id,
                   'msg':'Record added'}
        return render(request, 'myapp/user_marklist_details_add.html',context)

    else:
        schedule_master_id = int(request.GET.get('schedule_master_id'))
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_master_id':schedule_master_id,
                   'msg':''}
        return render(request, 'myapp/user_marklist_details_add.html',context)

def user_marklist_details_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ml_obj = marklist_details.objects.get(id=int(id))
    ml_obj.delete()

    schedule_master_id = int(request.GET.get('schedule_master_id'))
    user_id = request.session['user_id']
    ml_l = marklist_details.objects.filter(schedule_master_id=schedule_master_id)
    ss_l = subject_settings.objects.all()
    context ={'marklist_list':ml_l,'subject_list': ss_l, 
              'schedule_master_id':schedule_master_id,'msg':'Marklist deleted'}
    return render(request,'myapp/user_marklist_details_view.html',context)

def user_marklist_details_view(request):
    schedule_master_id = int(request.GET.get('schedule_master_id'))
    user_id = request.session['user_id']
    ml_l = marklist_details.objects.filter(schedule_master_id=schedule_master_id)
    ss_l = subject_settings.objects.all()
    context ={'marklist_list':ml_l,'subject_list': ss_l, 
              'schedule_master_id':schedule_master_id,'msg':''}
    return render(request,'myapp/user_marklist_details_view.html',context)



# schedule_details - id, schedule_master_id, subject_id, priority
from .models import schedule_details
def user_schedule_details_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        
        schedule_master_id = int(request.POST.get('schedule_master_id'))
        subject_id = int(request.POST.get('subject_id'))
        priority = 1 #float(request.POST.get('priority'))
        
        # dt = datetime.today().strftime('%Y-%m-%d')
        # tm = datetime.today().strftime('%H:%M:%S')
        # status = 'ok'

        md_obj = schedule_details(schedule_master_id=schedule_master_id, 
                                  subject_id=subject_id, priority=priority)
        md_obj.save()
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_master_id':schedule_master_id,
                   'msg':'Record added'}
        return render(request, 'myapp/user_schedule_details_add.html',context)

    else:
        schedule_master_id = int(request.GET.get('schedule_master_id'))
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_master_id':schedule_master_id,
                   'msg':''}
        return render(request, 'myapp/user_schedule_details_add.html',context)

def user_schedule_details_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ml_obj = schedule_details.objects.get(id=int(id))
    ml_obj.delete()

    schedule_master_id = int(request.GET.get('schedule_master_id'))
    user_id = request.session['user_id']
    ml_l = schedule_details.objects.filter(schedule_master_id=schedule_master_id)
    ss_l = subject_settings.objects.all()
    context ={'schedule_details':ml_l,'subject_list': ss_l, 
              'schedule_master_id':schedule_master_id,'msg':'Subject deleted'}
    return render(request,'myapp/user_schedule_details_view.html',context)

def user_schedule_details_view(request):
    schedule_master_id = int(request.GET.get('schedule_master_id'))
    user_id = request.session['user_id']
    ml_l = schedule_details.objects.filter(schedule_master_id=schedule_master_id)
    ss_l = subject_settings.objects.all()
    context ={'schedule_details':ml_l,'subject_list': ss_l, 
              'schedule_master_id':schedule_master_id,'msg':''}
    return render(request,'myapp/user_schedule_details_view.html',context)


# module_details - id, schedule_details_id, module_title, module_description
from .models import module_details
def user_module_details_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        
        schedule_details_id = int(request.POST.get('schedule_details_id'))
        module_title = str(request.POST.get('module_title'))
        module_description = str(request.POST.get('module_description'))
        
        # dt = datetime.today().strftime('%Y-%m-%d')
        # tm = datetime.today().strftime('%H:%M:%S')
        # status = 'ok'

        md_obj = module_details(schedule_details_id=schedule_details_id, 
                                  module_title=module_title, module_description=module_description)
        md_obj.save()
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_details_id':schedule_details_id,
                   'msg':'Record added'}
        return render(request, 'myapp/user_module_details_add.html',context)

    else:
        schedule_details_id = int(request.GET.get('schedule_details_id'))
        ss_list = subject_settings.objects.all()
        context = {'subject_list':ss_list,
                   'schedule_details_id':schedule_details_id,
                   'msg':''}
        return render(request, 'myapp/user_module_details_add.html',context)

def user_module_details_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ml_obj = module_details.objects.get(id=int(id))
    ml_obj.delete()

    schedule_details_id = int(request.GET.get('schedule_details_id'))
    user_id = request.session['user_id']
    ml_l = module_details.objects.filter(schedule_details_id=schedule_details_id)
    ss_l = subject_settings.objects.all()
    context ={'module_details':ml_l,'subject_list': ss_l, 
              'schedule_details_id':schedule_details_id,'msg':'Module deleted'}
    return render(request,'myapp/user_module_details_view.html',context)

def user_module_details_view(request):
    schedule_details_id = int(request.GET.get('schedule_details_id'))
    user_id = request.session['user_id']
    ml_l = module_details.objects.filter(schedule_details_id=schedule_details_id)
    ss_l = subject_settings.objects.all()
    context ={'module_details':ml_l,'subject_list': ss_l, 
              'schedule_details_id':schedule_details_id,'msg':''}
    return render(request,'myapp/user_module_details_view.html',context)

from .planner_test import get_planning
def user_generate_planner_view(request):
    schedule_master_id = int(request.GET.get('schedule_master_id'))
    sm_obj = schedule_master.objects.get(id=schedule_master_id)
    subject_list = schedule_details.objects.filter(schedule_master_id=schedule_master_id)
    modules_input = []
    md_list  = marklist_details.objects.filter(schedule_master_id=schedule_master_id)
    mark_d = {}
    print(len(md_list))
    if(len(md_list) == 2):
        mark_d[md_list[0].sub1_id] = (md_list[0].sub1_mark+md_list[1].sub1_mark )/2
        mark_d[md_list[0].sub2_id] = (md_list[0].sub2_mark+md_list[1].sub2_mark )/2
        mark_d[md_list[0].sub3_id] = (md_list[0].sub3_mark+md_list[1].sub3_mark )/2
        mark_d[md_list[0].sub4_id] = (md_list[0].sub4_mark+md_list[1].sub4_mark )/2
        mark_d[md_list[0].sub5_id] = (md_list[0].sub5_mark+md_list[1].sub5_mark )/2
    else:
        context ={'msg':'Not enough marks'}
        return render(request,'myapp/user_home.html',context)
    mark_sorted_list = list(mark_d.values())
    mark_sorted_list.sort()

    dict(sorted(mark_d.items(), key=lambda item: item[1]))
    print('************************', mark_d, mark_sorted_list)
    for sl in subject_list:
        subject_obj = subject_settings.objects.get(id=sl.subject_id)
        ml_l = module_details.objects.filter(schedule_details_id=sl.id)
        subject_name=subject_obj.subject_name
        s_mark = mark_d[subject_obj.id]
        s_priority = mark_sorted_list.index(s_mark)+1
        print(s_mark, s_priority, '***')
        priority = s_priority#int(sl.priority)
        for ml in ml_l:
            m_d={"name": f"{subject_name}-{ml.module_title}",  "priority": priority}
            modules_input.append(m_d)

    modules_output = get_planning(modules_input, sm_obj.total_duration)
    context ={'module_list':modules_output}
    return render(request,'myapp/user_generate_planner_view.html',context)

###################################################


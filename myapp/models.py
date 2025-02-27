from django.db import models

# user_login - id, uname ,passwd ,u_type 
# user_details - id, user_id ,fname ,lname ,gender ,dob ,addr ,pin ,contact ,email
# schedule_master - id, user_id, subjects, total_duration, dt, tm, status
# marklist_details - id, schedule_master_id, sub1_id, sub1_mark, sub2_id, sub2_mark, sub3_id, sub3_mark, sub4_id, sub4_mark, sub5_id, sub5_mark 
# subject_settings - id, subject_name
# schedule_details - id, schedule_master_id, subject_id, priority
# module_details - id, schedule_details_id, module_title, module_description
# schedule_planner - id, schedule_master_id, subject_id, module_id, duration, dt, tm, status
# doc_pool - id, user_id, doc_file, dt, tm , status
# question_bank1 - id, user_id, doc_id, question, answer, mark
# question_bank2 - id, user_id, doc_id, question, answer, mark
# question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark


# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname

class schedule_master(models.Model):
    #id
    user_id = models.IntegerField()
    subjects  = models.CharField(max_length=100) 
    total_duration = models.IntegerField()
    dt  = models.CharField(max_length=15) 
    tm  = models.CharField(max_length=15)
    status  = models.CharField(max_length=20)


class marklist_details(models.Model):
    #- id
    schedule_master_id =models.IntegerField()
    sub1_id = models.IntegerField()
    sub1_mark = models.FloatField()
    sub2_id = models.IntegerField()
    sub2_mark = models.FloatField()
    sub3_id = models.IntegerField()
    sub3_mark = models.FloatField()
    sub4_id = models.IntegerField()
    sub4_mark = models.FloatField()
    sub5_id = models.IntegerField()
    sub5_mark = models.FloatField()

class subject_settings(models.Model):
    # id
    subject_name  = models.CharField(max_length=100)

class schedule_details(models.Model):
    # id
    schedule_master_id = models.IntegerField()
    subject_id = models.IntegerField()
    priority = models.FloatField()

class module_details(models.Model):
    # id
    schedule_details_id = models.IntegerField()
    module_title  = models.CharField(max_length=100)
    module_description  = models.CharField(max_length=1000)

class schedule_planner(models.Model):
    # id 
    schedule_master_id = models.IntegerField()
    subject_id = models.IntegerField()
    module_id = models.IntegerField()
    duration =models.IntegerField()
    dt  = models.CharField(max_length=15) 
    tm  = models.CharField(max_length=15)
    status  = models.CharField(max_length=20)

class doc_pool(models.Model):
    # id
    user_id = models.IntegerField()
    doc_file  = models.CharField(max_length=250)
    dt  = models.CharField(max_length=15)
    tm  = models.CharField(max_length=15)
    status  = models.CharField(max_length=20)

class question_bank1(models.Model):
    # id
    user_id = models.IntegerField()
    doc_id = models.IntegerField()
    question  = models.CharField(max_length=300)
    answer  = models.CharField(max_length=1000) 
    mark = models.FloatField()

class question_bank2(models.Model):
    # id
    user_id = models.IntegerField()
    doc_id = models.IntegerField()
    question  = models.CharField(max_length=300)
    answer  = models.CharField(max_length=1000) 
    mark = models.FloatField()
    
class question_bank3(models.Model):
    # id
    user_id = models.IntegerField()
    doc_id = models.IntegerField()
    question = models.CharField(max_length=300)
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)
    answer = models.CharField(max_length=300) 
    mark = models.FloatField()

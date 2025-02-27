from django.contrib import admin

# Register your models here.
from .models import user_login, user_details

from.models import doc_pool, schedule_details,schedule_master,schedule_planner,marklist_details
from.models import user_details,question_bank3,question_bank1,question_bank2


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(question_bank3)
admin.site.register(question_bank1)
admin.site.register(question_bank2)
admin.site.register(doc_pool)
admin.site.register(marklist_details)
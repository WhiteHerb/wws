from django.contrib import admin
from .models import Uploaduseranswer,Uploadanswer

admin.site.register(Uploaduseranswer,name='답지')
admin.site.register(Uploadanswer,name='결과')

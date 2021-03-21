from django.contrib import admin
from .models import Quiz,Question,Choice,CustomUser,Answer
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display =['email','username','first_name','last_name','age','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)


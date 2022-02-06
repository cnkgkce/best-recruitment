from django.contrib import admin
from .models import Candidate


# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("username","profile_url",)
    search_fields = ("username",)
    readonly_fields = ('username','profile_url',)


admin.site.register(Candidate)
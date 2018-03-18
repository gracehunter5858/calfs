from django.contrib import admin

# Register your models here.

from .models import Member
admin.site.site_header = "Cal FS Admin"

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')
    list_filter = ('team',)
    fields = (
        'name', 'year', ('major_1', 'major_2'), ('minor_1', 'minor_2'),
        'hometown', 'team', 'photo', 'officer_position'
    )

admin.site.register(Member, MemberAdmin)

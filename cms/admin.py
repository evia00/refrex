from django.contrib import admin


from cms.models import User, Auth


class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', )
    list_display_links = ('userId', )


admin.site.register(User, UserAdmin)


class AuthAdmin(admin.ModelAdmin):
    list_display = ('authId', 'regTs')
    list_display_links = ('authId',)


admin.site.register(Auth, AuthAdmin)

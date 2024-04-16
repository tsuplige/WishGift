from django.contrib import admin
from authentication.models import User
from .models import UserFollows

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(UserFollows)
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following_user_id', 'created')

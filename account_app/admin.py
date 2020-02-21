from django.contrib import admin

from .models import SubHead, SubEntry, Entry, SubHeadAccount
# Register your models here.


# admin.site.register(SubEntry)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    search_fields = ['dated']
    list_display = ['dated','total_amount', 'created_on', 'modified_on']
    list_filter = ['dated', 'created_on','modified_on']

@admin.register(SubHead)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['sub_head', 'head']

@admin.register(SubEntry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['sub_head_account', 'sub_head', 'head', 'amount']

    def sub_head(self, obj):
        return obj.sub_head_account.sub_head.sub_head

    def head(self, obj):
        return obj.sub_head_account.sub_head.head


@admin.register(SubHeadAccount)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['sub_head_account', 'description', 'sub_head', 'head']

    def head(self, obj):
        return obj.sub_head.head
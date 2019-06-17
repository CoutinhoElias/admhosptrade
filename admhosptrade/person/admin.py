from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline

from admhosptrade.person.models import Person, PersonCategory


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'name')
    search_fields = ('id', 'name')
    # inlines = [InlineContact, ]

@admin.register(PersonCategory)
class PersonCategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'name')
    search_fields = ('id', 'name')
    # inlines = [InlineContact, ]

# @admin.register(Kind)
# class KindAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'id', 'kind')
#     search_fields = ('id', 'kind')


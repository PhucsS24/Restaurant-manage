from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking
from django.contrib.admin.actions import action
# Register your models here.
# @action(name="Đánh Dấu Hoàn Thành (Marked)", permissions=['change'])  # Action details
# def mark_completed(self, request, queryset):
#     queryset.update(status='marked')  # Update 'status' field to 'marked'
#     return None  # Optional: Return a success message (see note)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('select_location', 'select_size', 'choice_time','choice_date' ,'fname', 'lname')
    list_filter = ('select_location', 'select_size', 'choice_time','choice_date')  # Add list filters
    search_fields = ['select_location', 'fname', 'lname', 'email']  # Add search fields
    # actions = [mark_completed] 

admin.site.register(Booking,BookingAdmin)
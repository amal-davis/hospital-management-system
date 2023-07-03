from django.contrib import admin
from hospitalapp.models import Bookings_model
from django.utils.html import format_html
from django.urls import reverse



# Register your models here.
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'confirm_button', 'reject_button','dept','email','age','phoneno']
    
    def confirm_button(self, obj):
        return format_html('<a class="button" href="{}">Confirm</a>', reverse('confirm_appointment', args=[obj.id]))
    confirm_button.short_description = 'Confirm'

    def reject_button(self, obj):
        return format_html('<a class="button" href="{}">Reject</a>', reverse('reject_appointment', args=[obj.id]))
    reject_button.short_description = 'Reject'

admin.site.register(Bookings_model, BookingsAdmin)
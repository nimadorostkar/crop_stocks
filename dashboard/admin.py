from .models import Profile, Notice, Payment, Submitted_files, Ticket, Money_req, Stock
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from . import models


admin.site.site_header= " Crop "
admin.site.site_title= " Crop "



class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on')
class Submitted_filesAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on')
class TicketAdmin(admin.ModelAdmin):
	list_display = ('ticket_number' ,'user_name', 'title','descriptions','created_on','status','case')
class StockAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'total_price','created_on')
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'image_tag','descriptions','created_on')
class Money_reqAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'req_number','descriptions','amount','created_on','status')
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'image_tag','national_code','phone','address')



admin.site.register(models.Notice,NoticeAdmin)
admin.site.register(models.Submitted_files,Submitted_filesAdmin)
admin.site.register(models.Ticket,TicketAdmin)
admin.site.register(models.Money_req,Money_reqAdmin)
admin.site.register(models.Stock,StockAdmin)
admin.site.register(models.Payment,PaymentAdmin)
admin.site.register(models.Profile,ProfileAdmin)

admin.site.register(LogEntry)



'''
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date',)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'amount', 'transaction_date', 'status')
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order',)


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
'''

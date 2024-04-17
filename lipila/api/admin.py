from django.contrib import admin
from .models import (BusinessUser, LipilaDisbursement)
from business.models import Product, BNPL, Student
from creators.models import CreatorUser
from LipilaInfo.models import ContactInfo, LipilaUser, Contact


class BusinessUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'bio', 'business_category',
                    'address', 'company', 'city', 'country', 'first_name', 'profile_image')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'other_name', 'school', 'address', 'grade')
class CreatorUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'bio', 'creator_category',
                    'address', 'company', 'city', 'country', 'first_name', 'profile_image')


class LipilaUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'category',
                    'address', 'company', 'city', 'country', 'first_name', 'profile_image')


class DisbursementAdmin(admin.ModelAdmin):
    list_display = ('payer', 'payee', 'payee_account', 'payment_amount', 'payment_method',
                    'description', 'transaction_id', 'payment_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'price',
                    'date_created', 'description', 'quantity')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.none()


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('street', 'location', 'phone1', 'phone2',
                    'email1', 'email2', 'hours', 'days')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'subject', 'message')


class BNPLAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'requested_by',
        'product',
        'amount',
        'status',
        'approved_by'
    )


# Register your models here.
admin.site.register(BusinessUser, BusinessUserAdmin)
admin.site.register(LipilaDisbursement, DisbursementAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BNPL, BNPLAdmin)
admin.site.register(CreatorUser, CreatorUserAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(LipilaUser, LipilaUserAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.site_header = 'Lipila Adminstration'
admin.site.site_url = '/'
admin.site.site_title = 'lipila'

# superuser: pita, password: test@123

from django.contrib import admin
from .models import Property, Picture, Owner
# Register your models here.


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'lastname','phone']
    search_fields = ('firstname', 'lastname','id')
admin.site.register(Owner, OwnerAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id','property_type', 'disposal_type', 'price','available', 'created', 'updated','owner_id']
    list_filter = ['property_type','disposal_type','price','available', 'owner_id',]
    list_editable = ['price', 'available','disposal_type']
    search_fields = ['id','owner_id']
    raw_id_fields = ('owner',)
    #search_fields = ['price','disposal_type','property_type','id','owner_id']
admin.site.register(Property, PropertyAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ['id','img_desc','property_id']
    raw_id_fields = ('property',)
admin.site.register(Picture,PictureAdmin)

from django.contrib import admin
from django.shortcuts import HttpResponseRedirect

from .models import Manufacturer, Category, Product


class ManufacturerAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'updated_date')
    list_display = ('code', 'category', 'manufacturer', 'quantity', 'price', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    change_form_template = "admin/quantity_change_form.html"

    def response_change(self, request, obj):
        if '_add-ten' in request.POST:
            obj.quantity += 10
            obj.save()
            self.message_user(request, 'Добавлено 10 единиц')
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


admin.site.site_header = 'Склад'
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
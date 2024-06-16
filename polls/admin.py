from django.contrib import admin

from polls.models import Produkt, Klient, Prodazba, Kategorija


# Register your models here.
class ProduktInlineAdmin(admin.TabularInline):
    model = Produkt
    extra = 1


class KategorijaAdmin(admin.ModelAdmin):
    inlines = [ProduktInlineAdmin]


class ProduktAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProduktAdmin, self).save_model(request, obj, form, change)




class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class KlientAdmin(admin.ModelAdmin):
    list_display = ('name', 'prezime',)


admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Klient, KlientAdmin)
admin.site.register(Prodazba)
admin.site.register(Kategorija, KategorijaAdmin)

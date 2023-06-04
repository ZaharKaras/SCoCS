from django.contrib import admin
from .models import Climate, Country, Hotel, Client, Package, Order


class HotelInline(admin.TabularInline):
    model = Hotel
    extra = 0


class PackageInline(admin.TabularInline):
    model = Package
    extra = 0


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ['package', 'order_date']


class ClimateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'star_rating', 'price_per_night']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'phone']
    inlines = [OrderInline]


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'get_hotels', 'price', 'duration']
    inlines = [OrderInline]

    def get_hotels(self, obj):
        return ', '.join(hotel.name for hotel in obj.hotels.all())

    get_hotels.short_description = 'Hotels'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'package', 'order_date']


admin.site.register(Climate, ClimateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Order, OrderAdmin)

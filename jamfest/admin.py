from django.contrib import admin
from .models import Artist, Events, Articles, Releases, Merchandise, Testimonials, Services, Type_of_Event, Talent, Genre

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    filter_horizontal = ('Type_of_Event',)
    filter_horizontal = ('Talent',)
    filter_horizontal = ('Genre',)

admin.site.register(Artist)
admin.site.register(Events)
admin.site.register(Articles)
admin.site.register(Releases)
admin.site.register(Merchandise)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Type_of_Event)
admin.site.register(Talent)
admin.site.register(Genre)

from django.contrib import admin
from .models import UpcomingEvent, ThingsHappening, Uploads, Album, Gallery, Devotion, DevotionCategory
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# Apply summernote to all TextField in model.
class ThingsHappeningAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    readonly_fields = ('create_date','update_date',)
    
class DevotionAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    readonly_fields = ('create_date','update_date',)

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)
    
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)

admin.site.register(UpcomingEvent)
admin.site.register(ThingsHappening, ThingsHappeningAdmin)
admin.site.register(Uploads)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Devotion, DevotionAdmin)
admin.site.register(DevotionCategory)
from django.contrib import admin
from .models import Home, Tags, Slider, Resume_intro, Resume_services, Resume_experience, \
    Resume_education, Resume_language_skill, Resume_coding_skill, Resume_knowledge, Resume_interests, Testimonials,\
    Client_logos, Custom_text, Portfolio, Contact_detail

# Register your models here.
admin.site.register(Home)
admin.site.register(Tags)
admin.site.register(Resume_intro)
admin.site.register(Resume_services)
admin.site.register(Resume_experience)
admin.site.register(Resume_education)
admin.site.register(Resume_language_skill)
admin.site.register(Resume_coding_skill)
admin.site.register(Resume_knowledge)
admin.site.register(Resume_interests)
admin.site.register(Testimonials)
admin.site.register(Client_logos)
admin.site.register(Custom_text)
admin.site.register(Portfolio)
admin.site.register(Contact_detail)


class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Slider, SliderAdmin)

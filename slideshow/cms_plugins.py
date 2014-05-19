from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from slideshow.models import  *

class SlideshowHome(CMSPluginBase):
    model = SlideshowHomePlugin
    name = "Home slideshow Plugin"
    render_template = "plugins/slideshow_plugin.html"
    
    def render(self, context, instance, placeholder):
        images = SlideshowHome.objects.all()
        context.update({
            'instance': instance,
            'images': images,
            'placeholder': placeholder,
        })
        return context

class SlideshowReference(CMSPluginBase):
    model = SlideshowReferencePlugin
    name = "Reference slideshow Plugin"
    render_template = "plugins/slideshow_plugin.html"
    
    def render(self, context, instance, placeholder):
        images = SlideshowReference.objects.all()
        context.update({
            'instance': instance,
            'images': images,
            'placeholder': placeholder,
        })
        return context
        
class SlideshowReport(CMSPluginBase):
    model = SlideshowReportPlugin
    name = "Report slidesho Plugin"
    render_template = "plugins/slideshow_plugin.html"
    
    def render(self, context, instance, placeholder):
        images = SlideshowReport.objects.all()
        context.update({
            'instance': instance,
            'images': images,
            'placeholder': placeholder,
        })
        return context
        
class SlideshowSearch(CMSPluginBase):
    model = SlideshowSearchPlugin
    name = "Search slideshow Plugin"
    render_template = "plugins/slideshow_plugin.html"
    
    def render(self, context, instance, placeholder):
        images = SlideshowSearch.objects.all()
        context.update({
            'instance': instance,
            'images': images,
            'placeholder': placeholder,
        })
        return context
                        
plugin_pool.register_plugin(SlideshowHome)
plugin_pool.register_plugin(SlideshowReference)
plugin_pool.register_plugin(SlideshowReport)
plugin_pool.register_plugin(SlideshowSearch)

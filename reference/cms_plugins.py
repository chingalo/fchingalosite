from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from reference.models import  *
from reference.forms import  *

class ReferencePlugin(CMSPluginBase):
	model = ReferencePlugin
	name = 'reference plugin'
	render_template = "plugins/references.html" 
	def render(self, context, instance, placeholder):
		references = Reference.objects.all()
		reference_detail = Reference_file.objects.all()
		context.update({
		'instance': instance,
		'references': references,
		'reference_detail':reference_detail,
		'placeholder': placeholder,		
		})
		return context
		
class ReferencePlugin(CMSPluginBase):
	model = ReferenceFormPlugin
	name = 'reference test plugin'
	render_template = "plugins/test.html" 
	def render(self, context, instance, placeholder):
		form = referenceForm()
		context.update({
		'instance': instance,
		#'form': form,
		'placeholder': placeholder,		
		})
		return context		

plugin_pool.register_plugin(ReferencePlugin)
plugin_pool.register_plugin(ReferenceFormPlugin)

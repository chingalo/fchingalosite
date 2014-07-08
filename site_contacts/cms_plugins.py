from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from site_contacts.models import  *

class ContactsPlugin(CMSPluginBase):
	model = ContactsPlugin
	name = "contacts Plugin"
	render_template = "plugins/contacts.html" 
	def render(self, context, instance, placeholder):
		contacts = Contacts.objects.all()
		context.update({
			'instance': instance,
			'contacts': contacts,
			'placeholder': placeholder,
		})
		return context		

class ServicesPlugin(CMSPluginBase):
	model = ServicesPlugin
	name = "services Plugin"
	render_template = "plugins/services.html" 
	def render(self, context, instance, placeholder):
		services = Contacts.objects.all()
		context.update({
			'instance': instance,
			'services': services,
			'placeholder': placeholder,
		})
		return context     

plugin_pool.register_plugin(ContactsPlugin)
plugin_pool.register_plugin(ServicesPlugin)




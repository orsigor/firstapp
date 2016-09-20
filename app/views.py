from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from .models import ContactGroup,Contact

class GroupModelView(ModelView):
	datamodel=SQLAInterface(ContactGroup)
	related_view=[ContactModelView]

class ContactModelView(ModelView):
	datamodel=SQLAInterface(Contact)
	
	label_columns={'contact_group':'Contacts Group'}
	list_columns=['name','personal_celphone','birthday','contact_group']
	show_fieldset=[
		('Summary',{'fields':['name','address','contact_group']}),
		('Personal Info',{'fields':['birthday','personal_phone','personal_celphone'],'expanded':False}),
	]



@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(ContactModelView, "List Contacts", icon="fa-envelope", category="Contacts")


from app import app, db
from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from app.models import MedicineCategory, Medicine, User, UserRoleEnum
from flask_login import current_user, logout_user
from flask import redirect


class MyAdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRoleEnum.ADMIN)


class MedicineView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list= ['name', 'unit']
    column_filters = ['name', 'price']
    column_exclude_list = ['category']
    column_labels = {
        'name' : 'Medicine Name',
        'unit': 'Unit',
        'in_stock': 'In Stock',
        'exp_date' : 'Expiry Date'
    }
    column_sortable_list = ['id', 'name', 'price']


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    
    def is_accessible(self):
        return current_user.is_authenticated


admin = Admin(app=app, name="MEDICARE - HEALTH SPECIALISTS ADMINISTRATION", template_mode='bootstrap4', index_view=MyAdminView())
admin.add_view(MedicineView(Medicine, db.session))
admin.add_view(AuthenticatedModelView(MedicineCategory, db.session))
admin.add_view(AuthenticatedModelView(User, db.session))
admin.add_view(LogoutView(name='Logout'))




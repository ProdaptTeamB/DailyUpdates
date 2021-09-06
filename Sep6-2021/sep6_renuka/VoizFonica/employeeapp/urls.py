from django.urls import path,include
from . import views

urlpatterns = [
   #VIEWS
    path('add/',views.employee_view,name='employee_view'),
    path('viewemp/',views.emp_view,name='emp_view'),
    path('updateemp/',views.upd_view,name='upd_view'),
    path('deleteemp/',views.del_view,name='del_view'),
    path('searchemp/',views.search_view,name='search_view'),

    #APIS
    path('eadd/',views.employeeaddpage,name='employeeaddpage'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('viewall/',views.employee_list,name='employee_list'),
    path('viewemployee/<empcode>',views.employee_details,name='employee_details'),
    path('updateactionapi/',views.update_data_read,name='update_data_read'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),
   
]
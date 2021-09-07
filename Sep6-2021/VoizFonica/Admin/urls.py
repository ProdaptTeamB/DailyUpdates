from . import views
from django.urls import path


urlpatterns = [
    #page
    path('',views.home,name='home'),
    path('login',views.login_page,name='login_page'),
    path('dashboard/',views.dashboard,name='dashboard_page'),


    # query
    path('query',views.homeQuery,name='home_query'),
    path('add/', views.addQuery,name='addQuery'),
    path('viewall/', views.viewQuery,name='viewQuery'),
    path('search/', views.searchapi,name='searchapi'),
    path('feedback/', views.searchFeedback,name='searchFeedback'),
    path('questions/', views.searchQuestions,name='searchQuestions'),
    path('complaints/', views.searchComplaints,name='searchComplaints'),


    path('page/',views.QueryAdd,name='QueryAdd'),
    path('viewquerypage/',views.viewQuerys,name='viewQuerys'),
    path('searchquerypage/',views.searchQuerys,name='searchQuerys'),
    path('feedbackpage/',views.Feedbacksearch,name='Feedbacksearch'),
    path('questionpage/',views.Questionssearch,name='Questionssearch'),
    path('complaintpage/',views.Complaintssearch,name='Complaintssearch'),
    path('updatepage/',views.updateToCustomer,name='updateToCustomer'),


#customer 

    path('customer/',views.homecustomer,name="home_customer"),
    path("addcustomer/",views.addcustomer,name="addcustomer"),
    path("viewallcustomer/",views.view_all,name="view_all"),
    path('viewcustomer/<fetchid>',views.viewcustomer,name='viewcustomer'),
    path('searchapi/',views.search_api,name='search_api'),

    path('updatedata/',views.update_data,name='update_data'),
    path('updateapi/',views.update_api,name='update_api'),

    path('deleteapi/',views.delete_api,name='delete_api'),
    path('deletedata/',views.delete_data,name='delete_data'),

    path('viewconnection/',views.view_connection,name='view_connection'),
    path('viewapi/',views.view_api,name='view_api'),

    path('viewtoday/',views.view_today,name='view_today'),   
    path('viewtodayapi/',views.view_todayapi,name='view_todayapi'),

    path('viewproduct/',views.product,name='product'),   
    path('viewproductapi/',views.product_api,name='product_api'),
    
    path('add_customer/',views.add_c,name='add_c'),
    path('header_customer/',views.header,name='header'),
    path('view_customer/',views.viewall,name='viewall'),
    path('search_customer/',views.search,name='search'),
    path('update_customer/',views.update,name='update'),
    path('delete_customer/',views.delete,name='delete'),








#employee
    path('employee',views.employeehome,name='employee_home'),
    path('addemploye/',views.add_employe,name='add_employe'),
    path('viewemploye/',views.view_employe,name='view_employe'),
    path('updateemploye/',views.upd_view,name='upd_view'),
    path('deleteemploye/',views.del_view,name='del_view'),
    path('searchemploye/',views.search_view,name='search_view'),

    #APIS
    path('eadd/',views.employeeaddpage,name='employeeaddpage'),
    path('search/',views.searchapi,name='searchapi'),
    path('viewall/',views.employee_list,name='employee_list'),
    path('viewemployee/<fetchid>',views.employee_details,name='employee_details'),
    
    path('updateactionapi/',views.update_data_read,name='update_data_read'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),

    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),








#billing 



]
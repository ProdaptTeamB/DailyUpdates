from django.urls import path,include
from . import views
urlpatterns = [    
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



]
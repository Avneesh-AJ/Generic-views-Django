import imp
from django.urls import path
from main import views

urlpatterns=[
    path('',views.Index.as_view(),name="index"),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name="college"),
    path('colleges/',views.CollegeList.as_view()),
    path('add_college/',views.CollegeCreate.as_view()),
    path('update_college/<int:pk>',views.CollegeUpdate.as_view()),
    path('add_student/',views.StudentCreate.as_view()),
    path('update_student/<int:pk>',views.StudentUpdate.as_view()),
    path('delete_student/<int:pk>',views.StudentDelete.as_view())
]
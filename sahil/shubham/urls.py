from shubham import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

# urlpatterns=[
    
#     path('',views.shubham_List.as_view(),name='shubham_list'),
#     path('shubham/<pk>/',views.shubham_details.as_view(),name='shubham_details'),    
# ]

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
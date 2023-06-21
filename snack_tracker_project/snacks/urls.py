from django.urls import path
from .views import * 


urlpatterns=[
    # path('', Home.as_view() , name='home'),
    path('',SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailView.as_view() , name='snack_detail')

]
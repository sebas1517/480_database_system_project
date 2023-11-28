from django.urls import path
from . import views
from .views import NurseUpdateView, NurseHomeView

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('schedule/', views.schedule_vaccination, name='schedule'),
    path('record/<str:pk>', views.user_record, name='record'),
    path('schedule_confirm/<str:pk>', views.schedule_confirm, name='schedule_confirm'),
    path('add_schedule/<str:pk>', views.add_schedule, name='add_schedule'),
    path('nurse_home/', NurseHomeView.as_view(), name='nurse_home'),
    path('update_nurse_info/<str:nurse_id)/', NurseUpdateView.as_view(), name='update_nurse_info')
    
]

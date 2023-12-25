from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('user_reg',views.user_reg,name="user_reg"),
    path('user_test',views.user_test,name='user_test'),
    path('user_login',views.user_login,name='user_login'),
    path('user_check',views.user_check,name="user_check"),
    path('admin_login',views.admin_login,name='admin_login'),
    path('ground_booking',views.ground_booking,name='ground_booking'),
    path('data_ground_booking',views.data_ground_booking,name='data_ground_booking'),
    path("admin_login_page",views.admin_login_page,name="admin_login_page"),
    path('admin_check',views.admin_check,name="admin_check"),
    path('admin_booking',views.admin_booking,name="admin_booking"),
    path('admin_event',views.admin_event,name="admin_event"),
    path('add_event',views.add_event,name='add_event'),
    path('db_add_event',views.db_add_event,name='db_add_event'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('show_event',views.show_event,name='show_event'),
    path('userhome',views.userhome,name='userhome'),
    path('event_delete',views.event_delete,name='event_delete'),
    path('mail_send',views.mail_send,name='mail_send'),
    path('email_check',views.email_check,name='email_check'),
    path('otp_check',views.otp_check,name='otp_check'),
    path('update_pass',views.update_pass,name='update_pass')
    ]
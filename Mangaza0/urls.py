from django.contrib import admin
from django.urls import path
import home.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property, name='property'),
    # path('vacational/', views.vacational, name='vacation'),
    path('vacation/', views.homepage, name="vacation"),
    path('home', views.homepage, name="homepage"),
    path('about', views.aboutpage, name="aboutpage"),
    path('contact', views.contactpage, name="contactpage"),
    path('user', views.user_log_sign_page, name="userloginpage"),
    path('user/login', views.user_log_sign_page, name="userloginpage"),
    path('user/bookings', views.user_bookings, name="dashboard"),
    path('user/book-room', views.book_room_page, name="bookroompage"),
    path('user/book-room/book', views.book_room, name="bookroom"),
    path('user/signup', views.user_sign_up, name="usersignup"),
    path('staff/', views.staff_log_sign_page, name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page, name="staffloginpage"),
    path('staff/signup', views.staff_sign_up, name="staffsignup"),
    path('logout', views.logoutuser, name="logout"),
    path('staff/panel', views.panel, name="staffpanel"),
    path('staff/allbookings', views.all_bookings, name="allbookigs"),

    path('staff/panel/add-new-location', views.add_new_location, name="addnewlocation"),
    path('staff/panel/edit-room', views.edit_room),
    path('staff/panel/add-new-room', views.add_new_room, name="addroom"),
    path('staff/panel/edit-room/edit', views.edit_room),
    path('staff/panel/view-room', views.view_room),

    path('admin/', admin.site.urls),

]

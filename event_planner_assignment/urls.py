from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('', views.home_page),  # الصفحة الرئيسية
    path('about/', views.about_page),  # About
    path('events/create/', views.create_event),  # create
    path('events/', views.event_list_page),  # عرض HTML
    path('events/json/', views.get_all_events),  # عرض JSON
    path('events/<uuid:event_id>/', views.event_detail),  # تفاصيل HTML
    path('events/<uuid:event_id>/json/', views.get_event),  # تفاصيل JSON
    path('events/<uuid:event_id>/update/', views.update_event),  # update
    path('events/<uuid:event_id>/delete/', views.delete_event),  # delete
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
]
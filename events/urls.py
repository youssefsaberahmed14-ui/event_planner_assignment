from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('', views.home_page),  # الصفحة الرئيسية
    path('about/', views.about_page),  # صفحة About
    path('events/create/', views.create_event),  # إنشاء حدث
    path('events/', views.event_list_page),  # عرض كل الأحداث HTML
    path('events/json/', views.get_all_events),  # عرض كل الأحداث JSON
    path('events/<uuid:event_id>/', views.event_detail),  # تفاصيل حدث HTML
    path('events/<uuid:event_id>/json/', views.get_event),  # تفاصيل حدث JSON
    path('events/<uuid:event_id>/update/', views.update_event),  # تعديل حدث
    path('events/<uuid:event_id>/delete/', views.delete_event),  # حذف حدث
    path('admin/', admin.site.urls),  # لوحة تحكم Admin
]
from django.urls import path
from .views import EventList

urlpatterns = [
    path('events/', EventList.as_view()),
]
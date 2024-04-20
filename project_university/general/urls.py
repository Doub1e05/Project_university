from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    re_path(r'^work-check/$', views.Teacher.work_check, name="teacher-work-check"),
    re_path(r'^work-list/$', views.Teacher.work_list, name="teacher-work-list"),
    re_path(r'^about-teacher/$', views.Teacher.about, name="teacher-about"),

    re_path(r'^get-id/$', views.Students.get_id, name="students-get-id"),
    re_path(r'^notification/$', views.Students.notification, name="students-notification"),
    re_path(r'^progress/$', views.Students.progress, name="students-progress"),
    re_path(r'^about-student/$', views.Students.about, name="students-about"),

    path('api/labs', views.lab_list),
    path('api/labs/<int:pk>/', views.lab_detail),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
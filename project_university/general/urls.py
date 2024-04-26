from django.urls import path
from .views import StatusAPIView, StatusAPIViewAction

urlpatterns = [
    path('work-statuses/', StatusAPIView.as_view(), name='work-statuses'),
    path('work-statuses/<int:id>/', StatusAPIViewAction.as_view(), name='work-statuses-action')
]
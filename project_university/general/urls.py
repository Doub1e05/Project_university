from django.urls import path

from .views import StatusAPIView, StatusAPIViewAction, UserLogin,\
        UserLogout, UserView, ThreadView, WorksView, SubjectsView,\
        ThreadAPIViewAction, WorksAPIViewAction, SubjectsAPIViewAction
        

urlpatterns = [
    path('work-statuses/', StatusAPIView.as_view(), name='work-statuses'),
    path('work-statuses/<int:id>/', StatusAPIViewAction.as_view(), name='work-statuses-action'),

	path('login', UserLogin.as_view(), name='login'),
	path('logout', UserLogout.as_view(), name='logout'),
	path('profile', UserView.as_view(), name='profile'),

    path('threads', ThreadView.as_view(), name='threads'),
    path('threads/<int:id>/', ThreadAPIViewAction.as_view(), name='thread'),

    path('works', WorksView.as_view(), name='works'),
    path('works/<int:id>/', WorksAPIViewAction.as_view(), name='work'),

    path('subjects', SubjectsView.as_view(), name='subjects'),
    path('subjects/<int:id>/', SubjectsAPIViewAction.as_view(), name='subject'),
]
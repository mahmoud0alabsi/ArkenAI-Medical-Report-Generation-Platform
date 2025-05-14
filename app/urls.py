from django.urls import path
from .views.home.Home import *
from .views.dashboard.Dashboard import *
from .views.dashboard.History import *
from .views.dashboard.Profile import *

from .views.auth.Auth import *

app_name = 'app'

urlpatterns = [
    path('', HomePage, name='home'),

    path('book-demo/trial/auth/login/', LoginPage, name='login'),
    path('book-demo/trial/auth/logout/', LogoutPage, name='logout'),

    path('dashboard/', DashboardPage, name='dashboard'),
    path('dashboard/history/', HistoryPage, name='history'),
    path('dashboard/profile/', ProfilePage, name='profile'),
]
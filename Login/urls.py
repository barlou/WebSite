from django.urls import URLPattern, path
from Login.views import (
    register_view, 
    login_view,
    logout_view, 
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView
)

app_name = 'Login'

urlpatterns = [
    path('', login_view, name="login-login"),
    path('logout', logout_view, name="login-logout"),
    path('subscribe', register_view, name="login-subscribe"),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete')

]

from django.urls import path
from your_app.views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
]

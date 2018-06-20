from django.urls import path

from .views import LeaveRequest, Completed, Clockin, Clock, Clockout, PastAttendance #LeaveTable

app_name = 'attendance'
urlpatterns = [
    path('leave/', LeaveRequest.as_view(), name='leave_request'),
    path('completed/', Completed.as_view(), name='task_completed'),
    #path('clock/', Clock.as_view(), name='clock'),
    path('clock/in/', Clockin.as_view(), name='clockin'),
    path('clock/out/', Clockout.as_view(), name='clockout'),
<<<<<<< HEAD
    path('userattendance/', PastAttendance.as_view(), name='pastattendance' )
]

=======
    path('userattendance/', PastAttendance.as_view(), name='pastattendance' ),
    #path('leaverequest/', LeaveTable.as_view(), name = 'leave_request')
]
>>>>>>> 0a4ad975e1662f23018696dc59e6087a87db3a76

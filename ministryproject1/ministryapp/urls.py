
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('register/',views.RegisterModelView.as_view(),name='register'),
    path('login/',views.LoginModelView.as_view(),name='login'),
    path('profile/',views.ProfileModelView.as_view(),name='profile'),
    path('changepassword/',views.PasswordChangeView.as_view(),name='changepassword'),
    path('send-mail-reset-password/',views.SendMailPasswordResetView.as_view(),name='send-mail-reset-password'),
    path('password-reset/<uid>/<token>/',views.DoPasswordResetView.as_view(),name='password-reset/'),
    path('graphview/',views.graph_view,name='graphview'),
    path('pieview/',views.pie_chart_view,name='pieview'),
    path('graphform/',views.graphform,name='graphform'),
    path('pieform/',views.pieform,name='pieform'),
    path('pie-chart/', views.generate_pie_chart, name='pie-chart'),
    path('line-chart/', views.generate_line_chart, name='line_chart'),
    path('generate-matrix/', views.generate_matrix_chart, name='generate_matrix'),
    path('matrixform/',views.matrixform,name='matrixform'),
    path('animation/', views.my_animation_view, name='my-animation'),
    path('sine/', views.animation_view, name='sine'),
    path('api/generate-angle-visualization/', views.generate_angle_visualization_api, name='generate_angle_visualization_api'),
    # path('guess_number/', views.guess_number, name='guess_number'),
    path('courses/', views.course_detail, name='course-list'),
    path('courses/<int:classnumber>/', views.course_detail, name='course-detail'),
    path('videos/<int:classnumber>/', views.course_detail, name='course-detail'),
    path('save-time/', views.save_time, name='save_time'),
    
    
]

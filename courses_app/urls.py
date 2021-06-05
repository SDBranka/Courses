from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('courses/destroy/<int:course_id>', views.destroy_check),
    path('process_destroy/<int:course_id>', views.process_destroy),
    path('courses/comment/<int:course_id>', views.comment),
    path('add_comment/<int:course_id>', views.add_comment),
]
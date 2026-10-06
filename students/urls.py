from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.student_list,
        name='student-list'
    ),

    path(
        'students/create/',
        views.student_create,
        name='student-create'
    ),

    path(
        'students/<int:student_id>/update/',
        views.student_update,
        name='student-update'
    ),

    path(
        'students/<int:student_id>/delete/',
        views.student_delete,
        name='student-delete'
    ),

]
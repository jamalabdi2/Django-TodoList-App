from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('add/',views.addTodoList,name = 'add_todolist'),
    path('edit/<int:pk>/',views.editTodoList,name = 'edit_todolist'),
    path('delete/<int:pk>/',views.deleteTodoList,name = 'delete_todolist'),
    # path('success/',views.success,name = 'success')
]
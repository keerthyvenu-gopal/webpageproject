from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:post_id>', views.post_view, name='post_view'),
    path('add/',views.add_post,name='add_post'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]
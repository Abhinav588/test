from . import views
from django.urls import path

urlpatterns = [
    path('',views.showpage,name='showpage'),
    path('add_student',views.add_student,name='add_student'),
    path('showsaved',views.showsaved,name='showsaved'),

    path('editpage/<int:od>',views.editpage,name='editpage'),
    path('delete/<int:od>',views.delete,name='delete'),
    path('editing/<int:od>',views.editing,name='editing'),
]

# path('editpage/<int:pk>',views.editpage,name='editpage'),
#     path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
#     path('edit_product_details/<int:pk>',views.edit_product_details,name='edit_product_details'),
#     path('delete_product/<int:pk>',views.delete_product,name='delete_product')
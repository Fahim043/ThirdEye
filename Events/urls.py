from . import views
from django.urls import path

app_name='Events'
urlpatterns = [
    path('', views.EventsClassView.as_view(), name='Events'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('Itemm/', views.Itemm, name='Itemm'),
    # add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    # update item
    path('update/<int:id>', views.update_item, name='update_item'),
]
 
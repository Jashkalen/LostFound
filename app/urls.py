from django.urls import path
from .views import HomePageView, AboutPageView, ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('item/', ItemListView.as_view(), name='item'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item_detail'),
    path('item/create', ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/edit',  ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='item_delete'),

]
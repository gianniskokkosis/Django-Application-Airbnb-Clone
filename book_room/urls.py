from django.urls import path
from . import views
from users import views as user_views
from .views import (
    RoomListView, 
    RoomDetailView, 
    ReviewCreateView, 
    PurchaseCreateView,
    ReviewListView,
    ReviewUserList,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView, 
    UserPurchasesListView
)


urlpatterns = [
    path('', RoomListView.as_view(), name='home-page'),
    path('about/', views.about, name='about-page'),
    path('detail/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('new_review/<int:pk>/', ReviewCreateView.as_view(), name='new-review'),
    path('purchase/<int:pk>/', PurchaseCreateView.as_view(), name='new-purchase'),
    path('all_reviews/<int:pk>/', ReviewListView.as_view(), name='all-reviews'),
    path('user_purchases/', UserPurchasesListView.as_view(), name='user-puchases'),
    path('user_reviews/', ReviewUserList.as_view(), name='user-reviews'),
    path('detail_review/<int:pk>/', ReviewDetailView.as_view(), name='detail-review'),
    path('detail_review/<int:pk>/update', ReviewUpdateView.as_view(), name='update'),
    path('detail_review/<int:pk>/delete', ReviewDeleteView.as_view(), name='delete'),
]

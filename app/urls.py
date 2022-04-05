from django.urls import path
from .views import *

urlpatterns = [
    path('about',AllProducts.as_view()),
    path('allmenu',AllCategory.as_view()),
    path('about/<int:pk>',AboutCategoryProduct.as_view()),
    path('payment',Test.as_view()),
    path('send/<str:xabar>',SendTelegramBot),
    path('order/<str:user>/<int:id>/<int:quantity>',order)
   
    
]
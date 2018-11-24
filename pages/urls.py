from django.urls import path
from . import views
from pages.views import MenuList,MList,SList

urlpatterns = [
   path('order/',MList.as_view(),name='order'),
   path('',MenuList.as_view(),name='home'),
    path('adminp/student/',SList.as_view(),name='student'),
   path('about/',views.about,name='about'),
   #path('order/',views.order,name='order'),
   path('profile/',views.profile,name='profile'),
   path('ordernow/',views.placeorder,name='placeorder'),
   # path('login/',views.login,name='login'),
   path('adminp/',views.adminp,name='adminp'),
   path('adminp/vo/',views.vo,name='vo'),
]
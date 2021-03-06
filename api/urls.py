from django.urls import path, include
from .views import *
from api import views

urlpatterns = [
  path("userclient/", UserClientList.as_view()),
  path("userhost/", UserHostList.as_view()),
  path("userclient/<int:id>/", UserClientDetail.as_view()),
  path("userhost/<int:id>/", UserHostDetail.as_view()),
  path("haircategory/", HairCategoryList.as_view()),
  path("haircategory/<int:id>/", HairCategoryDetail.as_view()),
  path("hairs/", HairList.as_view()),
  path("haircategory/<int:id>/hairs/", UniqueCategoryHairDetail.as_view()),
]
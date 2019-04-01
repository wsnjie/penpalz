from django.conf.urls import include
from django.urls import path
from .views import UserView, LangView, ProfView, MessageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("User", UserView)
router.register("Lang", LangView)
router.register("Prof", ProfView)
router.register("Message", MessageView)


urlpatterns = [path("", include(router.urls))]


from django.urls import path,include
from rest_framework import routers
from.views import studentViewsets

router=routers.DefaultRouter()
router.register('student',studentViewsets)


urlpatterns = [
    path('', include(router.urls)),

]

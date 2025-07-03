from rest_framework import routers
from .views import TripPlanView

router = routers.DefaultRouter()

router.register(r'trip-plans', TripPlanView)

urlpatterns = router.urls

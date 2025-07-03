from rest_framework import routers
from .views import CurrencyView

router = routers.DefaultRouter()

router.register(r'countries', CurrencyView)

urlpatterns = router.urls

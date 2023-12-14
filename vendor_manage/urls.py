from rest_framework_nested import routers
from .views import *


router = routers.DefaultRouter()
router.register('vendors',VendorModelViewSet,basename='vendors')
router.register('purchase_orders',PurchaseModelViewSet,basename='purchase_orders')

vendor_router = routers.NestedDefaultRouter(router,'vendors',lookup='vendors')
vendor_router.register('performance',HistoricalPerformanceModelViewSet,basename='performance')

purchase_router = routers.NestedDefaultRouter(router,'purchase_orders',lookup='purchase_orders')
purchase_router.register('acknowledge',AcknowledgeViewSet,basename='acknowledge')

urlpatterns = router.urls + vendor_router.urls + purchase_router.urls


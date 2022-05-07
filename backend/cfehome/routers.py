from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewsSet

router = DefaultRouter()
router.register('products-abc', ProductViewsSet, basename='products')
print(router.urls)
urlpattern = router.urls

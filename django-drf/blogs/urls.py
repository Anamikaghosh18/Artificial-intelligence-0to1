from .views import BlogViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blogs", BlogViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls
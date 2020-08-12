from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VendorViewSet,
    LocationViewSet,
    FavoritesViewSet,
    VendorDetailViewSet,
    CategoryViewSet,
    FaqViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    MyScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("schedule", ScheduleViewSet)
router.register("faq", FaqViewSet)
router.register("favorites", FavoritesViewSet)
router.register("vendor", VendorViewSet)
router.register("presenter", PresenterViewSet)
router.register("category", CategoryViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("location", LocationViewSet)
router.register("sponsor", SponsorViewSet)
router.register("vendordetail", VendorDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include # Ensure 'include' is imported
from . import views
from rest_framework.routers import DefaultRouter # New: Import DefaultRouter for API URLs

# Create a router for your API ViewSets
router = DefaultRouter()
# Register your ViewSets with the router. This will automatically generate URL patterns like:
# /api/bookings/ (GET, POST)
# /api/bookings/{id}/ (GET, PUT, PATCH, DELETE)
router.register(r'bookings', views.BookingViewSet)
# Register the MenuViewSet as well
router.register(r'menu-items', views.MenuViewSet)


urlpatterns = [
    # --- Existing Traditional Django View URLs ---
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),

    # --- New API URLs ---
    # Include all URLs registered with the router under the 'api/' prefix
    path('api/', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views  # Import the DRF token authentication views

# Define the main URL patterns
# project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet  # Import your TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API routes go under /api/
]

# Include the URL for obtaining an authentication token (this is for token-based authentication)
urlpatterns += [
    # This is where the client can obtain an authentication token (useful for subsequent requests)
    path('api-token-auth/', views.obtain_auth_token),
]

# If the project is in DEBUG mode, include Django Debug Toolbar URLs for debugging
if settings.DEBUG:
    import debug_toolbar
    # Add the debug toolbar's URLs to the main urlpatterns for easy access during development
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from todoApp import views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'due_task', views.DueTaskViewSet)
# router.register(r'completed_task', views.CompletedTaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^register/$', views.CreateUserView.as_view(), name='user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

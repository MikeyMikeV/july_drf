from rest_framework import routers
from movies import views as movies_viewsets
from accounts import views as user_viewsets

router = routers.DefaultRouter()
router.register('movie',movies_viewsets.MovieViewSet)
router.register('user', user_viewsets.UserViewSet)
router.register('movie/create/first-step', movies_viewsets.MovieFirstStepViewSet, basename='first_step')
router.register('movie/create/second-step', movies_viewsets.MovieSecondStepViewSet, basename='second_step')
router.register('movie/create/third-step', movies_viewsets.MovieThirdStepViewSet, basename='third_step')
urlpatterns = router.urls
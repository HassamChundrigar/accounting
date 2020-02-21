from django.urls import path
from .views import index, dashboard

from django.conf.urls import include
from rest_framework import routers
from .views import EntryViewSet, EntryListViewset, SubEntryViewSet, SubHeadViewSet, SubHeadAccountViewSet


router = routers.DefaultRouter()
router.register('entry', EntryViewSet)
router.register('entrylist', EntryListViewset)
router.register('subentry', SubEntryViewSet)
router.register('subhead', SubHeadViewSet)
router.register('subheadaccount', SubHeadAccountViewSet)



from .views import SubHeadList, SubHeadAccountList
urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('get_subhead', SubHeadList.as_view()),
    path('get_subhead_account', SubHeadAccountList.as_view()),
    path('api/', include(router.urls))
]

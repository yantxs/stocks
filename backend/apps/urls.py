from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, GroupViewSet
# from heroes.views import HeroViewSet, AbilityViewSet
from stocks.views import CompanyViewSet, CompanyCompactViewSet

from django.conf.urls import url
# hero_list = HeroViewSet.as_view({'get':'list'})
# hero_detail = HeroViewSet.as_view({'get':'retrieve'})
# ability_detail = AbilityViewSet.as_view({'get':'retrieve'})
# ability_list = AbilityViewSet.as_view({'get':'list'})
company_detail = CompanyViewSet.as_view({'get':'retrieve'})
companycompact_detail = CompanyCompactViewSet.as_view({'get':'retrieve'})


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

 # register the url link in /api so it can be clicked on (commenting this out doesnt invalidate /api/heroes)
# router.register(r'heroes', HeroViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'companies/compact', CompanyCompactViewSet)

urlpatterns= [
    # # url(r'^heroes/$', hero_list, name='hero-list'),
    # url(r'^heroes/(?P<hero_id>\d+)/$', hero_detail, name='hero-detail'), # overwrite the standard HeroViewSet urls by primary keys
    # # url(r'^api-auth/', include('rest_framework.urls',namespace = 'rest_framework'))
    # url(r'^heroes/(?P<heroid>\d+)/abilities/(?P<ability_name>[-\w\d]+)/$', ability_detail, name='ability-detail'),
    # url(r'^heroes/(?P<heroid>\d+)/abilities/$', ability_list, name='ability-list')
    url(r'^companies/(?P<ticker>\d+)/$', company_detail, name='company-detail'), # overwrite the standard CompanyViewSet urls by tickers
    url(r'^companies/compact/(?P<ticker>\d+)/$', companycompact_detail, name='company-detail') # overwrite the standard CompanyViewSet urls by tickers
]
urlpatterns += router.urls

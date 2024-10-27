from django.urls import path
from .views import common_views

app_name = "common"

urlpatterns = [
    path('', common_views.index, name="index"),
    path('home/', common_views.home, name='home'),
    #path('matching/', common_views.matching, name='matching'),
    #path('matching2/', common_views.matching2, name='matching2'),
    #path('matching3/', common_views.matching3, name='matching3'),
    #path('error/', common_views.error, name='error'),
    path('result/', common_views.find_and_render_match, name='result'),
    path('menu/', common_views.menu, name='menu'),
    path('meeting/', common_views.meeting, name='meeting'),
    path('meeting2/', common_views.meeting2, name='meeting2'),
    path('good/', common_views.good, name='good'),
    #path('fail/', common_views.fail, name='fail'),
    path('go/', common_views.go, name='go'),
    #path('use/', common_views.use, name='use'),
    path('my/<id>/',common_views.my,name='my'),
    path('you/', common_views.you, name='you'),
    path('choose/', common_views.choose, name='choose'),
    path('kakaologin/', common_views.kakaologin, name='kakaologin'),
    path('myinfo/',common_views.myinfo,name='myinfo'),
    path('success/',common_views.success,name='success'),
    path('youinfo/',common_views.youinfo,name='youinfo'),
    path('kakaoid/',common_views.kakaoid,name='kakaoid'),
    path('kakaoLoginLogic/', common_views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', common_views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', common_views.kakaoLogout),
]
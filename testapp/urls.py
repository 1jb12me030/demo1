from django.urls import path




from testapp import views
urlpatterns = [
    path('game-categories/',
        views.GameCategoryList.as_view(),
        name=views.GameCategoryList.name),
    path('game-categories/',
        views.GameCategoryDetail.as_view(),
        name=views.GameCategoryDetail.name),
    path('games/',
        views.GameList.as_view(),
        name=views.GameList.name),
    path('games/',
        views.GameDetail.as_view(),
        name=views.GameDetail.name),
    path('players/',
        views.PlayerList.as_view(),
        name=views.PlayerList.name),
    path('players/',
        views.PlayerDetail.as_view(),
        name=views.PlayerDetail.name),
    path('player-scores/',
        views.PlayerScoreList.as_view(),
        name=views.PlayerScoreList.name),
    path('player-scores/',
        views.PlayerScoreDetail.as_view(),
        name=views.PlayerScoreDetail.name),
    path('test/',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
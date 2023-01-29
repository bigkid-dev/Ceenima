from django.urls import path
from .views import ModelCreateView
from .views import ShowsListView, show_list, all_shows, NewShowsListView, Upcoming_Movies_View, navbar_view, thanks, page_not_found
from .views import footer_view, Cenima_Show_view, New_Movies_View, payments, login_page, signup, signin, logout_page, prelogin, homepage


urlpatterns = [
    path('', homepage, name="homepage"),
    path("Content", ModelCreateView.as_view() ),
    path("List", ShowsListView.as_view() ),
    path("Lists", NewShowsListView ),
    path("create", show_list),
    # path("shows", new_shows),
    path("test", all_shows, name="test"),
    path("upload", Upcoming_Movies_View.as_view() ),
    path('nav', navbar_view),
    path('footer', footer_view),
    path('show',  Cenima_Show_view.as_view()),
    path('push',  New_Movies_View.as_view()),
    path('pay', payments, name='pay'),
    path('auth/login', login_page, name="login_view"),
    path('auth/signup', signup, name="signup_view"),
    path('signin', signin, name="signin_view"),
    path('logout', logout_page, name="signin_view"),
    path('prelogin', prelogin, name="prelogin_view"),
    path('thanks', thanks, name="thanks"),


]

handler404 = "cenima.views.page_not_found"


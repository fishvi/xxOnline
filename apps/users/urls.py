from django.conf.urls import url

from apps.users.views import UserInfoView, UploadImageView, ChangePwdView, ChangeMobileView, MyCoursesView, \
    MyFavOrgsView, MyFavTeachersView, MyFavCoursesView, MyMessagesView


urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="info"),
    url(r'^image/upload/$', UploadImageView.as_view(), name="image"),
    url(r'^update/pwd/$', ChangePwdView.as_view(), name="update_pwd"),
    url(r'^update/mobile/$', ChangeMobileView.as_view(), name="update_mobile"),
    url(r'^mycourses/$', MyCoursesView.as_view(), name="mycourses"),
    url(r'^myfav_orgs/$', MyFavOrgsView.as_view(), name="myfav_orgs"),
    url(r'^myfav_teachers/$', MyFavTeachersView.as_view(), name="myfav_teachers"),
    url(r'^myfav_courses/$', MyFavCoursesView.as_view(), name="myfav_courses"),
    url(r'^messages/$', MyMessagesView.as_view(), name="messages"),
]

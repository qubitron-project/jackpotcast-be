from django.urls import path, include
from django.contrib import admin
from movies.views import movie_upload_from_csv, channel_upload_from_csv, episode_upload_from_csv, ChannelView, ChannelDetailView, BannerView, NoticeView
import debug_toolbar

urlpatterns = [
    path('users', include('users.urls')),
    path("movies", include("movies.urls")),
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('banners', BannerView.as_view()),
    path('notices', NoticeView.as_view()),
    path('channels', ChannelView.as_view()),
    path('channels/<int:channel_id>', ChannelDetailView.as_view()),
    path('movie_upload', movie_upload_from_csv, name='movie_upload'),
    path('channel_upload', channel_upload_from_csv, name='channel_upload'),
    path('episode_upload', episode_upload_from_csv, name='episode_upload'),
]
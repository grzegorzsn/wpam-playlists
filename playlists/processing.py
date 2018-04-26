from celery import shared_task
from pytube import Playlist as YTPlaylist, YouTube

from playlists.models import Playlist
from videos.models import Video
from videos.processing import parse


@shared_task
def process_playlist(yt_id):
    playlist = Playlist.objects.get(yt_id=yt_id)
    yt_playlist = YTPlaylist(playlist.get_url())
    yt_playlist.populate_video_urls()
    for url in yt_playlist.video_urls:
        yt_video = YouTube(url)
        video, is_new = Video.objects.get_or_create(yt_id=yt_video.video_id)
        playlist.videos.add(video)
        if is_new:
            parse.delay(video.id)
    playlist.save()

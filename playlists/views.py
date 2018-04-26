from django.http import JsonResponse
from playlists.models import Playlist
from playlists.processing import process_playlist


def index(request):
    return JsonResponse(list(Playlist.objects.values()), safe=False)


def playlist_view(request, yt_id):
    playlist, _ = Playlist.objects.get_or_create(yt_id=yt_id)
    process_playlist.delay(playlist.yt_id)
    return JsonResponse(list(playlist.videos.all().values()), safe=False)


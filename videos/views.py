from django.http import JsonResponse

from videos.models import Video
from videos.processing import parse


def index(request):
    return JsonResponse(list(Video.objects.values()), safe=False)


def video_view(request, yt_id):
    video, is_new = Video.objects.get_or_create(yt_id=yt_id)
    if is_new:
        parse.delay(video.id)
    video = Video.objects.filter(id=video.id).values().first()
    return JsonResponse(video, safe=False)

from pydub import AudioSegment
from celery import shared_task
from pytube import YouTube
from videos.models import Video
from wpam.settings import MEDIA_ROOT

wpam_task = shared_task(autoretry_for=(Exception,), default_retry_delay=60)


@wpam_task
def parse(id):
    video = Video.objects.get(id=id)
    yt = YouTube(video.get_url())
    video.title = yt.title
    video.parsed = True
    video.save()
    download.delay(video.id)


@wpam_task
def download(id):
    video = Video.objects.get(id=id)
    stream = YouTube(video.get_url()).streams.first()
    stream.filename = video.yt_id
    stream.download(filename=stream.filename, output_path=MEDIA_ROOT)
    video.downloaded = True
    video.save()
    convert.delay(video.id)


@wpam_task
def convert(id):
    video = Video.objects.get(id=id)
    mp3 = "{}/{}.mp3".format(MEDIA_ROOT, video.yt_id)
    mp4 = "{}/{}.mp4".format(MEDIA_ROOT, video.yt_id)
    AudioSegment.from_file(mp4).export(mp3, format="mp3")
    video.converted = True
    video.save()

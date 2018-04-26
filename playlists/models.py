from django.db import models

from videos.models import Video


class Playlist(models.Model):
    yt_id = models.CharField(max_length=200)
    name = models.CharField(max_length=300, default=None, null=True)
    creator_username = models.CharField(max_length=200)
    videos = models.ManyToManyField(Video)

    def get_url(self):
        return "https://www.youtube.com/playlist?list={}".format(self.yt_id)


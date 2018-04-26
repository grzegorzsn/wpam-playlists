from django.db import models


class Video(models.Model):
    yt_id = models.CharField(max_length=200)
    title = models.CharField(max_length=300, default=None, null=True)
    parsed = models.BooleanField(default=False)
    downloaded = models.BooleanField(default=False)
    converted = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)

    def get_url(self):
        return "https://youtube.com/watch?v={}".format(self.yt_id)


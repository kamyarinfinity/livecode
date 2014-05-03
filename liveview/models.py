from django.db import models
from solo.models import SingletonModel

class LiveCode(SingletonModel):
	raw_css = models.TextField(default="")
	raw_js = models.TextField(default="")
	raw_html = models.TextField(default="")

from django.db import models

from helpers.models import BaseModel
from users.models import User

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image=models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.title)    # post 제목 형식



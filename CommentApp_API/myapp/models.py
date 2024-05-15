from django.db import models

class Post(models.Model):
    post_id = models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.body}"

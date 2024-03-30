from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.full_name

class Chairman(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()

    def __str__(self):
        return self.name

class Member(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NoticeView(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    viewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice

class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.member

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()
    purpose = models.TextField()
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Watchmen(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()

    def __str__(self):
        return self.name

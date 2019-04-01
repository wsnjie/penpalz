from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Prof(models.Model):
    user = models.ForeignKey(
        User, related_name="prof_of_user", on_delete=models.CASCADE
    )
    language = models.ForeignKey(
        "Lang", related_name="prof_of_lang", on_delete=models.CASCADE
    )
    level = models.IntegerField()


class Lang(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    sent = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    rec = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    language = models.ForeignKey(
        Lang, related_name="in_language", on_delete=models.DO_NOTHING
    )
    content = models.TextField()

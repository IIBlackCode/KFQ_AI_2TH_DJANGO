from django.db import models
class SecondManager(models.Manager):
    def get_queryset(self):
        return super(SecondManager, self).get_queryset().filter(name__contains='kim')

class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    second_objects = SecondManager()
    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()

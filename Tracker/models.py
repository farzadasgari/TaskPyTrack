from django.db import models


class Task(models.Model):
    class Meta:
        verbose_name_plural = 'Tasks'

    PRIORITY_CHOICES = (
        (1, 'Emergency'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low'),
    )

    Task = models.CharField(max_length=255, blank=True)
    Slug = models.CharField(max_length=255, blank=True)
    Description = models.TextField(blank=True)
    Init_Date = models.CharField(max_length=10, blank=True)
    Deadline_Date = models.CharField(max_length=10, blank=True)
    Priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, blank=True, null=True)
    Is_Complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk) + '-' + self.Task


def create_with_pk(instance, filename):
    return f'Track/{instance.Checklist.pk}/{filename}'


class Track(models.Model):
    class Meta:
        verbose_name_plural = 'Tracks'

    Checklist = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True)
    File = models.FileField(upload_to=create_with_pk, blank=True)
    Complete_Date = models.CharField(max_length=10, blank=True)
    Note = models.TextField(blank=True)

    def __str__(self):
        return str(self.Checklist.pk) + '-' + self.Checklist.Task

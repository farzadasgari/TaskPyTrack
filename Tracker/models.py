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
    slug = models.CharField(max_length=255, blank=True)
    Description = models.TextField(blank=True)
    Init_Date = models.CharField(max_length=10, blank=True)
    Complete_Date = models.CharField(max_length=10, blank=True)
    Deadline_Date = models.CharField(max_length=10, blank=True)
    File = models.FileField(upload_to='pk-slug', blank=True)
    Priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, blank=True, null=True)
    Note = models.TextField(blank=True)
    Is_Complete = models.BooleanField(default=False)

    def __str__(self):
        return self.pk + '-' + str(self.Task)

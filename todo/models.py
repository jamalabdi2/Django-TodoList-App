from django.db import models

class TodoList(models.Model):
    STATUS_CHOICE = (
        ('In Progress','In progress'),
        ('Completed','Completed')
    )
    DEFAULT_STATUS = 'In Progress'
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default=DEFAULT_STATUS, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title.capitalize()
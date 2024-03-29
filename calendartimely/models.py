from django.db import models
from django.urls import reverse

# Create your models here.

REPEAT = (
('D', 'Daily'),
('W', 'Weekly'),
('M', 'Monthly'),
('Y', 'Yearly'),
)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    repeat = models.CharField(max_length=1, choices=REPEAT)

    @property
    def get_html_url(self):
        url = reverse('calendartimely:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
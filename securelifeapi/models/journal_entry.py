from django.db import models

class JournalEntry(models.Model):
    human = models.ForeignKey("Human", related_name='journal_entries', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ForeignKey("Image", related_name='journal_entries', on_delete=models.CASCADE)
from django.db import models

class JournalEntry(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    human = models.ForeignKey("Human", related_name='journal_entries', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    entry = models.CharField(max_length=500)
    
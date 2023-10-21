from django.db import models

class FlashCard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    # created = models.DateTimeField(auto_now=True)
    # updated = models.DecimalField(auto_created=True)
    
    def __str__(self) -> str:
        return f"self.question[0:10]..."

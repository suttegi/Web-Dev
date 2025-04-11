from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=200)
    scores = models.JSONField()

    def get_average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def get_top_score(self):
        if not self.scores:
            return 0
        return max(self.scores)
    
    def __str__(self):
        return f"{self.name} с балами {self.scores}"
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=200)
    scores = models.IntegerField(max_length=2)

    def get_average_score(self):
        sum_score = 0
        for i in self.scores:
            sum_score += i
        avg_score = sum_score / self.scores.length()
        return avg_score
    
    def get_top_score(self):
        max_score = self.scores.sort[-1]
        return max_score
    
    def __str__(self):
        return "${self.name} с балами ${self.scores}"
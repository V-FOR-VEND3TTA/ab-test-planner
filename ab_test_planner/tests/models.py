from django.db import models

class ABTest(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class ABTestVariant(models.Model):
    test = models.ForeignKey(ABTest, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ABTestOutcome(models.Model):
    test = models.ForeignKey(ABTest, related_name='outcomes', on_delete=models.CASCADE)
    metric = models.CharField(max_length=100)
    baseline = models.FloatField()
    goal = models.FloatField()

    def __str__(self):
        return f"{self.metric} (Baseline: {self.baseline}, Goal: {self.goal})"

from django.db import models


# Create your models here.
class VotingOption(models.Model):
    name = models.CharField(max_length=64)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def voteFor(self):
        self.votes += 1

    def clearVotes(self):
        self.votes = 0 

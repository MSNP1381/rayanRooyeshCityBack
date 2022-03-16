from django.db import models


# Create your models here.
class Transaction(models.Model):
    class ActionsEnum(models.IntegerChoices):
        OTHELLO = 1
        PENTAGO = 2
        BEZANGAH = 3
        DREKTESHAF = 4
        HEX = 5
        DOOZ = 6
        KARDASTI = 7
        SIMPLEQ = 8
        HARDQ = 9
        MEDIUMQ = 10
        GOLDENQ = 11
        TANGO = 12
        ORIGAMI = 13
        GAME = 14
        BALANCE = 15
        ADD = 16
        REMOVE = 17

    actionId = models.IntegerField(choices=ActionsEnum.choices, default=15)
    team_id = models.IntegerField()
    withdrawAmount = models.IntegerField()

    def __str__(self):
        return str(self.pk)+ ' '+ str(self.team_id) + ' ' + str(self.actionId) + ' ' + str(self.withdrawAmount)


class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)

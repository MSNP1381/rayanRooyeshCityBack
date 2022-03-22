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
        krdastinejat = 8
        SIMPLEQ = 9
        HARDQ = 10
        MEDIUMQ = 11
        GOLDENQ = 12
        TANGO = 13
        ORIGAMI = 14
        GAME = 15
        BALANCE = 16
        ADD = 17
        REMOVE = 18

    actionId = models.IntegerField(choices=ActionsEnum.choices, default=15)
    team_id = models.IntegerField()
    withdrawAmount = models.IntegerField()

    def __str__(self):
        return str(self.pk) + ' ' + str(self.team_id) + ' ' + str(self.actionId) + ' ' + str(self.withdrawAmount)


class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)


class Sections(models.Model):
    game_id = models.IntegerField()
    section_id = models.IntegerField()
    title = models.CharField(max_length=100)
    is_two = models.BooleanField(default=False)
    enter_amount = models.IntegerField(default=-70)
    win_amount=models.IntegerField(default=100)

    def __str__(self):
        return self.title
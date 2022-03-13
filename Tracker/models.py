from django.db import models


class TeamsData(models.Model):

    objects = None
    team_id = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    team_member_id = models.CharField(max_length=100)
    status_of_member = models.BooleanField()


class TaskData(models.Model):

    objects = None
    task_id = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    team_member = models.CharField(max_length=100)
    task_status = models.CharField(max_length=100)


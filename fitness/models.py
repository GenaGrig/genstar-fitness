from django.db import models


class RegisteredUser(models.Model):
    '''Model for registered users.'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Trainer(models.Model):
    '''Model for trainers.'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Workout(models.Model):
    '''Model for workouts.'''
    workout_name = models.CharField(max_length=100)
    workout_description = models.CharField(max_length=100)
    workout_video = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.workout_name


class WorkoutPlan(models.Model):
    '''Model for workout plans.'''
    workout_plan_name = models.CharField(max_length=100)
    workout_plan_description = models.CharField(max_length=100)
    workout_plan_video = \
        models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.workout_plan_name


class WorkoutTrainer(models.Model):
    '''Model for workout trainers.'''
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.workout.workout_name + " - " + self.trainer.first_name \
            + " " + self.trainer.last_name

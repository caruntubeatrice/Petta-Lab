from __future__ import unicode_literals
from django.db import models

# Pressure table for the 1st fridge
class press_1(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Pressure table for the 2nd fridge
class press_2(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Pressure table for the 3rd fridge
class press_3(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Pressure table for the 4th fridge
class press_4(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Pressure table for the 5th fridge
class press_5(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Pressure table for the 6th fridge
class press_6(models.Model):
    time = models.DateTimeField(primary_key=True)
    press_in = models.FloatField()
    press_out = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return "press_in = " + self.press_in + ", press_out = " + self.press_out

# Temperature Table for the 1st fridge
class temp_1(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil

# Temperature Table for the 2nd fridge
class temp_2(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil

# Temperature Table for the 3rd fridge
class temp_3(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil

# Temperature Table for the 4th fridge

class temp_4(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil

# Temperature Table for the 5th fridge

class temp_5(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil

# Temperature Table for the 6th fridge
class temp_6(models.Model):
    time = models.DateTimeField(primary_key=True)
    temp_in = models.FloatField()
    temp_out = models.FloatField()
    temp_oil = models.FloatField()
    def __str__(self):
        return "t_in = " + self.temp_in + ",t_out= " + self.temp_out + ",t_oil= " + self.temp_oil
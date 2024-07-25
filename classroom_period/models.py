from django.db import models

# from course.models import Courses

# Create your models here.


class ClassPeriod(models.Model):

   start_time=models.TimeField()
   end_time=models.TimeField()
   course=models.CharField(max_length=20)
   # course_id = models.ForeignKey(Courses, default=None, on_delete=models.CASCADE, related_name='course_name')
   classroom=models.CharField(max_length=20)
   day_of_the_week=models.DateField()
   def __str__(self):
        return f"{self.start_time} {self.end_time}"

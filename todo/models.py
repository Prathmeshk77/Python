from django.db import models
class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    
    def __str__(self):
        st=self.fname+self.lname
        return st


class Todo(models.Model):
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    time = models.DateTimeField(null = True, blank = True)
    statusch  = (('1','Created'),('2','Inprocess'),('3','Done'))
    status = models.CharField(max_length = 20, choices = statusch)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         ss=self.title +self.status
         return ss  

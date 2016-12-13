from django.db import models

class Book(models.Model):
    Name = models.CharField( max_length = 100 )
    Link = models.CharField( max_length = 200 )
    Description = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.Name



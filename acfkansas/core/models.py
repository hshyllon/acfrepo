from django.db import models
import datetime
from django.contrib.auth.models import User



class DevotionCategory(models.Model):
    category = models.CharField(max_length=128, blank=False)
    
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s' %( self.cat_title)

class Devotion(models.Model):
    devotion_title = models.CharField(max_length=128, blank=False)
    #devotion_category = models.CharField(max_length=128, blank=False, default = "Religion")
    author = models.ForeignKey(User) 
    dev_picture = models.ImageField(upload_to='devotions', blank = False, null = True)
    message = models.TextField(max_length=20000, blank=False)
    #make_it_visible = models.BooleanField('Visible in Website?', default = True)
    make_visible = models.BooleanField('Visible in the Website?', default = True)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    
    def __str__(self):
        return u'%s %s' %(self.author, self.devotion_title)
    

class Album(models.Model):
    album_title = models.CharField(max_length=128, blank=False)
    album_desc = models.CharField(max_length=128, blank=False)
    make_it_visible = models.BooleanField('Visible in Website Album?',default = True)
    homepage_visible = models.BooleanField('Visible in Homepage?',default = False)
    
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    def __str__(self):
        return u'%s %s' %(self.album_title, self.create_date)
    
class Gallery(models.Model):
    #pic_desc = models.CharField(max_length=128, blank = False, null = True)
    pic = models.ImageField(upload_to='gallery', blank = False, null = True)
    pic_album = models.ForeignKey(Album)
    is_album_cover = models.BooleanField('Album Cover?', default = False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s %s' %(self.pic.name, self.create_date)
    
# Create your models here.
class UpcomingEvent(models.Model):
    event_title = models.CharField(max_length=128, blank=False)
    location = models.CharField(max_length=128, blank=False)
    start_day = models.DateField('Begin Day',default=datetime.date.today)
    start_day_start_time = models.TimeField('Begin Start Time',default=datetime.time)
    start_day_end_time = models.TimeField('Begin End Time',default=datetime.time)
    end_day = models.DateField('Final Day',default=datetime.date.today)
    end_day_start_time = models.TimeField('Final Start Time',default=datetime.time)
    end_day_end_time = models.TimeField('Final End Time',default=datetime.time)
    adult_cost = models.DecimalField('Cost for Adult',default= '0', max_digits=7, decimal_places=2)
    youth_cost = models.DecimalField('Cost for Youth', default= '0', max_digits=7, decimal_places=2)
    children_cost = models.DecimalField('Cost for Child',default= '0', max_digits=7, decimal_places=2)
    event_note = models.TextField('Event Description',max_length=256, blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    make_visible = models.BooleanField('Visible in HomePage?',default = False)
    
    def __str__(self):
        return u'%s %s' %(self.event_title, self.start_day)
    
class ThingsHappening(models.Model):
    happening_thing_title = models.CharField(max_length=128, blank=False)
    happening_thing_location = models.CharField(max_length=128, blank=False)
    start_time = models.TimeField(default=datetime.time)
    end_time = models.TimeField(default=datetime.time)
    frequency = models.CharField(max_length=128, blank=True)
    adult_cost = models.DecimalField(default= '0', max_digits=7, decimal_places=2)
    youth_cost = models.DecimalField(default= '0', max_digits=7, decimal_places=2)
    children_cost = models.DecimalField(default= '0', max_digits=7, decimal_places=2)
    happening_thing_photo = models.ImageField(upload_to = 'happening_thing_gallery', blank= True)
    happening_thing_note = models.TextField(max_length=256, blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    make_visible = models.BooleanField(default = False)
    show_in_homepage = models.BooleanField(default = False)
    
    def __str__(self):
        return u'%s' %(self.happening_thing_title)
    
    
class Uploads(models.Model):
    author = models.ForeignKey(User, default = 7) 
    document_title = models.CharField(max_length=128, blank=False)
    document_description = models.TextField(max_length=256, blank=False)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    make_visible = models.BooleanField(default = False)
    
    def __str__(self):
        return u'%s' %(self.document_title)
    
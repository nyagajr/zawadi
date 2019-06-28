from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name  = models.CharField(max_length=30)  
    location = models.CharField(max_length =10)
    # profile = models.ForeignKey(Profile, null = True,related_name='neighbourhood')
    # occupants = models.ForeignKey(User, null = True,related_name='business')
    admin = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hoodimage/', null=True)
   
    
    def save_restaurant(self):
        self.save()

    def delete_restaurant(self):
        self.delete()

    @classmethod
    def find_restaurant_id(cls, id):
        restaurant = Restaurant.objects.get(pk=id)
        return restaurant

    @classmethod
    def get_profile_restaurant(cls, profile):
        restaurant = Restaurant.objects.filter(profile__pk = profile)
        return restaurant

   
 

  

  
    

class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50,null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',blank=True, null=True)
    # first_name = models.CharField(max_length =30)
    # last_name = models.CharField(max_length =30)
    email = models.EmailField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
    
   
class Post(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 50,null = True)
    user = models.ForeignKey(User, null = True,related_name='post')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null = True,related_name='posts')
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_hood_posts(cls,id):
        posts = Post.objects.filter(id = id)
        return posts



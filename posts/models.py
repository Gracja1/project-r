from django.db import models


# Create your models here.

# do zmiany na restaurant
class Posts(models.Model):
    rest_name = models.CharField(max_length=32)
    rest_descp = models.TextField()

    # rest_type ( 1 do 1 polaczenie z typem restauracji)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # jak bedzie wygladac objekt klasy Posts w shellu
        return self.rest_name

        # to w shellu
        # from  posts.models import Posts
        # Posts.objects.all()


class User(models.Model):
    pass
    # tu wszystko pod django auth i formularz w HTML metodą post



class Comment(models.Model):
    users = models.ManyToManyField(User)
    restaurant = models.ForeignKey(Posts, on_delete=models.CASCADE)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # nizej do  bedzie pasowac po zamianie modelu post na restaurant.
    # user = User.objects.get(id=1)
    # restaurant = Restaurant.objects.get(id=2)
    # comment = Comment.objects.create(restaurant=restaurant, text='Great food!')
    # comment.users.add(user)

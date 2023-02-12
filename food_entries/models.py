from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import ModelForm

STATUS = ((0, "Draft"), (1, "Published"))


class Entry(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entry_recipe")  # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# class EntryForm(ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['title', 'description']


# entryform = EntryForm()


# This custom model below was going to be used to allow users upon registration
# and login to add their family name so they can view posts from their family members   # noqa
# but i could not figure out how to import an extra field into the standard allauth   # noqa
# signup.html or login.html forms and since the project was already overdue, I decided to  # noqa
# comment it out so it's intention could be seen.

# class FamilyMember(models.Model):
#     name = models.CharField(max_length=150)
#     family_name = models.CharField(max_length=150)
#     likes = models.TextField()
#     dislikes = models.TextField()

#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


class Team(models.Model):
    """Model representing a team."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a team name",
    )
    members = models.ManyToManyField(
        User,
        help_text="Select team members",
        blank=True,
    )
    secrets = models.ManyToManyField(
        'Secret',
        help_text="Select team secrets",
        blank=True,
    )

    def display_members(self):
        """Creates a string for the Members. This is required to display members in Admin."""
        return ', '.join([member.username for member in self.members.all()[:3]])

    display_members.short_description = 'Members'

    def get_absolute_url(self):
        """Returns the url to access a particular team instance."""
        return reverse('team-detail', args=[str(self.id)])

    class Meta:
        permissions = (("can_manage_group", "Manage a group"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Secret(models.Model):
    """Model representing a secret."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular secret across whole storage",
    )
    name = models.CharField(
        max_length=200,
        help_text="Enter a secret name",
    )
    content = models.CharField(
        max_length=200,
        help_text="Enter a secret content",
    )
    comment = models.TextField(
        max_length=1000,
        help_text="Enter a secret comment",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular secret instance."""
        return reverse('my-secret-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=512)
    email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=100)
    site_admin = models.BooleanField()
    name = models.CharField(max_length=512, null=True, blank=True)
    node_id = models.CharField(max_length=512)
    avatar_url = models.CharField(max_length=512)
    gravatar_id = models.CharField(max_length=10, null=True, blank=True)
    url = models.CharField(max_length=512)
    html_url = models.CharField(max_length=512)
    followers_url = models.CharField(max_length=512)
    following_url = models.CharField(max_length=512)
    gists_url = models.CharField(max_length=512)
    starred_url = models.CharField(max_length=512)
    subscriptions_url = models.CharField(max_length=512)
    organizations_url = models.CharField(max_length=512)
    repos_url = models.CharField(max_length=512)
    events_url = models.CharField(max_length=512)
    received_events_url = models.CharField(max_length=512)
    company = models.CharField(max_length=512, null=True, blank=True)
    blog = models.CharField(max_length=512, null=True, blank=True)
    location = models.CharField(max_length=512, null=True, blank=True)
    hireable = models.NullBooleanField()
    bio = models.TextField(null=True, blank=True)
    public_repos = models.IntegerField()
    public_gists = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.login

from django.db import models

app_name = "games"


class Game(models.Model):

    # choices
    YES = "Y"
    NO = "N"
    _EDITORS_CHOICE = (
        (YES, "yes"),
        (NO, "no"),
    )

    title = models.CharField(
        "Title",
        max_length=255,
    )
    platform = models.CharField(
        "Platform",
        max_length=100,
    )
    score = models.FloatField(
        "Score",
    )
    genre = models.CharField(
        "Genre",
        max_length=100,
        null=True,
    )
    editors_choice = models.CharField(
        "Editors' Choice",
        max_length=1,
        choices=_EDITORS_CHOICE,
        default=NO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

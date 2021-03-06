from django.db import models
from django.contrib.auth.models import User

AREA_TYPES = [
    ('Film', 'Film'),
    ('TV', 'TV'),
    ('OAV', 'OAV')
]

MUSIC_TYPES = [
    ('OP', 'OP'),
    ('ED', 'ED'),
    ('OST', 'OST')
]
RATINGS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
]


class Franchise(models.Model):
    franchies_name = models.CharField(max_length=255, unique=True)
    franchise_slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True, unique=True)


    film_type = models.BooleanField(default=False)
    film_num = models.IntegerField()

    tv_type = models.BooleanField(default=False)
    tv_num = models.IntegerField()

    oav_type = models.BooleanField(default=False)
    oav_num = models.IntegerField()

    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    all_user_average = models.IntegerField()
    def __str__(self):
        return self.franchies_name


class UserOverallOpinion(models.Model):
    user_real_average = models.IntegerField()
    user_opinion_average = models.CharField(max_length=255, choices=RATINGS)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class FranchiseUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)


class AllFilmUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)


class AllTVAllSeasonUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)


class AllOAVUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)


class FranchiseItem(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    name = models.CharField(max_length=255)
    number_of_episodes = models.IntegerField()
    all_user_average = models.IntegerField()
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class FranchiseItemUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.PROTECT)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    animation_opinion = models.IntegerField()
    story_opinion = models.IntegerField()
    op_num = models.IntegerField()
    ed_num = models.IntegerField()
    music_opinion = models.IntegerField()


class Episides(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.PROTECT)
    episode_number = models.IntegerField()
    all_user_average = models.IntegerField()
    def __int__(self):
        return self.episode_number


class EpisidesUser(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.PROTECT)
    episode_number = models.ForeignKey(Episides, on_delete=models.PROTECT)
    user_opinion = models.IntegerField()
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)


class Music(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.PROTECT)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.PROTECT)
    song_name = models.CharField(max_length=255)
    song_type = models.CharField(max_length=255, choices=MUSIC_TYPES)
    all_user_average = models.IntegerField()
    def __str__(self):
        return self.song_name


class MusicUser(models.Model):
    song_name = models.ForeignKey(Music, on_delete=models.PROTECT)  # need to make unique
    song_rate = models.IntegerField()
    
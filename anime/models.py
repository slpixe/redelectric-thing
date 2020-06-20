from django.db import models

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
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]


class Franchise(models.Model):
    franchies_name = models.CharField(max_length=255)# need to make unique
    franchise_slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)


    film_type = models.BooleanField(default=False)
    film_num = models.IntegerField()

    tv_type = models.BooleanField(default=False)
    tv_num = models.IntegerField()

    oav_type = models.BooleanField(default=False)
    oav_num = models.IntegerField()

    all_user_average = models.IntegerField()
    def __str__(self):
        return self.franchies_name


class UserOverallOpinion(models.Model):
    user_real_average = models.IntegerField()
    user_opinion_average = models.CharField(max_length=255, choices=RATINGS)

    class Meta:
        abstract = True


class FranchiseUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)


class AllFilmUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)


class AllTVAllSeasonUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)


class AllOAVUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)


class FranchiseItem(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    name = models.CharField(max_length=255)
    number_of_episodes = models.IntegerField()
    all_user_average = models.IntegerField()

    def __str__(self):
        return self.name


class FranchiseItemUser(UserOverallOpinion):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.CASCADE)
    animation_opinion = models.IntegerField()
    story_opinion = models.IntegerField()
    op_num = models.IntegerField()
    ed_num = models.IntegerField()
    music_opinion = models.IntegerField()


class Episides(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    all_user_average = models.IntegerField()
    def __int__(self):
        return self.episode_number


class EpisidesUser(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.CASCADE)
    episode_number = models.ForeignKey(Episides, on_delete=models.CASCADE)
    user_opinion = models.IntegerField()


class Music(models.Model):
    franchies_name = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    area_type = models.CharField(max_length=255, choices=AREA_TYPES)
    franchies_item_name = models.ForeignKey(FranchiseItem, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=255)
    song_type = models.CharField(max_length=255, choices=MUSIC_TYPES)
    all_user_average = models.IntegerField()
    def __str__(self):
        return self.song_name


class MusicUser(models.Model):
    song_name = models.ForeignKey(Music, on_delete=models.CASCADE)  # need to make unique
    song_rate = models.IntegerField()
    
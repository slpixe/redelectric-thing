# i = 9
# tv_eps + i = "Test"
# print(tv_eps9)
from . models import Franchise, FranchiseItem, FranchiseUser, FranchiseItemUser, Episides
class Item:
    def __init__(self, name, ep_num, story, animation, music, overall):
        self.name = name
        self.ep_num = ep_num
        self.story = story
        self.animation = animation
        self.music = music
        self.overall = overall

class Episode:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

tvs = []
        tv_items = FranchiseItem.objects.filter(franchies_name=2, area_type="TV")
        if not tv_items.exists():
            tvs = None
        else:
            tv_rates = FranchiseItemUser.objects.filter(franchies_name=franchises_details.id, author=request.user, area_type="TV")
            for tv_item in tv_items:
                tv_eps = []
                tv_item_eps = Episides.objects.filter(franchies_name=franchises_details.id, franchies_item_name=tv_item.id)
                tv_rating = False
                for tv_rate in tv_rates:
                    if tv_item.id == tv_rate.franchies_item_name_id:
                        tv_rating = True
                        tv_item.stroy = (f'{tv_rate.story_opinion}{rate_max}')
                        tv_item.animation = (f'{tv_rate.animation_opinion}{rate_max}')
                        tv_item.music = (f'{tv_rate.music_opinion}{rate_max}')
                        tv_item.overall = (f'{tv_rate.user_opinion_average}{rate_max}')
                if not tv_rating:
                    tv_item.stroy = "Not Yet Rated"
                    tv_item.animation = "Not Yet Rated"
                    tv_item.music = "Not Yet Rated"
                    tv_item.overall = "Not Yet Rated"
                for tv_item_ep in tv_item_eps:
                    tv_item_ep.name = "Test Name"
                    tv_item_ep.rate = "Test Rate"
                    tv_eps.append(Episode(tv_item_ep.name, tv_item_ep.rate))                
                print(tv_eps)
                tvs.append(Item(tv_item.name, tv_item.number_of_episodes, tv_item.stroy, tv_item.animation, tv_item.music, tv_item.overall))
                tvs.append(tv_eps)
                tv_eps.clear()
# tvs = []
# tv_items_tests = [1,2,3,4]
# i = 0
# ep_test = 6
# for tv_item in tv_items_tests:
#     i += 1
#     name = i
#     stroy = i
#     animation = i
#     music = i
#     overall = i
#     tvs.append(Item(name, ep_test, stroy, animation, music, overall))

# print(tvs.name)





d = {}
for x in range(1, 10):
    d["string{0}".format(x)] = "Hello"

print(d["string5"])

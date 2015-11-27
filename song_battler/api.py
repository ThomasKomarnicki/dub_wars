from tastypie.resources import ModelResource
from tastypie import fields
from models import Song, SongBattle, UserProfile

class UserResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'


class SongBattleResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user_profile')

    class Meta:
        queryset = SongBattle.objects.all()
        resource_name = 'battle'

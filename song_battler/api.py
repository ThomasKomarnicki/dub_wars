from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.http import HttpForbidden
from tastypie.utils import trailing_slash
from django.conf.urls import url
from models import Song, SongBattle, UserProfile
from models_helper import get_song_battle

class UserResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
        fields = ['id', 'email', 'user_type']


class SongBattleResource(ModelResource):
    """
    GET battle/new - gets a new song battle
    PUT battle/{id}/winner - update the battle with the winner
    {"winner":1}
    """
    user = fields.ForeignKey(UserResource, 'user_profile')

    class Meta:
        queryset = SongBattle.objects.all()
        resource_name = 'battle'

    def prepend_urls(self):
        """ Add the following array of urls to the GameResource base urls """
        return [
            url(r"^(?P<resource_name>%s)/new%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_new_battle'), name="new"),
             url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/winner%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('set_winner'), name="winner"),
        ]

    def get_new_battle(self, request, **kwargs):
        song_battle = get_song_battle(request.session.session_key)
        return self.create_response(request,song_battle)

    def set_winner(self, request, **kwargs):
        if request.method != "PUT":
            return HttpForbidden("Only accepts PUT requests")

        return self.patch_detail(request, **kwargs)


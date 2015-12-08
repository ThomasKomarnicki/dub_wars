from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.http import HttpForbidden, HttpAccepted
from tastypie.utils import trailing_slash
from django.conf.urls import url
from models import Song, SongBattle, UserProfile
from models_helper import get_song_battle
from tastypie.serializers import Serializer
from django.http import QueryDict, HttpResponse


class UserResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
        fields = ['id', 'email', 'user_type']


class SongResource(ModelResource):
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'
        fields = ['id', 'name', 'url', 'song_id']

    def prepend_urls(self):
        """ Add the following array of urls to the GameResource base urls """
        return [
            # url(r"^(?P<resource_name>%s)/search%s/$" % (self._meta.resource_name, trailing_slash()),
            #     self.wrap_view('search'), name="search"),
            url(r"^search/(?P<query>\w*)%s$" % (trailing_slash()),
                self.wrap_view('search'), name="search"),
        ]

    def search(self, request, query, **kwargs):
        filtered_songs = Song.objects.filter(name__icontains=query).all()
        # print filtered_songs
        bundles = [self.build_bundle(obj=q, request=request) for q in filtered_songs]
        data = [self.full_dehydrate(bundle) for bundle in bundles]
        serialized_data = self.serialize(None, data, 'application/json')
        return HttpResponse(content=serialized_data)



class SongBattleResource(ModelResource):
    """
    GET battle/new - gets a new song battle
    PUT battle/{id}/winner - update the battle with the winner
    {"winner":1}
    """
    user = fields.ForeignKey(UserResource, 'user', full=True)
    left_song = fields.ForeignKey(SongResource, 'left_song', full=True)
    right_song = fields.ForeignKey(SongResource, 'right_song', full=True)

    class Meta:
        queryset = SongBattle.objects.all()
        resource_name = 'battle'
        serializer = Serializer(formats=['json'])
        fields = ['id', 'user', 'left_song', 'right_song', 'winner']

    def prepend_urls(self):
        """ Add the following array of urls to the GameResource base urls """
        return [
            url(r"^(?P<resource_name>%s)/new%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_new_battle'), name="new"),
             url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/winner%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('set_winner'), name="winner"),
        ]

    def get_new_battle(self, request, **kwargs):
        song_battle = get_song_battle(request, request.session.session_key)
        print "got new song battle: " + str(song_battle)
        # serialized = self.serialize(request, song_battle, 'application/json')
        return self.get_detail(request, pk=song_battle.id, api_name='v1', resource_name='battle')

    def set_winner(self, request, *args, **kwargs):
        if request.method != "PUT":
            return HttpForbidden("Only accepts PUT requests")

        body = QueryDict(request.body)
        winner = body.get('winner')
        song_battle = SongBattle.objects.get(id=kwargs['pk'])
        song_battle.winner = winner
        song_battle.save()
        return HttpAccepted()


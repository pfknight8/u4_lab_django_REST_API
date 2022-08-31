from rest_framework import serializers
from .models import Team, Player, Conference, Division

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
  divisions = serializers.HyperlinkedRelatedField(
    view_name='division_detail',
    many=True,
    read_only=True
  )
  # conference_url = serializers.ModelSerializer.serializer_url_field(
  #   view_name='conference_detail'
  # )
  class Meta:
    model = Conference
    fields = ('id', 'name', 'league', 'founded', 'divisions', 'conference_url')

class DivisionSerializer(serializers.HyperlinkedModelSerializer):
  # teams = serializers.HyperlinkedRelatedField(
  #   view_name='team_detail',
  #   many=True,
  #   read_only=True
  # )
  division_url = serializers.ModelSerializer.serializer_url_field(
    view_name='division_detail'
  )
  conference_id = serializers.PrimaryKeyRelatedField(
    queryset=Conference.objects.all(),
    source='conference'
  )
  class Meta:
    model = Division
    fields = ('id', 'name', 'conference_id', 'division_url')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField(
    view_name='team_detail',
    read_only=True
  )
  team_id = serializers.PrimaryKeyRelatedField(
    queryset=Team.objects.all(),
    source='team'
  )
  class Meta:
    model = Player
    fields = ('id', 'name', 'birthdate', 'team', 'team_id')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  players = serializers.HyperlinkedRelatedField(
    view_name='player_detail',
    many=True,
    read_only=True
  )
  division_id = serializers.PrimaryKeyRelatedField(
    queryset=Division.objects.all(),
    source='division'
  )
  class Meta:
    model = Team
    fields = ('id', 'name', 'location', 'division_id', 'players')

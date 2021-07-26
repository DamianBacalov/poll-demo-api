from rest_framework import serializers
from api.models import VotingOption


class VotingOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VotingOption
        fields = ('pk', 'name', 'votes')


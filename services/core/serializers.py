from dataclasses import field
from rest_framework  import serializers
from core.models import Fund,Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("Member_id","Member_name")

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ("Fund_id","Fund_data")

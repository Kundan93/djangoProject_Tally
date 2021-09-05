from rest_framework import serializers
import djangoProject


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = djangoProject
        fields = ('C1',
                  'C2',
                  'C3')
from rest_framework import serializers

from CMS.models import Customer


class CustomerSerializer(serializers.Serializer):
    account_number = serializers.IntegerField()
    account_name = serializers.CharField(max_length=255)
    account_holder_name = serializers.CharField(max_length=255)
    customer_birth_date = serializers.DateField()
    customer_nida = serializers.IntegerField()
    customer_role = serializers.CharField(max_length=20)
    customer_occupation = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.account_number = validated_data.get('account_number',instance.account_number)
        instance.account_holder_name = validated_data.get('account_holder_name',instance.account_holder_name)
        instance.customer_role = validated_data.get('account_role',instance.customer_role)

        instance.save()
        return instance

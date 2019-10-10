from rest_framework import serializers
from userinfo.models import UserInfo, MicroLoan


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'name', 'age', 'monthly_income', 'investments', 'bills', 'leisure', 'mortgage']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.monthly_income = validated_data.get('monthly_income', instance.monthly_income)
        instance.investments = validated_data.get('investments', instance.investments)
        instance.bills = validated_data.get('bills', instance.bills)
        instance.leisure = validated_data.get('leisure', instance.leisure)
        instance.mortgage = validated_data.get('mortgage', instance.mortgage)
        instance.save()
        return instance


class MicroLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroLoan
        fields = ['id', 'borrower', 'creditor', 'borrower_status', 'creditor_status', 'interest', 'amount', 'duration', 'status']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return MicroLoan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.borrower = validated_data.get('borrower', instance.borrower)
        instance.creditor = validated_data.get('creditor', instance.creditor)
        instance.borrower_status = validated_data.get('borrower_status', instance.borrower_status)
        instance.creditor_status = validated_data.get('creditor_status', instance.creditor_status)
        instance.borrower_interest = validated_data.get('borrower_interest', instance.borrower_interest)
        instance.borrower_amount = validated_data.get('borrower_amount', instance.borrower_amount)
        instance.borrower_duration = validated_data.get('borrower_duration', instance.borrower_duration)    
        instance.creditor_interest = validated_data.get('creditor_interest', instance.creditor_interest)
        instance.creditor_amount = validated_data.get('creditor_amount', instance.creditor_amount)
        instance.creditor_duration = validated_data.get('creditor_duration', instance.creditor_duration)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance

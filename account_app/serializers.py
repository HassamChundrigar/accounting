from rest_framework import serializers
from .models import Entry, SubEntry, SubHeadAccount, SubHead, Head


class SubHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubHead
        fields = '__all__'


class SubHeadAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubHeadAccount
        fields = '__all__'


class SubHeadAccountListSerializer(serializers.ModelSerializer):
    sub_head = SubHeadSerializer()

    class Meta:
        model = SubHeadAccount
        fields = '__all__'


class SubEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubEntry
        fields = '__all__'


class SubEntryListSerializer(serializers.ModelSerializer):
    sub_head_account = SubHeadAccountListSerializer()

    class Meta:
        model = SubEntry
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    debit = SubEntrySerializer()
    credit = SubEntrySerializer()

    class Meta:
        model = Entry
        fields = '__all__'

    def create(self, validated_data):
        deb_amount = validated_data['debit'].get('amount')
        deb_acc = validated_data['debit'].get('sub_head_account')

        cre_amount = validated_data['credit'].get('amount')
        cre_acc = validated_data['credit'].get('sub_head_account')

        if (deb_amount != cre_amount):
            raise serializers.ValidationError(
                "Debit Amount Should Be Equal Credit Amount")
        if ((deb_amount <= 0) | (cre_amount <= 0)):
            raise serializers.ValidationError(
                "Amount should be greater than zero")

        deb = SubEntry.objects.create(
            amount=deb_amount, sub_head_account=deb_acc)
        cre = SubEntry.objects.create(
            amount=cre_amount, sub_head_account=cre_acc)

        dated = validated_data['dated']
        description = validated_data.get('description')
        if description == None:
            description = ""
        entry = Entry.objects.create(
            debit=deb, credit=cre, dated=dated, description=description)

        return entry

    def update(self, instance, validated_data):
        print(instance.debit.amount, instance.credit.amount)
        deb_amount = validated_data['debit'].get('amount')
        deb_acc = validated_data['debit'].get('sub_head_account')

        cre_amount = validated_data['credit'].get('amount')
        cre_acc = validated_data['credit'].get('sub_head_account')

        if (deb_amount != cre_amount):
            raise serializers.ValidationError(
                "Debit Amount Should Be Equal Credit Amount")
        if ((deb_amount <= 0) | (cre_amount <= 0)):
            raise serializers.ValidationError(
                "Amount should be greater than zero")

        instance.debit.amount =deb_amount
        instance.debit.sub_head_account = deb_acc
        instance.debit.save()
        instance.credit.amount =cre_amount
        instance.credit.sub_head_account = cre_acc
        instance.credit.save()
        instance.dated = validated_data['dated']
        description = validated_data.get('description')

        if description == None: instance.description = ""
        else: instance.description = description

        instance.save()
        print(instance.debit.amount, instance.credit.amount)
        return instance


class EntryListSerializer(serializers.ModelSerializer):
    debit = SubEntryListSerializer()
    credit = SubEntryListSerializer()

    class Meta:
        model = Entry
        fields = '__all__'

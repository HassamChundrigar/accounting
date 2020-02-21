from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

# Create your models here.

Head = (
    ('Asset', "Asset"),
    ('Expense', "Expense"),
    ('Liability', "Liability"),
    ('Revenue', "Revenue"),
    ('Equity', "Equity")
)


class SubHead(models.Model):
    head = models.CharField(choices=Head, max_length=15)
    sub_head = models.CharField(max_length=100)

    class Meta:
        unique_together = (('head','sub_head'),)
        index_together = (('head','sub_head'),)
    def __str__(self):
        return self.sub_head


class SubHeadAccount(models.Model):
    sub_head = models.ForeignKey(SubHead, on_delete=models.CASCADE)
    sub_head_account = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('sub_head','sub_head_account'),)
        index_together = (('sub_head','sub_head_account'),)
    def __str__(self):
        return self.sub_head_account


class SubEntry(models.Model):
    sub_head_account = models.ForeignKey(SubHeadAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    def __str__(self):
        return self.sub_head_account.sub_head_account + ' ( '+self.sub_head_account.sub_head.sub_head+' --> '+self.sub_head_account.sub_head.head+' ) ' + str(self.amount)


class Entry(models.Model):
    dated = models.DateField()
    debit = models.ForeignKey(SubEntry, on_delete=models.CASCADE, related_name='debit')
    credit = models.ForeignKey(SubEntry, on_delete=models.CASCADE, related_name='credit')
    description = models.TextField(null=True, blank=True)
    created_on = models. DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
        
    @property
    def total_amount(self):
        amount = self.debit.amount
        return amount

@receiver(post_delete, sender=Entry)
def delete_entry(sender, instance, using, **kwargs):
    try: instance.debit.delete()
    except: pass
    try: instance.credit.delete()
    except: pass

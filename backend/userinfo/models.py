from django.db import models
import uuid



class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200)
    monthly_income = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    investments = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    bills = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    leisure = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    mortgage = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    documents = models.URLField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)


class MicroLoan(models.Model):

    EXPIRED = 0
    COMPLETED = 1
    PENDING = 2
    STATUS_CHOICES = ((EXPIRED,0),(COMPLETED,1),(PENDING,2))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    borrower = models.OneToOneField('UserInfo', null=True, related_name="borrower", on_delete=models.SET_NULL)
    creditor = models.OneToOneField('UserInfo', null=True, related_name="creditor", on_delete=models.SET_NULL)
    borrower_status = models.BooleanField(default=True)
    creditor_status = models.BooleanField(default=False)

    borrower_interest = models.SmallIntegerField()
    borrower_amount = models.DecimalField(max_digits=7, decimal_places=2)
    borrower_duration = models.SmallIntegerField() #months

    creditor = models.SmallIntegerField()
    creditor = models.DecimalField(max_digits=7, decimal_places=2)
    creditor = models.SmallIntegerField() #months

    status = models.PositiveSmallIntegerField(verbose_name=("status"), choices=STATUS_CHOICES, default=PENDING, blank=False)

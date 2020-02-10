from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


class Participants(models.Model):
	name = models.CharField(max_length=120)
	
	def part_hold_amount(self):
		hold_amount=self.loan.hold_amount.all()
		part_hold_amount=self.hold_amount.part_hold_amount.all()
		return hold_amount + part_hold_amount

	def part_profit_amount(self):
		return Loan.profit_amount

	def __str__(self):
		return self.name


class Hold_amount(models.Model):
	participant = models.ForeignKey(Participants, on_delete=models.CASCADE, blank=True, null=True)
	part_hold_amount = models.IntegerField(default=0)
	date=models.DateField()


class Loan(models.Model):
	participant = models.ForeignKey(Participants, on_delete=models.CASCADE, blank=True, null=True)
	loan_amount = models.IntegerField(default=0)
	hold_amount = models.IntegerField(default=0)
	profit_amount = models.IntegerField(default=0)
	date=models.DateField(blank=True, null=True)

	#-----recived from get_total_amount signal-----#
	totla_loan_amount=models.IntegerField(default=0)

	#-----recived from get_paid_amount signal------#
	paid_amount=models.IntegerField(default=0)

	def __str__(self):
		return f"{self.participant.name} - loan is :{self.id}"




class Pyments(models.Model):
	loan=models.ForeignKey(Loan, on_delete=models.CASCADE)
	pyment=models.IntegerField()
	date=models.DateField()

	def __str__(self):
		return f" payment :{self.id} - {self.date}"



#-------------- singnel to popelate Loan.paid_amount ------------- #
@receiver(pre_save, sender=Loan)
def get_total_amount(instance, *args, **kwargs):
	instance.totla_loan_amount=instance.loan_amount+instance.hold_amount+instance.profit_amount
	

#-------------- singnel to popelate Loan.paid_amount (add when created) ------------- #
@receiver(pre_save, sender=Pyments)
def get_paid_amount_Add(instance, *args, **kwargs):
	instance.loan.paid_amount += instance.pyment
	instance.loan.save()

#-------------- singnel to popelate Loan.paid_amount (subtract when deleted) -------- #
@receiver(pre_delete, sender=Pyments)
def get_paid_amount_sabtract(instance, *args, **kwargs):
	instance.loan.paid_amount -= instance.pyment
	instance.loan.save()


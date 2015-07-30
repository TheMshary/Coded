from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length=30, unique=True)

class Cereal(models.Model):

	# cereal identification attributes
	name = models.CharField(max_length=30, unique=True)
	cereal_type = models.CharField(max_length=1, null=True)
	manufacturer = models.ForeignKey("main.Manufacturer", null=True)

	# other
	shelf = models.ForeignKey("main.DisplayShelf")
	ss_weight = models.IntegerField(null=True)
	cps = models.FloatField(null=True)

class NutritionFacts(models.Model):

	calories = models.IntegerField(null=True)

	protein = models.IntegerField(null=True)				# grams
	fat = models.IntegerField(null=True)					# grams
	fiber = models.IntegerField(null=True)					# grams
	carbs = models.IntegerField(null=True)					# grams
	sugar = models.IntegerField(null=True)					# grams

	sodium = models.IntegerField(null=True)					# milligrams
	potassium = models.IntegerField(null=True)				# milligrams
	vitamins_minerals = models.IntegerField(null=True)		# milligrams
	cereal = models.OneToOneField("main.Cereal")

class DisplayShelf(models.Model):
	number = models.IntegerField(unique=True)

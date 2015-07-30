#!/usr/bin/env python
import csv, os, sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cereal.settings")

from main.models import Manufacturer, Cereal, NutritionFact, DisplayShelf

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file)), "cereal.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	
	cereal = Cereal()

	manufacturer, created = Manufacturer.objects.get_or_create(name=row['manufacturer'])

	try:
		manufacturer.save()
	except Exception, e:
		print e
		print "ERROR :::: Failed to save Manufacturer instance"

	cereal.cereal_type = row['type']
	cereal.display_shelf = row['display shelf']
	cereal.ss_weight = row['serving size weight']
	cereal.cps = row['cups per serving']
	cereal.manufacturer = manufacturer

	shelf, created = DisplayShelf.objects.get_or_create(number=row['display shelf'])

	
	try:
		shelf.save()
	except Exception, e:
		print e
		print "ERROR :::: Failed to save DisplayShelf instance"

	cereal.shelf = shelf

	try:
		cereal.save()
	except Exception, e:
		print e
		print "ERROR :::: Failed to save Cereal instance"

	nurtition = NutritionFacts()
	nutrition.calories = row['calories']
	nutrition.protein = row['protein (g)']
	nutrition.fat = row['fat']
	nutrition.fiber = row['dietary fiber']
	nutrition.carbs = row['carbs']
	nutrition.sugar = row['sugars']
	nutrition.sodium = row['sodium']
	nutrition.potassium = row['potassium']
	nutrition.vitamins_minerals = row['vitamins and minerals']
	nutrition.cereal = cereal

	try:
		nutrition.save()
	except Exception, e:
		print e
		print "ERROR :::: Failed to save Nutrition instance"


	print "Cereal %s was manufactured by %s and has %d calories." % (cereal.name, manufacturer.name, nutrition.calories)
	print "------------------------------------------------------"


#!/usr/bin/python3
"""self exercise practice 2"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print(farm.get("name") + " is a farm in the "+str(farm.get("name"))[0:2] + " and it has the following.")
    for item in farm.get("agriculture"):
         print("  " + item)



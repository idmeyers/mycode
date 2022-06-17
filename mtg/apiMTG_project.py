#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests
import yaml
import crayons
import time
# Define our "base" API
API = "https://labs.alta3.com/demo/switchconfig" # this will never change regardless of the lookup we perform
def delay():
    
    #for second in range(4):
    print(crayons.yellow(".", end=' '))
    time.sleep(.25)

def configSwitch(yamlFile):
    print(crayons.white(f"Connecting to {yamlFile.get('switchname')} via  {yamlFile.get('sshtarget')}"))

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get(API)   # this "f" string reads: API + "sets"
                                        # OR, https://api.magicthegathering.io/v1/sets
    print(resp.text)
    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    configurations = yaml.safe_load(resp.text)
    print(configurations)
    
    for configuration in configurations:
        configSwitch(configuration)
        for second in range(4):
            delay()

    # open a file we write our data into
    #with open("switchconfiguration", "w") as mtgfile:
     #   for cardset in cardsets:  # loop across ALL of the sets of MTG cards (they are stored as dict objects)
      #      print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)  # write the data "we want"
                                                                                    # into mtgfile

if __name__ == "__main__":
    main()

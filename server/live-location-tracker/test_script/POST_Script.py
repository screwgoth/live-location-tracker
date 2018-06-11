import csv
import requests
import time


class TestPostScript(object):
    """
    This is the python script that post  lat and long after every n seconds.
    It takes lat and long from csv and then post it one by one after every n sex.
    """
    filename = "location_path.csv"
    locations_list = []

    @classmethod
    def read_csv(cls):
        f = open(cls.filename, "r+")
        reader = csv.reader(f)
        return reader

    @classmethod
    def create_params(cls, reader_obj):
        """
        This method returns dict with lat and long. It collects lat and long from reader object save it into the dict.
        And that dict we passed as parameter in POST Request
        """
        for row in reader_obj:
            location_dict = dict()
            location_dict["lat"] = row[1]                # Column 1 - Latitude
            location_dict["long"] = row[2]               # Column 2 - Longitude
            location_dict["profile"] = "chetan2"         # We can take it as default profile for testing purpose
            cls.locations_list.append(location_dict)

    @classmethod
    def runit(cls, url):
        reader_obj = cls.read_csv()                      # Read CSV file
        cls.create_params(reader_obj)                    # Save Latitude and Longitude from csv to python dict.
        counter = 1                                      # Skipping Header Row
        while counter != 382:                            # Total 382 Records
            r= requests.post(url=url,                       # Creates POST Request
                             data=(
                                cls.locations_list[counter]
                                  ),
                            )
            print(r)
            time.sleep(3)                               # because we need to create post request in every 10 sec

            counter += 1


t = TestPostScript()
t.runit("http://20.20.5.105:8000/api/v1/location/log/")


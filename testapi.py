import requests

resp = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false") #Call the endpoint
json = resp.json()

class DescriptionError(Exception):
   """Error for Description do not have Plunket """
   pass

class TaglineError(Exception):
   """Error for Tagline do not have well child health services """
   pass

try:
    assert json['Name'] == "Badges"
except:
    print("Name is not Badges")
else:
    print("Name test is OK")

try:
    assert json['CanListClassifieds'] == False
except:
    print("CanListClassifieds is not false")
else:
    print("CanListClassifieds test is OK")


try:

    if "Plunket" in [i['Description'] for i in json["Charities"]]:
        for i in json["Charities"]:
            if i['Description'] == 'Plunket':
                tagline = i["Tagline"]
    else:
        raise DescriptionError

    assert 'well child health services' in tagline
except DescriptionError:
    print("Response does not have a Description named Plunket")
except TaglineError:
    print("The Tagline does not have 'well child health services'")
else:
    print("Charities element test is OK")







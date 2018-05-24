import pycrits
from pycrits.backdoor import Backdoor
from pycrits.vocabulary import CRITsBackdoor

myBackdoor = Backdoor()

myQuery = {
    CRITsBackdoor.NAME:"foo",
    CRITsBackdoor.VERSION:"1.0",
}

results = myBackdoor.objects(query=myQuery)

for result in results:
	print result.get('CRITsBackdoor.ID')
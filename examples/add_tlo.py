import pycrits
from pycrits.backdoor import Backdoor
from pycrits.vocabulary import CRITsBackdoor

myBackdoor = Backdoor()

myParams = {
    CRITsBackdoor.NAME:"foo",
    CRITsBackdoor.SOURCE:"bar",
}

result = myBackdoor.new(params=myParams)

print result
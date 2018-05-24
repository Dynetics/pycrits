from pycrits.backdoor import Backdoor
from pycrits.vocabulary import CRITsBackdoor

myBackdoor = Backdoor()

import datetime
# date must be in the format %Y-%m-%d %H:%M:%S.%f
formatted_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

data = {
    'action' : 'ticket_add',
    'ticket' : {
        'ticket_number' : '11',
        'date': formatted_date,
    }
}

response = myBackdoor.update(id='myIdHere', data=data)

print response
#!/usr/bin/env python
"""

 DBS 3 Client Example.   This script is called 

./dbs3Example.py '/*/*Fall13-POST*/GEN-SIM'

"""

#import  sys,time
from dbs.apis.dbsClient import DbsApi
#from time import gmtime
url="https://cmsweb.cern.ch/dbs/prod/global/DBSReader"
api=DbsApi(url=url)



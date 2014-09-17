#!/usr/bin/env python



'''
HOW TO USE SNMP_HELPER LIBRARY IN PYTHON

Created by Ron Nilekani
'''


IP = 'X.X.X.X'
SNMP_PORT = '161'
COMMUNITY_STRING = 'secret'

# Creating a tuple so that these values dont change.
a_device = (IP, COMMUNITY_STRING, SNMP_PORT)


#Importing the functions from SNMP_HELPER library
from snmp_helper import snmp_get_oid,snmp_extract
'
# This OID maps to System Description on Cisco devices
#http://tools.cisco.com/Support/SNMP/do/BrowseOID.do?objectInput=1.3.6.1.2.1.1.1&translate=Translate&submitValue=SUBMIT&submitClicked=true
OID = '1.3.6.1.2.1.1.1.0'

#Passing the values to the SNMP helper function we exported and storing the results in snmp_data variable
snmp_data = snmp_get_oid(a_device, OID)

print
print "Hexadecimal Format\n"
print snmp_data
print

#SNMP_DATA would have the data in hex format so we need to convert that into human readable format
#Therefore, we use the extract function from snmp_helper library

output = snmp_extract(snmp_data)

print
print "Human Readable Format\n\n"
print output

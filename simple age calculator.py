from datetime import datetime
import time
dob = input("Enter DOB, use dd/mm/yyyy format: ")
dob = datetime.strptime(dob, '%d/%m/%Y')
print("Here are your age statistics...")
time.sleep(2)
print ("Years : %d" % ((datetime.today() - dob).days/365))
print ("Months : %d" % ((datetime.today() - dob).days/30))
print ("Hours : %d" % ((datetime.today() - dob).days*24))
print ("Minutes : %d" % ((datetime.today() - dob).days*1440))
print ("Seconds : %d" % ((datetime.today() - dob).days*86400))
x=input("---------------------------------")
# Download the form sheet in 'csv' format
# Run the python script using python3 with path to sheet and team name
# eg: python3 ./genstat.py forms.csv Machine Learning
# To save it to a file use eg: python3 ./genstat.py forms.csv Machine Learning > ML-Team.txt
import sys
import csv
print('{:^73}'.format(''.join(sys.argv[2:])+" Team"))
print('{:30} \t {:30} \t {:13}'.format("Name","Email","Class/Section"))
with open(sys.argv[1],"rt") as csvfile:
 reader=csv.DictReader(csvfile)
 for row in reader:
  if(row['Which technology have you decided to acquire after reading the Welcome Tutorial?'].find(sys.argv[2])>-1):
   print('{:30} \t {:30} \t {:13}'.format(row['Name'],row['E-Mail ID'],row['Class/Section']))
    

import csv

with open('config.csv', 'w', newline='') as csvfile:
    myWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    myWriter.writerow(['Mat', 500])
    myWriter.writerow(['under15', 1000])
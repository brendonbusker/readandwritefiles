#Import
import csv


#Constants
CUSTFILE = r"D:\CODE\Python\AdvancedPython\readandwritefiles\customers.csv"
NAMECOUNTRYFILE = r"D:\CODE\Python\AdvancedPython\readandwritefiles\customer_country.csv"
#CUSTFILE = "customers.csv"
#NAMECOUNTRYFILE = "customer_country.csv"


#Main
def main():
    infile = open(CUSTFILE, "r", newline = "")
    reader = csv.reader(infile)
    next(reader)

    outfile = open(NAMECOUNTRYFILE, "w", newline = "")
    writer = csv.writer(outfile, delimiter = ",")

    customer_name_country = []

    for row in reader:
        customer_name_country.append(row)

    for i in range(0, len(customer_name_country)):
        last_name = customer_name_country[i][2]
        first_name = customer_name_country[i][1]
        country = customer_name_country[i][4]

        new_row = [first_name, last_name, country]

        writer.writerow(new_row)

    
    infile.close()
    outfile.close()


#Call Main
main()
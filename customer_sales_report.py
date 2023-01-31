#Import
import csv


#Constants
#SALESFILE = r"D:\CODE\Python\AdvancedPython\readandwritefiles\sales.csv"
#SALESREPORTFILE = r"D:\CODE\Python\AdvancedPython\readandwritefiles\salesreport.csv"
SALESFILE = "sales.csv"
SALESREPORTFILE = "salesreport.csv"


#Main
def main():
    infile = open(SALESFILE, "r", newline = "")
    reader = csv.reader(infile)
    next(reader)

    outfile = open(SALESREPORTFILE, "w", newline = "")
    writer = csv.writer(outfile, delimiter = ",")

    sales_list = []
    sales_report_list = []

    for row in reader:
        sales_list.append(row)

    header_row = ["Customer", "Total"]
    writer.writerow(header_row)

    
    for i in range(0, len(sales_list)):
        id = int(sales_list[i][0])
        curr_order_total = float(sales_list[i][3]) + float(sales_list[i][4]) + float(sales_list[i][5])

        new_row = [int(id), float(curr_order_total)]

        sales_report_list.append(new_row)

    curr_id = sales_report_list[0][0]
    total_sales = 0
    sales_report_final = []

    for j in sales_report_list:
        if j[0] == curr_id:
            total_sales += float(j[1])
        
        else:
            sales_report_final.append([curr_id, total_sales])
            curr_id = j[0]
            total_sales = float(j[1])
    
    sales_report_final.append([curr_id, total_sales])
        
    for i in range(0, len(sales_report_final)):
        final_id = sales_report_final[i][0]
        final_total = sales_report_final[i][1]

        final_rows = [final_id, final_total]

        writer.writerow(final_rows)

    infile.close()
    outfile.close()    

#Call Main
main()





            
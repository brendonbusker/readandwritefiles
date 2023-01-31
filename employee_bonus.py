#Import
import csv


#Constants
#EMPLOYEEPAY = r"D:\CODE\Python\AdvancedPython\readandwritefiles\EmployeePay.csv"
EMPLOYEEPAY = "EmployeePay.csv"


#Main
def main():
    infile = open(EMPLOYEEPAY, "r", newline = "")
    reader = csv.reader(infile)
    next(reader)

    employee_pay_list = []

    for row in reader:
        employee_pay_list.append(row)

    print(format("ID", "<2"), format("EmpFName", "<18"), format("EmpLName", "<18"), format("Salary", "<6"), format("Bonus", "<5"))
    print(format("--", "<2"), format("-" * 18, "<18"), format("-" * 18, "<18"), format("------", "<6"), format("-----", "<5"))

    for i in range(0, len(employee_pay_list)):
        print(format(employee_pay_list[i][0], "<2"), format(employee_pay_list[i][1], "<18"), format(employee_pay_list[i][2], "<18"),
            format(employee_pay_list[i][3], "<6"), format(employee_pay_list[i][4], "<5"))

    infile.close()

#Call Main
main()

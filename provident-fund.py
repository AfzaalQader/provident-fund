#Employee provident fund
#basic salary is 35000
#provident fund is 8% / month
#empolyee has worked for 39 months
#anual increment is 15000
#calculate provident fund
provident_fund_rate = round(8/100,2)
provident_fund = 0
total_provident_fund = 0
basic_salary = 35000
for i in range(1,40):
  if i % 12 == 0:
    basic_salary += 15000
  provident_fund = provident_fund_rate * basic_salary
  total_provident_fund += provident_fund
print("Employee provident fund is {}".format(total_provident_fund))

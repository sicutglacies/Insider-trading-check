from cik_match import get_ticker
from form4 import form4


ticker = input('Enter a ticker: ')
cik, name, exchange = get_ticker(ticker)

print('Found ' + name + ' trades on ' + exchange)
data = form4(cik)

for instance in data:
    print('Transaction type: ', instance[0][10:])
    print('Transaction_date:', instance[0][:10])
    print('Reported_date:', instance[1][:10], instance[1][10:])
    print('Company_name:', instance[2])
    print('Ticker:', instance[3])
    print('Insider_name:', instance[4])
    print('Shares_traded:', instance[5])
    print('Average_price:', instance[6])
    print('Total_amount:', instance[7])
    print('Shares_owned:', instance[8])
    print('-'*30)

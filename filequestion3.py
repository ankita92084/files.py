banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
bank=open("banks.html","w")
for bank_name in banks_list:
    bank.write(""+bank_name+"\n")
bank.close()
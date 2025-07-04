# python program
#atm demo code
def cashwithdraw(cur_bal,cur_dep):
    sub=cur_bal-cur_dep
    return sub
  
if __name__== "__main__":
    print("welcome to mogesh cash withdraw system")
    balance=20000
    cash_withdraw=5000
    currentbalance=cashwithdraw(balance,cash_withdraw)
    print(currentbalance)
  

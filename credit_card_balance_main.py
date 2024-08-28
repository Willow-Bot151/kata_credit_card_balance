import math

def credit_card_func(outstanding_balance,yearly_charge,monthly_repay):
    new_outstanding_balance = outstanding_balance
    for i in range(12):
        print(f"Month {i+1}")
        print(new_outstanding_balance)
        min_pay = (math.ceil(new_outstanding_balance * monthly_repay * 100)) / 100
        print(min_pay)
        balance_after_min_pay = round(new_outstanding_balance - min_pay,2)
        print(balance_after_min_pay)
        percent_charge = (math.ceil((yearly_charge/12)*balance_after_min_pay* 100)) / 100
        print(percent_charge)
        new_outstanding_balance = round(balance_after_min_pay + percent_charge,2)
        print(new_outstanding_balance)
        print("\n")
    string_out = f"Outstanding Balance: {new_outstanding_balance:.2f}"
    return string_out
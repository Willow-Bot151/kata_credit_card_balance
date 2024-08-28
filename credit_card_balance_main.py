def credit_card_func(outstanding_balance,yearly_charge,monthly_repay):
    new_outstanding_balance = outstanding_balance
    for i in range(12):
        min_pay = new_outstanding_balance * monthly_repay
        print(min_pay)
        balance_after_min_pay = new_outstanding_balance - min_pay
        print(balance_after_min_pay)
        percent_charge = (yearly_charge/12)*balance_after_min_pay
        print(percent_charge)
        new_outstanding_balance = balance_after_min_pay + percent_charge
        print(new_outstanding_balance)
    string_out = f"Outstanding Balance: {new_outstanding_balance:.2f}"
    return string_out
import pytest
from credit_card_balance_main import credit_card_func

class TestOutputFormat:
    @pytest.mark.it("Test the output string starts with Outstanding Balance.")
    def test_string_format(self):
        assert credit_card_func(0,0,0)[:21] == "Outstanding Balance: "
    @pytest.mark.it("The string ends with a number to two decimal places")
    def test_num_format(self):
        assert credit_card_func(0,0,0)[21:] == "0.00"

class TestRemainingBalanceMath:
    @pytest.mark.skip()
    @pytest.mark.it("The function returns the correct results 1")
    def test_spec_data_verify_1(self):
        assert credit_card_func(3329,0.2,0.03) == "Outstanding Balance: 2816.55"
      
    @pytest.mark.it("The function returns the correct results 2")
    def test_spec_data_verify_2(self):
        assert credit_card_func(341,0.12,0.053) == "Outstanding Balance: 207.63"

    @pytest.mark.skip()    
    @pytest.mark.it("The function returns the correct results 3")
    def test_spec_data_verify_3(self):
        assert credit_card_func(168,0.15,0.06) == "Outstanding Balance: 92.81"
import pytest
import accounting_v3


def test_create_valid_transaction():
    transaction = accounting_v3.Transaction("收入",100,"工资")
    assert transaction.type == "收入"
    assert transaction.amount == 100.0
    assert transaction.note == "工资"



def test_reject_invalid_transaction_type():
    with pytest.raises(ValueError):
        accounting_v3.Transaction("借款", 100, "借款")

@pytest.mark.parametrize("bad_amount", [0, -10])
def test_rejece_non_positive_amount(bad_amount):
    with pytest.raises(ValueError):
        accounting_v3.Transaction("支出",bad_amount," 测试")

def test_empty_ledger_summary():
    ledger = accounting_v3.Ledger()
    assert ledger.summary() =={
        "income":0.0,
        "expense":0.0,
        "balance":0.0,
    }


def test_add_list_trasaction():
    ledger = accounting_v3.Ledger()

    transaction = accounting_v3.Transaction("收入", 100, "工资")

    ledger.add(transaction)

    assert ledger.list() == [transaction]

def test_summary_income_expense_balance():
    ledger = accounting_v3.Ledger()

    ledger.add(accounting_v3.Transaction("收入", 500, "工资"))
    ledger.add(accounting_v3.Transaction("支出", 52.5, "午饭"))
    assert ledger.summary() == {
        "income": 500.0,
        "expense": 52.5,
        "balance": 447.5,
    }

    
def test_reject_non_numeric_amount():
    with pytest.raises(ValueError):
        accounting_v3.Transaction("支出", "abc", "测试")
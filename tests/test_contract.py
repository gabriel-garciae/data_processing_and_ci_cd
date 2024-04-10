from src.contract import Vendas
import pytest
from datetime import datetime
from pydantic import ValidationError

def test_sales_with_valid_data():
    dados_validos = {
        "email": "comprador@example.com",
        "date": datetime.now(),
        "value": 100.51,
        "product": "product x",
        "amount": 3,
        "category": "category3",
    }

    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.date == dados_validos["date"]
    assert venda.value == dados_validos["value"]
    assert venda.product == dados_validos["product"]
    assert venda.amount == dados_validos["amount"]
    assert venda.category == dados_validos["category"]

def test_sales_with_invalid_data():
    dados_invalidos = {
        "email": "comprador",
        "date": "datetime.now()",
        "value": -100.51,
        "product": "",
        "amount": -3,
        "category": "category3",
    }

    with pytest.raises(ValidationError):
            Vendas(**dados_invalidos)

def test_category_validation():
    dados = {
        "email": "comprador@example.com",
        "date": datetime.now(),
        "value": 100.50,
        "product": "Produto Y",
        "amount": 1,
        "category": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)
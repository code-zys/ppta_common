from iso4217 import Currency
from iso4217parse import by_symbol, by_alpha3


class CurrencyHelper:
    @staticmethod
    def get_by_symbol(sign: str) -> Currency | None:
        currency = by_symbol(sign)
        if not currency or not currency[0]:
            return None
        elif sign == '$':
            return Currency.USD
        return Currency(currency[0].alpha3)
    
    @staticmethod
    def get_by_alpha_code(code: str) -> Currency:
        currency = by_alpha3(code)
        return Currency(currency.alpha3)
from enum import Enum


class TransactionType(str,Enum):
    PRODUCTS = "PRODUCTS"
    SERVICES = "SERVICES"
    PRODUCTS_AND_SERVICES = "PRODUCTS_AND_SERVICES"
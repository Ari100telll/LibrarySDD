from services.payment.payment_strategy import PaymentStrategyEnum

PAYMENT_METHOD_STRING_MAX_LEN = max(
    [len(method.value) for method in PaymentStrategyEnum]
)
BASE_PAYMENT_MESSAGE = (
    "[PAYMENT / {method}] The account has been replenished "
    "by UAH {amount} by {user_full_name} ({user_phone_number})"
)

from services.payment.payment_strategy import PaymentStrategyEnum

PAYMENT_METHOD_STRING_MAX_LEN = max(
    [len(method.value) for method in PaymentStrategyEnum] + [len("PROCESSING")]
)

BASE_PAYMENT_MESSAGE = (
    "[PAYMENT / {method}] The account has been replenished "
    "by UAH {amount} by {user_full_name} ({user_phone_number})"
)

PROCESSING_PAYMENT_MESSAGE = (
    f"[PAYMENT / {'PROCESSING'.ljust(PAYMENT_METHOD_STRING_MAX_LEN)}] Started processing "
    f"payment from {{user_phone_number}}"
)

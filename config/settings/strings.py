from services.payment.payment_strategy import PaymentStrategyEnum

PAYMENT_PROCESSING_TEXT = "PROCESSING"

PAYMENT_TAG_STRING_MAX_LEN = max(
    [len(method.value) for method in PaymentStrategyEnum]
    + [len(PAYMENT_PROCESSING_TEXT)]
)

BASE_PAYMENT_MESSAGE = (
    "[PAYMENT / {method}] The account has been replenished "
    "by UAH {amount} by {user_full_name} ({user_phone_number})"
)

PROCESSING_PAYMENT_MESSAGE = (
    f"[PAYMENT / {PAYMENT_PROCESSING_TEXT.ljust(PAYMENT_TAG_STRING_MAX_LEN)}] Started processing "
    f"payment from {{user_phone_number}}"
)

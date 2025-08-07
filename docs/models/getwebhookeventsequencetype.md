# GetWebhookEventSequenceType

If set to `first`, a payment mandate is established right after a payment is made by the customer.

Defaults to `oneoff`, which is a regular payment link and will not establish a mandate after payment.

The mandate ID can be retrieved by making a call to the
[Payment Link Payments Endpoint](get-payment-link-payments).


## Values

| Name     | Value    |
| -------- | -------- |
| `ONEOFF` | oneoff   |
| `FIRST`  | first    |
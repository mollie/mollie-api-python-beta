# ListAllSubscriptionsLocale

Allows you to preset the language to be used in the hosted payment pages shown to the customer. Setting a locale
is highly recommended and will greatly improve your conversion rate. When this parameter is omitted the browser
language will be used instead if supported by the payment method. You can provide any `xx_XX` format ISO 15897
locale, but our hosted payment pages currently only support the specified languages.

For bank transfer payments specifically, the locale will determine the target bank account the customer has to
transfer the money to. We have dedicated bank accounts for Belgium, Germany, and The Netherlands. Having the
customer use a local bank account greatly increases the conversion and speed of payment.


## Values

| Name    | Value   |
| ------- | ------- |
| `EN_US` | en_US   |
| `EN_GB` | en_GB   |
| `NL_NL` | nl_NL   |
| `NL_BE` | nl_BE   |
| `DE_DE` | de_DE   |
| `DE_AT` | de_AT   |
| `DE_CH` | de_CH   |
| `FR_FR` | fr_FR   |
| `FR_BE` | fr_BE   |
| `ES_ES` | es_ES   |
| `CA_ES` | ca_ES   |
| `PT_PT` | pt_PT   |
| `IT_IT` | it_IT   |
| `NB_NO` | nb_NO   |
| `SV_SE` | sv_SE   |
| `FI_FI` | fi_FI   |
| `DA_DK` | da_DK   |
| `IS_IS` | is_IS   |
| `HU_HU` | hu_HU   |
| `PL_PL` | pl_PL   |
| `LV_LV` | lv_LV   |
| `LT_LT` | lt_LT   |
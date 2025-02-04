<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

async def main():
    async with Mollie(
        security=mollie_api_python_beta.Security(
            api_key=os.getenv("MOLLIE_API_KEY", ""),
        ),
    ) as mollie:

        res = await mollie.balances.list_async(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->
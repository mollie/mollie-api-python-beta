<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import mollie
from mollie import Client
import os

async def main():

    async with Client(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client:

        res = await client.balances.list_async(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->
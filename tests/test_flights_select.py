from httpx import AsyncClient
import pytest

from flights.models import Flights


@pytest.mark.asyncio
async def test_get_flights(ac: AsyncClient):

    response = await ac.get("/flights/", params={
        "depdate": "2022-11-29",
    })

    assert response.status_code == 200
   
    
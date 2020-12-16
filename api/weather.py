from models.umbrella_status import UmbrellaStatus
from models.location import Location
import fastapi
import httpx

router = fastapi.APIRouter()


@router.get('/api/umbrella', response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    url = f"https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}"
    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        res.raise_for_status()

        data = res.json()

        weather = data.get("weather", {})
        forecast = data.get("forecast", {})

        cat = weather.get("category", "UNKNOWN")
        temp = forecast.get('temp', 0.0)

        bring = cat.lower().strip() in {'rain', 'mist'}

        print("*****************:::")
        print(temp)
    return UmbrellaStatus(bring_umbrella=bring, temp=temp)

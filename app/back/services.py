import httpx
from config import settings
import json

async def check_imei(imei: str) -> dict:
    '''
    Отправляет запрос к API imeicheck.net для проверки устройства по IMEI.
    '''
    url = 'https://api.imeicheck.net/v1/checks'
    
    payload = json.dumps({
        "deviceId": imei,  
        "serviceId": 1     
    })
    
    headers = {
        'Authorization': f'Bearer {settings.IMEI_SANDBOX_TOKEN}', 
        'Accept-Language': 'en',
        'Content-Type': 'application/json' 
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=payload)
        
        if response.status_code == 200:
            return response.json() 
        else:
            return {"error": f"Failed to fetch data: {response.status_code}", "message": response.text}

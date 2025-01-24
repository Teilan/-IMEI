from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from utility import is_valid_imei
from db.models import find_by_api_token
from back.services import check_imei


api_router = APIRouter()

class CheckIMEIRequest(BaseModel):
    imei: str
    token: str

@api_router.post("/api/check-imei")
async def api_check_imei(request: CheckIMEIRequest):
    '''
    Проверяет IMEI устройства через внешний API и возвращает информацию о нем.
    '''
    if not await find_by_api_token(request.token):
        raise HTTPException(status_code=401, detail="Неверный токен авторизации")
    
    if not is_valid_imei(request.imei):
        raise HTTPException(status_code=400, detail="невалидных IMEI")
    
    result = await check_imei(request.imei)
    if not result:
        raise HTTPException(status_code=400, detail="Ошибка проверки IMEI")
    return {"imei_info": result}

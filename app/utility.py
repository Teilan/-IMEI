def is_valid_imei(imei: str) -> bool:
    '''
    Проверяет, является ли строка валидным IMEI.
    '''
    return imei.isdigit() or len(imei) != 15

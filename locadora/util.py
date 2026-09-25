import datetime

def str_to_datetime(data: str):
    formato = "%d/%m/%Y %H:%M"
    obj = datetime.datetime.strptime(data, formato)
    return obj

def datetime_to_str(data) -> str:
    formato = "%d/%m/%Y %H:%M"
    obj = data.strftime(formato)
    return obj

if __name__ == "__main__":
    agora = datetime.datetime.now()
    o = datetime_to_str(agora)
    print(o)

    data_str = '22/09/2026 22:00'
    o = str_to_datetime(data_str)
    print(o.totalseconds())


import requests
class praytime:
    def timepray(city):
        javob=''
        
        url=f"https://islomapi.uz/api/present/day?region={city}"
        r=requests.get(url)

        res=r.json()
        javob+=f"📆Sana: {res['date']}\n"
        javob+=f"📌Kun: {res['weekday']}\n"
        javob+=f"📍Hudud: {res['region']}\n\n"
        javob+=f"Bomdod(🕌Azon): {res['times']['tong_saharlik']}\n"
        javob+=f"Quyosh chiqishi: {res['times']['quyosh']}\n"
        javob+=f"Peshin: {res['times']['peshin']}\n"
        javob+=f"Asr: {res['times']['asr']}\n"
        javob+=f"Shom: {res['times']['shom_iftor']}\n"
        javob+=f"Hufton: {res['times']['hufton']}\n"
        javob+="\n\n@Namoz_vaqtlari_taqvim_bot"
        return javob
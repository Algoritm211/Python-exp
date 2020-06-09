import COVID19Py
from pprint import pprint

covid19 = COVID19Py.COVID19()

pprint(covid19.getLocationByCountryCode('RU'))

class InfoCountry:

    def __init__(self, country_code):

        self.country_code = country_code

    def get_info(self):
        info = covid19.getLocationByCountryCode(self.country_code)
        date = info[0]['last_updated'].split('T')[0]
        time = info[0]['last_updated'].split('T')[1][0:8:]
        text = '<b>Информация по стране</b>' + '<b>' + str(info[0]['country']) + '</b>\n\n' + \
                '<i>Население страны: </i>' + str(info[0]['country_population']) + '\n' +\
                '<i>Подтвержденные случаи заражения: </i>' + str(info[0]['latest']['confirmed']) + '\n' +\
                '<i>Всего зарегистрировано смертей: </i>' + str(info[0]['latest']['deaths']) + '\n\n' +\
                '<b>Данные от </b>' + '<b>' + date + ' ' +time + '</b>'

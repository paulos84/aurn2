from datetime import datetime, timedelta
from dateutil import parser
import pytz

local_tz = pytz.timezone('Europe/London')


def hourly_data(soup, site):
    """ extract values from the html table row into a dictionary """
    if soup.find_all('a', string=site):
        site_link = soup.find_all('a', string=site)[0]
        row = site_link.findParent('td').findParent('tr').findAll('td')
        o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
        no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
        so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
        pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
        pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
        hour = row[6].text[:10] + ' ' + row[6].text[10:]
        try:
            dt = parser.parse(hour)
        # expect ValueError for times containing '24:00'
        except ValueError:
            time = hour.replace('24:00', '00:00')
            dt = datetime.strptime(time, "%d/%m/%Y %H:%M")
            dt += timedelta(days=1)
        return {'o3': o3, 'no2': no2, 'so2': so2, 'pm25': pm25, 'pm10': pm10, 'time': local_tz.localize(dt)}


def validate_data(data_dict):
    """ ensure that stale data is not recorded """
    current_hour = datetime.now(local_tz).replace(microsecond=0, second=0, minute=0)
    if data_dict['time'] != current_hour:
        na_values = ['n/a'] * 5 + [current_hour]
        return dict(zip(['o3', 'no2', 'so2', 'pm25', 'pm10', 'time'], na_values))
    else:
        return data_dict

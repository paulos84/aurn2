from datetime import datetime, timezone, timedelta
from datetime import datetime


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
        time = row[6].text[:10] + ' ' + row[6].text[10:]
        return {'o3': o3, 'no2': no2, 'so2': so2, 'pm25': pm25, 'pm10': pm10, 'time': time}


def validate_data(data_dict):
    """ ensure that stale data is not recorded """
    hour_dt = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)
    current_hour = datetime.strftime(hour_dt, "%d/%m/%Y %H:%M")
    if data_dict and data_dict['time'] != current_hour:
        na_values = ['n/a'] * 5 + [current_hour]
        return dict(zip(['o3', 'no2', 'so2', 'pm25', 'pm10', 'time'], na_values))
    else:
        return data_dict
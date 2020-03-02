import requests


def get_lat_lng(apiKey, address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), apiKey))
    print(url)
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng


if __name__ == '__main__':
    # get key
    apiKey = 'AIzaSyB-wmFf8_Orjq5yvvW8GqQ9mWsRjdpxpbs'

    # get coordinates
    address = 'paris'
    lat, lng = get_lat_lng(apiKey, address)
    print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(address, lat, lng))
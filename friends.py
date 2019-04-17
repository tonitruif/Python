import requests
import datetime
import collections



def calc_age(uid):
    payload = {'v': '5.71', 'access_token': '24d9ce2224d9ce2224d9ce228d24b3c77f224d924d9ce22786ed240e40619ae8d9de2c5', 'user_ids': uid}
    r = requests.get('https://api.vk.com/method/users.get', params=payload)
    response = r.json()
    response = response.pop('response')
    user_id = response[0].pop('id')

    payload = {'v': '5.71', 'access_token': '24d9ce2224d9ce2224d9ce228d24b3c77f224d924d9ce22786ed240e40619ae8d9de2c5',
               'user_id': user_id,  'fields': 'bdate'}
    r = requests.get('https://api.vk.com/method/friends.get', params=payload)

    response = r.json()
    response = response.pop('response')
    count = response.pop('count')
    dates = []
    for dictionary in response['items']:
        try:
            if len(dictionary['bdate']) > 5:
                dates.append((dictionary['bdate']))
        except KeyError:
            pass

    now = datetime.datetime.now()
    now = now.year
    age = []
    for date in dates:
        age.append(now - int(date[-4::]))
    pass
    ageDict = dict((x, age.count(x)) for x in set(age))
    ageDict = sorted(ageDict.items(), key=lambda v: (v[1], -v[0]), reverse=True)
    return ageDict

if __name__ == '__main__':
    res = calc_age('tonitrui')
    print(res)

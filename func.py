import requests
import os

def random_value():
    req = requests.get('https://www.random.org/integers/?num=1&min=1&max=2&col=1&base=10&format=plain&rnd=new')
    if req.status_code != 200:
        return None
    else:
        return int(req.text)

def pedro_isa():
    with open('ultimo.txt', 'r') as fp:
        nome = fp.readline()
        if 'pedro' in nome:
            nome = 'isa'
            result = {'pedro': 1, 'isa': 2}
        elif 'isa' in nome:
            nome = 'pedro'
            result = {'pedro': 2, 'isa': 1}
        else:
            return None
    with open('ultimo.txt', 'w') as fp:
        fp.write(nome)
    return result

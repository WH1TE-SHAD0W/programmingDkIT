from grades import max_value
from random import uniform
from random import randint

def generate_random_list():
    random_list = []
    for i in range(randint(40,60)):
        random_list.append(uniform(0,100))
    return random_list

def test_max_value():
    data = generate_random_list()
    assert max_value(data) == max(data)
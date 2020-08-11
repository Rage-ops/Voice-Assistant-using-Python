import requests
import json


def data_muse_request(param):  # returns up to first three words from the result
    param['max'] = 4
    res = requests.get("https://api.datamuse.com/words", params=param)
    parsed = json.loads(res.text)
    res = [dict_word['word'] for dict_word in parsed]
    return res


def mean_like(word):  # returns words with a meaning similar to the given word
    return data_muse_request(param={"ml": word})


def sound_like(word):  # returns words that sound like the given word
    return data_muse_request(param={"sl": word})


def spelled_like(word):  # words that are spelled similarly to the given word
    return data_muse_request(param={"sp": word})


def rhyme_like(word):  # returns words that rhyme with the given word
    return data_muse_request(param={"rel_rhy": word})


def adjective(word):  # returns adjectives that are often used to describe given word
    return data_muse_request(param={"rel_jjb": word})

import pickle
import requests
from string import printable
from logging import info
# i know it's dirty, but i am too lazy :P
ELF_DICT = {}

def export_dict()->str:
    '''
    save by json is a bad idea, let's use pickle instead :D
    '''
    return pickle.dumps(ELF_DICT).hex()

def load_dict(s:str):
    '''
    save by json is a bad idea, let's use pickle instead :D
    '''
    global ELF_DICT
    ELF_DICT = pickle.loads(bytes.fromhex(s))

def reset():
    '''
    prevent sb destroy my bot
    '''
    global ELF_DICT
    ELF_DICT = {}

def query(sentense:str)->str:
    '''
    translate word by word
    '''
    res = ""

    for i in sentense:
        # elf does not contains ascii words
        if i in printable:
            res += i
        else:
            res += query_single_word(i)
    return res

def query_single_word(txt:str)->str:
    '''
    check if word exsist in database
    '''
    global ELF_DICT
    if txt not in ELF_DICT:
        with requests.get(f"https://www.moedict.tw/uni/{txt}") as resp:
            if resp.status_code == 200:
                info(f'got {txt} query result :{resp.json()["heteronyms"][0]["bopomofo"]}')
                ELF_DICT.update({txt:resp.json()["heteronyms"][0]["bopomofo"].replace("（語音）", "")[0]})
            elif resp.status_code == 404:
                #raise ValueError(f"can not translate such word {txt}")
                ELF_DICT.update({txt:txt})
            else:
                raise Exception("wtf")
    return ELF_DICT[txt]
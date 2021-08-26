# This is mooncakes stock monitor for amazingorintal.nl
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from push import pushmessageHNV

def chechkmooncake():
    with urlopen('https://www.orientalwebshop.nl/zh/mooncakes') as response:
       html = str(response.read(), 'utf-8')

    obj = bf(html, 'html.parser')
    items = obj.find_all(class_= "product-name")
    itemlist = []
    for item in items:
        itemlist.append(item.find('a')['title'])
    #print (itemlist)

    #DefaultItemList = ['广州酒家 利口福 凤梨馅 500克 / Likofu Pineapple Mash 500g', '广州酒家 利口福 绿茶馅 500克 / Likofu Green Tea Mash 500g', '广州酒家 利口福 绿豆沙馅 500克 / Likofu Mung Bean Paste 500g', '广州酒家 利口福 芋蓉馅 500克 / Likofu Taro Paste 500g', '广州酒家 利口福 黑芝麻馅 500克 / Likofu Black Sesame Paste 500g', '日威 七星伴月 810g / Riwei Seven Stars Mooncake Gift Box (5 Flavours) 810g', '日威 五仁月饼 720克 / Riwei Mooncake Mixed Nuts 720g', '日威 纯正白莲蓉月饼 720g / Riwei Mooncake White Lotus Paste 720g', '日威 绿茶味双黄月饼 4件 720g / Riwei Mooncake Double Yolks Green Tea 720g', '日威 迷你月饼 合家团圆 540克 / Riwei Mini Mooncake Mix (3 Flavours) 540g', '美心冰皮 抹茶红豆月饼 2x60g / Hong Kong MX Snowy Twin Pack Green Tea & Red Bean 2x60g', '美心冰皮 红豆冰味月饼 2x60g / Hong Kong MX Snowy Twin Pack Red Bean Iced Drink 2x60g', '香港美心 丰年美月礼盒月饼 6x70克 / Hong Kong MX Harvest Moon Assorted Mooncake 6x70g', '香港美心 猫山王榴莲冰皮礼盒 (6x60g) 360克 / Hong Kong MX Snowy Musang King Durian Gift Box 6x60g 360g', '香港美心七星伴明月月饼 (6 Flavours) 1350g / Hong Kong MX Premium Assorted Mooncakes Gift Pack (6 Flavours) 1350g', '香港美心低糖蛋黄白莲蓉月饼 (6x90g) 540g / Hong Kong MX Low Sugar White Lotus Seed Paste Mooncake with Egg Yolk with Sweetener (6x90g) 540g', '香港美心冰皮二人世界 杨枝甘露 120克 / Hong Kong MX Snowy Twin Pack Mango With Pomelo Dessert', '香港美心冰皮二人世界 芒果脆脆月饼 2x60g / Hong Kong MX Snowy Twin Pack Mango Crunch (2x60g) 120g', '香港美心冰皮二人世界 香甜芒果 (2x60g) 120g / Hong Kong MX Snowy Twin Pack Mango', '香港美心精装八宝礼盒月饼 (8 Flavours) 675g / Hong Kong MX Mooncake Exclusive Selection (8 Flavours) 675g', '香港美心芒果栗子冰皮月饼 120克 / Hong Kong MX Snowy Twin Pack Mango Chestnut', '香港美心迷你版月饼 (2x70g) 140g / Hong Kong MX Mini Assorted Mooncakes (2x70g) 140g', '香港美心限量版月饼 (6 Flavours) 730g / Hong Kong MX Mooncake Limited Edition']

    #日威纯正白莲蓉没了
    DefaultItemList = ['广州酒家 利口福 凤梨馅 500克 / Likofu Pineapple Mash 500g', '广州酒家 利口福 绿茶馅 500克 / Likofu Green Tea Mash 500g', '广州酒家 利口福 绿豆沙馅 500克 / Likofu Mung Bean Paste 500g', '广州酒家 利口福 芋蓉馅 500克 / Likofu Taro Paste 500g', '广州酒家 利口福 黑芝麻馅 500克 / Likofu Black Sesame Paste 500g', '日威 七星伴月 810g / Riwei Seven Stars Mooncake Gift Box (5 Flavours) 810g', '日威 五仁月饼 720克 / Riwei Mooncake Mixed Nuts 720g', '日威 绿茶味双黄月饼 4件 720g / Riwei Mooncake Double Yolks Green Tea 720g', '日威 迷你月饼 合家团圆 540克 / Riwei Mini Mooncake Mix (3 Flavours) 540g', '美心冰皮 抹茶红豆月饼 2x60g / Hong Kong MX Snowy Twin Pack Green Tea & Red Bean 2x60g', '美心冰皮 红豆冰味月饼 2x60g / Hong Kong MX Snowy Twin Pack Red Bean Iced Drink 2x60g', '香港美心 丰年美月礼盒月饼 6x70克 / Hong Kong MX Harvest Moon Assorted Mooncake 6x70g', '香港美心 猫山王榴莲冰皮礼盒 (6x60g) 360克 / Hong Kong MX Snowy Musang King Durian Gift Box 6x60g 360g', '香港美心七星伴明月月饼 (6 Flavours) 1350g / Hong Kong MX Premium Assorted Mooncakes Gift Pack (6 Flavours) 1350g', '香港美心低糖蛋黄白莲蓉月饼 (6x90g) 540g / Hong Kong MX Low Sugar White Lotus Seed Paste Mooncake with Egg Yolk with Sweetener (6x90g) 540g', '香港美心冰皮二人世界 杨枝甘露 120克 / Hong Kong MX Snowy Twin Pack Mango With Pomelo Dessert', '香港美心冰皮二人世界 芒果脆脆月饼 2x60g / Hong Kong MX Snowy Twin Pack Mango Crunch (2x60g) 120g', '香港美心冰皮二人世界 香甜芒果 (2x60g) 120g / Hong Kong MX Snowy Twin Pack Mango', '香港美心精装八宝礼盒月饼 (8 Flavours) 675g / Hong Kong MX Mooncake Exclusive Selection (8 Flavours) 675g', '香港美心芒果栗子冰皮月饼 120克 / Hong Kong MX Snowy Twin Pack Mango Chestnut', '香港美心迷你版月饼 (2x70g) 140g / Hong Kong MX Mini Assorted Mooncakes (2x70g) 140g', '香港美心限量版月饼 (6 Flavours) 730g / Hong Kong MX Mooncake Limited Edition']


    curquantity = len(itemlist)
    print(f"\nNow they are providing {curquantity} kinds of mooncakes\n============================================")
    #pushmessageHNV(f"没有新月饼")

    if curquantity != 22:
        if curquantity < 22:
            changeditem = set(DefaultItemList) - set(itemlist)
            pushmessageHNV(f"有月饼下架啦, 下架的月饼有{changeditem}")
        if curquantity > 22:
            changeditem = set(itemlist) - set(DefaultItemList)
            pushmessageHNV(f"有月饼上架啦, 新上的月饼有{changeditem}")


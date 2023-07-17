import requests
import json
from ticket import add_ticket

sc = add_ticket.getData_yaml('Cookie')
token = add_ticket.getData_yaml('xfk-login-token')

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'gr_user_id=0e146762-f7aa-4223-b0f1-76b5716ea990; grwng_uid=406f2fd5-b128-4675-b021-223575b24269; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228645%22%2C%22first_id%22%3A%221762283e6da842-0e916b57114ded-52102b70-304500-1762283e6dbb19%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221762283e6da842-0e916b57114ded-52102b70-304500-1762283e6dbb19%22%7D; b41e88d01ddb041c_gr_last_sent_cs1=8645; JSESSIONID=ae46827c-5ac7-4c68-b4bf-c293d8a03da7; b41e88d01ddb041c_gr_cs1=8645',
    'Cookie': sc,
    'xfk-login-token': token

}
goodsID_list = [777786, 777787, 777788, 777789, 777790, 777791, 777792, 777796, 777797, 777815, 777816, 777817,
                777818, 777819, 777820, 777821, 777822, 777823, 777824, 777825, 777826, 777827, 777828,
                777829, 777830,
                777831]

good_list = [729, 733, 734, 735, 742, 744, 748, 754, 755, 760, 772, 891, 892, 1752, 2032, 777779, 777780, 777781,
             777782,
             777784, 777834, 741, 743, 41, 42, 43, 44, 45, 46, 47, 48, 49, 239, 641, 646, 647, 648, 650, 651, 652, 653,
             655,
             656, 657, 658, 660, 661, 662, 663, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678,
             679,
             680, 681, 682, 683, 684, 685, 686, 687, 689, 692, 693, 694, 695, 696, 697, 698, 699, 701, 702, 703, 704,
             705,
             706, 707, 708, 709, 712, 713, 714, 715, 716, 720, 724, 764, 893, 749, 774, 894, 906, 761, 1885, 762, 767,
             768,
             769, 770, 895, 896, 898, 928, 1129, 1152, 912, 913, 914, 915, 918, 952, 953, 954, 1075, 1076, 1077, 1078,
             1080,
             1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1102,
             1103, 1104, 1105, 1106, 1120, 1121, 1131, 1130, 1149, 930, 1151, 908, 909, 910, 1146, 925, 926, 723, 725,
             726,
             727, 728, 730, 924, 904, 949, 1147, 1160, 1162, 1168, 1240, 1241, 1243, 1244, 1245, 1252, 1253, 1262, 1263,
             1271, 1273, 1274, 1778, 1779, 1798, 1799, 1801, 1803, 1805, 1807, 1808, 1809, 1810, 1817, 1819, 1821, 1823,
             1825, 1828, 1830, 1832, 1835, 1837, 1839, 1841, 1843, 1845, 1848, 1850, 1857, 1861, 1872, 1878, 1887, 1894,
             1898, 1900, 7248, 7259, 7260, 7261, 7301, 777810, 777813]


def saveOrUpdate():
    # 增加门店
    shop_url = 'http://xfkadtestb.xfanka.com/mgr/shop/saveOrUpdate'
    data = {"type": "0", "hasshopid": "false", "entId": 197017, "name": "商户TTTTT门店", "shopType": "0",
            "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/huachunxue-1607670479545.jpg",
            "canCashout": 1, "label": "门店标签", "cityId": 130100, "countyId": 130105,
            "address": "河北省石家庄市裕华区昆仑南大街与淮河道交口西北260米", "mobile": "13122222222", "content": "<p>商户TTTTT门店详情</p>",
            "sharePosterUrl": "", "longitude": 114.618077, "latitude": 38.041553, "categoryId": 33, "shopCatId": 8,
            "shopCbdId": 9, "personAverageConsumption": "55", "score": 5, "shopTime": "营业时间", "picList": []}

    r = requests.post(url=shop_url, data=json.dumps(data), headers=headers)
    print(r.json())


def saveBase():
    # 商品基础信息
    goods_url = 'http://xfkadtestb.xfanka.com/mgr/goods/saveBase'
    alphabet = 'A1'
    for i in alphabet:
        data = {"name": "西双版纳商品" + str(i), "catId": "", "goodShortName": "西双版纳商品" + str(i), "price": "55",
                "originalPrice": "66",
                "payShopPrice": "44", "shopIds": "123320625", "type": 1, "useTimes": 0, "isLimitTime": 0,
                "noTimeContent": "西双版纳商品" + str(i) + "不可用日期", "timeContent": "西双版纳商品" + str(i) + "使用时间",
                "autoRefund": 0, "categoryId": 33,
                "hotCats": [1], "appointment": 1, "isAutoOffLine": 0, "offLineTime": "", "isLimitSnap": 0,
                "snapTime": "2020-12-31 00:00:00", "appointmentRemark": "西双版纳商品" + str(i) + "需要预约",
                "shopId": "123320625"}

        r = requests.post(url=goods_url, data=json.dumps(data), headers=headers)
        print(r.json())


def saveAndUpdatePic():
    '''商品图册'''
    saveAndUpdatePic_url = 'http://xfkadtestb.xfanka.com/mgr/goods/saveAndUpdatePic'

    for i in goodsID_list:
        data = {"id": i, "coverPic": "null",
                "videoUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000630477.jpg",
                "bigPicUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000527955.jpg",
                "picList": [""], "goodsPicList": [{"file": {}, "picName": "dd", "key": "16080005372810", "status": 1,
                                                   "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000537745.jpg?x-oss-process=image/crop,x_25,y_0,w_750,h_600/resize,m_fixed,w_750,h_600,limit_0"},
                                                  {"file": {}, "picName": "a", "key": "16080006054480", "status": 1,
                                                   "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000605840.jpg?x-oss-process=image/crop,x_28,y_0,w_594,h_475/resize,m_fixed,w_750,h_600,limit_0"},
                                                  {"file": {}, "picName": "oo", "key": "16080006113070", "status": 1,
                                                   "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000611778.jpg?x-oss-process=image/crop,x_40,y_0,w_400,h_320/resize,m_fixed,w_750,h_600,limit_0"},
                                                  {"file": {}, "picName": "cc", "key": "16080006175170", "status": 1,
                                                   "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000617981.jpg?x-oss-process=image/crop,x_25,y_0,w_750,h_600/resize,m_fixed,w_750,h_600,limit_0"},
                                                  {"file": {}, "picName": "aa", "key": "16080006226470", "status": 1,
                                                   "picUrl": "https://minifankatest.oss-cn-beijing.aliyuncs.com/gallery/shanqingshuixiu-1608000623227.jpg?x-oss-process=image/crop,x_25,y_0,w_750,h_600/resize,m_fixed,w_750,h_600,limit_0"}]}
        r = requests.post(url=saveAndUpdatePic_url, data=json.dumps(data), headers=headers)
        print(r.json())


def saveAndUpdateBaseOtherInfo():
    '''商品其他信息'''
    saveAndUpdateBaseOtherInfo_url = 'http://xfkadtestb.xfanka.com/mgr/goods/saveAndUpdateBaseOtherInfo'
    for i in goodsID_list:
        data = {"id": i, "confineCount": 5000, "confineCount1": 0, "perUserLimit": 0, "sort": 1000,
                "orderByStatus": "1", "goodsOrder": 10000, "biaoqian": "促销语", "purchaseNeeds": "购买须知",
                "packageIncludes": "套餐包含", "goodLongName": "商品分享语：", "soldFakeBase": 0, "isShowSalenum": 0,
                "isShowConfine": 0, "isLimitNew": 0}
        r = requests.post(url=saveAndUpdateBaseOtherInfo_url, data=json.dumps(data), headers=headers)
        print(r.json())


def saveAndUpdateDetail():
    '''图文详情'''
    saveAndUpdateDetail_url = 'http://xfkadtestb.xfanka.com/mgr/goods/saveAndUpdateDetail'
    for i in goodsID_list:
        data = {"id": i, "detail": "<p>2020-12-15</p>", "isTemplate": 0}
        r = requests.post(url=saveAndUpdateDetail_url, data=json.dumps(data), headers=headers)
        print(r.json())


def goodsZeroUp():
    '''上架'''
    goodsZeroUp_url = 'http://xfkadtestb.xfanka.com/mgr/goods/goodsZeroUp/'
    for i in good_list:
        r = requests.post(url=goodsZeroUp_url + str(i), headers=headers)
        print(r.json())


def goodsZeroDown():
    '''下架'''
    goodsZeroDown_url = 'http://xfkadtestb.xfanka.com/mgr/goods/goodsZeroDown/'
    for i in good_list:
        r = requests.get(url=goodsZeroDown_url + str(i), headers=headers)
        print(r.json())


if __name__ == '__main__':
    # 商品基础信息
    # saveBase()
    # 商品图册
    # saveAndUpdatePic()
    # 其他信息
    # saveAndUpdateBaseOtherInfo()
    # 图文详情
    # saveAndUpdateDetail()
    # 商品上架
    # goodsZeroUp()
    # 商品下架
    # goodsZeroDown()
    pass

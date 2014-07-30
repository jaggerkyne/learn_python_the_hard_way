# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


provinces = {
    u"河北省":u"冀",
    u"山西省":u"晋",
    u"辽宁省":u"辽",
    u"吉林省":u"吉",
    u"黑龙江省":u"黑",
    u"江苏省":u"苏",
    u"浙江省":u"浙", 
    u"安徽省":u"皖",
    u"福建省":u"闽",
    u"江西省":u"赣",
    u"山东省":u"鲁",
    u"河南省":u"豫",
    u"湖北省":u"鄂",
    u"湖南省":u"湘",
    u"广东省":u"粤",
    u"海南省":u"琼",
    u"四川省":u"川",
    u"贵州省":u"黔",
    u"云南省":u"滇",
    u"陕西省":u"陕",
    u"甘肃省":u"甘",
    u"青海省":u"青",
    u"北京市":u"京",
    u"天津市":u"津",
    u"上海市":u"申",
    u"重庆市":u"渝",
    u"台湾省":u"台",
}

print "*" * 180

for province, abv in provinces.items():
    print u"%s的缩写是%s。" %(province,abv)

cities = {
    u"粤":[
        u"广州市",
        u"深圳市",
        u"珠海市",
        u"汕头市",
        u"韶关市",
        u"佛山市",
        u"江门市",
        u"湛江市",
        u"茂名市",
        u"肇庆市",
        u"惠州市",
        u"梅州市",
        u"汕尾市",
        u"河源市",
        u"阳江市",
        u"清远市",
        u"东莞市",
        u"中山市",
        u"潮州市",
        u"揭阳市",
        u"云浮市"],

    u"桂":[
        u"梧州",
        u"桂林"
    ]
}
print "*" * 180
for abv, city in cities.items():
    cities = ''
    for c in city:
        cities += c +','
    print u"%s有这些城市：%s" % (abv,cities)

districts = {

    u"广州市": [
        u"越秀区",
        u"海珠区",
        u"荔湾区",
        u"天河区",
        u"白云区（景泰街道）",
        u"黄埔区",
        u"花都区（新华街道）",
        u"番禺区（市桥街道）",
        u"南沙区（黄阁镇）",
        u"萝岗区（夏港街道）",
        u"从化市（街口街道）",
        u"增城市（荔城街道）"],

    u"深圳市":[
        u"福田区",
        u"罗湖区",
        u"南山区",
        u"宝安区（新安街道）",
        u"龙岗区（龙岗街道）",
        u"盐田区（盐田街道）"],

    u"珠海市":[
        u"香洲区",
        u"斗门区（井岸镇）",
        u"金湾区（三灶镇）"],

    u"汕头市":[
        u"金平区",
        u"龙湖区",
        u"濠江区",
        u"澄海区（凤翔街道）",
        u"潮阳区（文光街道）",
        u"潮南区（峡山街道）",
        u"南澳县（后宅镇）"],

    u"韶关市":[
        u"浈江区",
        u"武江区",
        u"曲江区（马坝镇）",
        u"乐昌市（乐城街道",
        u"南雄市（雄州镇）",
        u"仁化县（仁化镇）",
        u"始兴县（太平镇）",
        u"翁源县（龙仙镇）",
        u"新丰县（丰城镇）",
        u"乳源瑶族自治县（乳城镇）"],

    u"佛山市":[
        u"禅城区",
        u"南海区（桂城街道）",
        u"顺德区（大良街道）",
        u"三水区（西南街道）",
        u"高明区（荷城街道）"],

    u"江门市":[
        u"江海区",
        u"蓬江区",
        u"新会区（会城街道）",
        u"台山市（台城镇）",
        u"开平市（长沙街道）",
        u"鹤山市（沙坪镇）",
        u"恩平市（恩城街道）"],

    u"湛江市":[
        u"赤坎区",
        u"霞山区",
        u"坡头区",
        u"麻章区",
        u"廉江市（罗州街道）",
        u"雷州市（雷城街道）",
        u"吴川市（梅菉街道）",
        u"遂溪县（遂城镇）",
        u"徐闻县（徐城镇）"],

    u"茂名市":[
        u"茂南区",
        u"茂港区（南海街道）",
        u"高州市（中山街道）",
        u"化州市（河西街道）",
        u"信宜市（东镇镇）",
        u"电白县（水东镇）"],

    u"肇庆市":[
        u"端州区",
        u"鼎湖区（坑口街道）",
        u"高要市（南岸街道）",
        u"四会市（东城街道）",
        u"广宁县（南街镇）",
        u"德庆县（德城街道）",
        u" 封开县（江口镇）",
        u"怀集县（怀城镇）"],

    u"惠州市":[
        u"惠城区",
        u"惠阳区（淡水街道）",
        u"惠东县（平山镇）",
        u"博罗县（罗阳镇）",
        u"龙门县（龙城街道）"],

    u"梅州市":[
        u"梅江区",
        u"兴宁市",
        u"梅县（程江镇）",
        u"蕉岭县（蕉城镇）",
        u"大埔县（湖寮镇）",
        u"丰顺县（汤坑镇）",
        u"五华县（水寨镇）",
        u"平远县（大柘镇）"],

    u"汕尾市":[
        u"陆丰市（东城镇）",
        u"海丰县（海城镇）",
        u"陆河县（河田镇）"],

    u"河源市":[
        u"源城区",
        u"和平县（阳明镇）",
        u"龙川县（老隆镇）",
        u"紫金县（紫城镇）",
        u"连平县（元善镇）",
        u"东源县（仙塘镇）"],

    u"阳江市":[
        u"江城区",
        u"阳春市（春城街道）",
        u"阳西县（织篢镇）",
        u"阳东县（东城镇）"],

    u"清远市":[
        u"清城区（凤城街道）",
        u"英德市（英城街道）",
        u"连州市（连州镇）",
        u"佛冈县（石角镇）",
        u"阳山县（阳城镇）",
        u"清新县（太和镇）",
        u"连山壮族瑶族自治县（吉田镇）",
        u"连南瑶族自治县（三江镇）"],

    u"东莞市":[
        u"莞城区",
        u"东城区",
        u"南城区",
        u"万江区四个区（大市区）",
        u"中堂镇",
        u"高埗镇",
        u"麻涌镇",
        u"沙田镇",
        u"虎门镇",
        u"厚街镇",
        u"寮步镇",
        u"长安镇",
        u"常平镇",
        u"石碣镇",
        u"石排镇",
        u"石龙镇",
        u"企石镇",
        u"横沥镇",
        u"塘厦镇",
        u"清溪镇",
        u"凤岗镇",
        u"谢岗镇",
        u"桥头镇",
        u"洪梅镇",
        u"道滘镇",
        u"东坑镇",
        u"黄江镇",
        u"大朗镇",
        u"望牛墩镇",
        u"大岭山镇",
        u"樟木头镇"],


    u"中山市":[
        u"东区",
        u"南区（环城）",
        u"西区",
        u"北区（石岐区）",
        u"火炬区（中山港）",
        u"港口镇",
        u"三角镇",
        u"民众镇",
        u"南蓢镇",
        u"三乡镇",
        u"坦洲镇",
        u"神湾镇",
        u"板芙镇",
        u"大涌镇",
        u"沙溪镇",
        u"横栏镇",
        u"古镇镇",
        u"小榄镇",
        u"东凤镇",
        u"南头镇",
        u"阜沙镇",
        u"黄圃镇",
        u"东升镇",
        u"五桂山镇"],

    u"潮州市":[
        u"湘桥区",
        u"潮安县（庵埠镇）",
        u"饶平县（黄冈镇）",
        u"枫溪区"],

    u"揭阳市":[
        u"榕城区",
        u"普宁市（流沙北街道）",
        u"揭东县（曲溪镇）",
        u"揭西县（河婆镇）",
        u"惠来县（惠城镇）",
        u"惠来县（惠城镇）",
        u"东山区管理委员会",
        u"揭阳经济开发试验区",
        u"普宁华侨管理区",
        u"大南山华侨管理区"],

    u"云浮市":[
        u"云城区",
        u"罗定市",
        u"云安县（六都镇）",
        u"新兴县（新城镇）",
        u"郁南县（都城镇）"]
}
print "*" * 280
for city, district in districts.items():
    districts = ''
    for d in district:
        districts += d + ','
    print u"%s有下面几个区：%s" % (city,districts)
# To be continued.
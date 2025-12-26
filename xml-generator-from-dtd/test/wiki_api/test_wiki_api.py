import unittest

from src.content.content import ContentType
from src.wiki_api.wiki_api import WikiAPI, Content, Image, XMLDocument


class TestWikiAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = WikiAPI()
        self.article_name = ['Димитър Маджаров', 'Астрономически обект', 'Какшаал Тоо']

    def test_get_text(self):
        result_from_wiki: Content = self.instance.get_page_text(self.article_name[0])
        self.assertEqual(result_from_wiki.content[0][1],
                         'Димитър Петков Маджаров, наричан Маришки, '
                         'е български революционер и войвода на Вътрешната македоно-одринска революционна организация'
                         ' и на Вътрешната тракийска революционна организация.')
        self.assertEqual(result_from_wiki.content[1][1], 'Димитър Маджаров е роден в село Мерхамли '
                                                         '(днес Пеплос, Гърция ), Софлийско. Влиза във ВМОРО'
                                                         ' и се занимава с набиране на оръжие. По време на'
                                                         ' Илинденско-Преображенското въстание е четник в'
                                                         ' Малкотърновско и Лозенградско. През 1907 година е четник'
                                                         ' в агитационната чета на Стамат Икономов в Малкотърновско.')
        self.assertEqual(result_from_wiki.content[2][1],
                         'След Хуриета в 1908 година е сред привържениците на Яне Сандански. '
                         'Основава в Мерхамли клуб на Народната федеративна партия (българска секция).')
        self.assertEqual(result_from_wiki.content[3][1],
                         'При избухването на Балканската война в 1912 година е доброволец в Македоно-одринското'
                         ' опълчение и служи във 2 рота на Лозенградската партизанска дружина на Михаил Герджиков.')
        self.assertEqual(result_from_wiki.content[4][1],
                         'През есента на 1913 година след оттеглянето на българските войски е начело на чета, '
                         'която заедно с четата на Руси Славов, защитава българското население в Дедеагачко'
                         ' и Гюмюрджинско. През септември двете чети разбиват турски конвои между'
                         ' Дедеагач и Фере и спасяват 12000 български бежанци.')
        self.assertEqual(result_from_wiki.content[5][1],
                         'След края на Първата световна война Георги Калоянов, Димитър Маджаров и Петър Чапкънов'
                         ' сформират първата чета на ВТРО за действие в Западна Тракия и Родопския край. Член е на'
                         ' Управителното тяло на ВТРО. Делегат е от Тракийската организация в състава на българската '
                         'делегация на Парижката мирна конференция, която довежда до сключването на Парижкия мирен '
                         'договор от 1947 година.')
        self.assertEqual(result_from_wiki.content[6][1],
                         'Маджаров умира на 25 ноември 1949 г. в град Кърджали.')
        self.assertEqual(result_from_wiki.content[7][1],
                         'В знак на признателност, в 1959 година село Дупница (днес град, до 1912 г.\xa0– Ятаджик)'
                         ', край което през 1913 г. закриляните от четата на Д. Маджаров тракийски бежанци от'
                         ' Беломорието преминават с много жертви граничната тогава р. Арда,'
                         ' е преименувано на Маджарово.')
        self.assertEqual(result_from_wiki.content[8][1],
                         'Морският нос Маджарово на остров Анвер в Антарктика е наименуван в чест на Димитър Маджаров,'
                         ' и във връзка с град Маджарово в Южна България.')

        for i in range(0, len(result_from_wiki.content)):
            self.assertEqual(result_from_wiki.content[i][0], ContentType.TEXT)

    def test_get_text_header(self):
        result_from_wiki: Content = self.instance.get_page_header_text(self.article_name[1])

        self.assertEqual(result_from_wiki.content[0][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[0][1],
                         'Астрономически обект или небесен обект е естествена физическо тяло, асоциация или структура,'
                         ' която съществува в наблюдаваната вселена. В астрономията термините обект и тяло често се'
                         ' използват взаимозаменяемо. Астрономическо тяло или небесно тяло, обаче, е единна,'
                         ' тясно свързана, съседна същност, докато астрономически или небесен обект е сложна, '
                         'по-малко кохезивно свързана структура, която може да се състои от множество тела'
                         ' или дори други обекти с подструктури.')

        self.assertEqual(result_from_wiki.content[1][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[1][1],
                         'Примери за астрономически обекти включват планетарни системи, звездни купове, мъглявини и '
                         'галактики, докато астероиди, спътници, планети и звезди са астрономически тела. Кометите '
                         'могат да бъдат идентифицирани като тела и обекти: те са тела, когато се отнасят до '
                         'замразеното ядро от лед и прах, и обект, когато описва цялата комета с дифузната кома и '
                         'опашката.')

        self.assertEqual(result_from_wiki.content[2][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[2][1],
                         ' Галактики редактиране | редактиране на кода')

        self.assertEqual(result_from_wiki.content[3][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[3][1],
                         'Вселената може да се разглежда като йерархична структура. В най-големите скàли основната '
                         'съставна част на съвкупността е галактиката. Галактиките са организирани в групи и купове, '
                         'често в по-големи свръхкупове, които са нанизани на големи нишки между почти празнини, '
                         'образувайки мрежа, която обхваща наблюдаваната вселена.')

        self.assertEqual(result_from_wiki.content[4][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[4][1],
                         ' Категории, според локация редактиране | редактиране на кода')

        self.assertEqual(result_from_wiki.content[5][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[5][1],
                         ' Източници редактиране | редактиране на кода')

    def test_get_text_header_image(self):
        result_from_wiki: Content = self.instance.get_page_header_text_image(self.article_name[2])

        self.assertEqual(result_from_wiki.content[0][0], ContentType.IMAGE)
        self.assertEqual(result_from_wiki.content[0][1].src,
                         '//upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Jengish_Chokusu_from_BC.jpg/250px'
                         '-Jengish_Chokusu_from_BC.jpg')

        self.assertEqual(result_from_wiki.content[1][0], ContentType.IMAGE)
        self.assertEqual(result_from_wiki.content[1][1].src,
                         '//upload.wikimedia.org/wikipedia/commons/thumb/6/62/'
                         'Relief_Map_of_Kyrgyzstan.png/240px-Relief_Map_of_Kyrgyzstan.png')

        self.assertEqual(result_from_wiki.content[2][0], ContentType.IMAGE)
        self.assertEqual(result_from_wiki.content[2][1].src,
                         '//upload.wikimedia.org/wikipedia/commons/thumb/3/33/Montanya.svg/12px-Montanya.svg.png')

        self.assertEqual(result_from_wiki.content[3][0], ContentType.IMAGE)
        self.assertEqual(result_from_wiki.content[3][1].src,
                         '//upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Flag_of_Kyrgyzstan.svg/23px'
                         '-Flag_of_Kyrgyzstan.svg.png')

        self.assertEqual(result_from_wiki.content[4][0], ContentType.IMAGE)
        self.assertEqual(result_from_wiki.content[4][1].src,
                         '//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People'
                         '%27s_Republic_of_China.svg/23px-Flag_of_the_People%27s_Republic_of_China.svg.png')

        self.assertEqual(result_from_wiki.content[5][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[5][1],
                         'Какшаал Тоо или Кокшаал Тоо, Кокшаалтау (на киргизки : Какшаал тоо ; на руски : Какшаал-Тоо '
                         ') е най-високият и един от най-дългите и мощни планински хребети на Тяншан. Разположен е в '
                         'Киргизстан ( Исъккулска и Наринска област ) и Китай ( Синдзян-уйгурски автономен регион ), '
                         'като по цялото му протежение, по билото преминава границата между двете държави.')

        self.assertEqual(result_from_wiki.content[6][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[6][1],
                         ' Съдържание')

        self.assertEqual(result_from_wiki.content[7][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[7][1],
                         ' Географска характеристика редактиране | редактиране на кода')

        self.assertEqual(result_from_wiki.content[8][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[8][1],
                         'Какшаал Тоо се простира от югозапад на североизток на протежение около 400 km и широчина '
                         'около 54 km, като загражда от югоизток Вътрешен Тяншан. В крайната си североизточна част, '
                         'в района на пик Военни топографи (6870 m) се свързва с Меридионалния хребет на Централен '
                         'Тяншан. Изграден е основно от глинести шисти, пясъчници и варовици, пронизани от гранитни '
                         'интрузии. Средна надморска височина 4000 – 6000 m. Северозападните му (киргизстански) '
                         'склонове са стръмни и се издигат на 1000 – 1500 m над околните съртови равнини, '
                         'а югоизточните (китайски) са полегати и дълги (50 – 70 km), силно разчленени от множество '
                         'речни долини. По гребенът му в средните и североизточните му части има значителни ледници с '
                         'обща площ от 983 km². Югоизточните му склонове са покрити със степна растителност, '
                         'а северозападните – от високопланински пасища и степни ландшафти. Билните части са заети от '
                         'рядка растителност, скали, сипеи и камениста тундра.')

        self.assertEqual(result_from_wiki.content[9][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[9][1],
                         ' Деление редактиране | редактиране на кода')

        self.assertEqual(result_from_wiki.content[10][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[10][1],
                         'На три места хребетът е проломен от каньоновидните долини на реките Сариджаз (Аксу, '
                         'лява съставяща на Тарим ), Узьонгю Кууш (ляв приток на Какшаал) и Какшаал (Кокшаал, '
                         'Таушкандаря, десен приток на Сариджаз ), като по този начин Какшаал Тоо се разделя на '
                         'четири обособени части: Североизточна, Средна Североизточна, Средна Югозападна и Югозападна')

        self.assertEqual(result_from_wiki.content[11][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[11][1],
                         'Североизточната част с дължина около 90 km се простира от пик Военни топографи на '
                         'североизток до каньона на река Сариджаз на югозапад и е най-високият участък в целия '
                         'планински хребет. Тук, в североизточната му част се издига пик Дженгиш Чокусу (Победа, '
                         '7438 m) ( 42°02′03″ с.\xa0ш. 80°07′46″ и.\xa0д. \ufeff / \ufeff 42.034167° с.\xa0ш. '
                         '80.129444° и.\xa0д. 42.034167, 80.129444 ), най-високият връх на Киргизстан и най-високата '
                         'точка на цялата планинска система на Тян Шан. Други по-високи върхове са: Неру (6918 m), '
                         'Еркиндик (Киров, 6073 m), Нансен (5697 m) и др. По северните му склонове се спускат мощни '
                         'ледници (Звьоздочка, Дружба, Дикий и др.), които се вливат в най-големия ледник в Тян Шан – '
                         'Инилчек. От северния му склон води началото си река Куюкан, а от южните – реките Пакаликсу, '
                         'Учказнаку и др., леви притоци на Сариджаз (Аксу).')

        self.assertEqual(result_from_wiki.content[12][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[12][1],
                         'Средната Североизточна част се простира на протежение около 140 km, между проломите на '
                         'реките Сариджаз (Аксу) на североизток и Узьонгю Кууш на югозапад. Максимална височина 5318 '
                         'm ( 41°40′24″ с.\xa0ш. 78°59′10″ и.\xa0д. \ufeff / \ufeff 41.673333° с.\xa0ш. 78.986111° '
                         'и.\xa0д. 41.673333, 78.986111 ). На три места хребета се пресича от високопланински '
                         'проходи: Сауктор (4583 m), Кайче (4463 m) и Бедел (4284 m). И в тази част броят на '
                         'ледниците е значителен. От северните му склонове води началото си река Акшийрак (десен '
                         'приток на Сариджаз ) и множество нейни десни притоци, а от южните му склонове – реките: '
                         'Кучкората (десен приток на Сариджаз ), Кукуртуксу, Кокрюм и др. (леви притоци на Какшаал).')

        self.assertEqual(result_from_wiki.content[13][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[13][1],
                         'Този участък от хребета Какшаал Тоо, за разлика от останалите се простира от изток на запад '
                         'между проломите на реките Узьонгю Кууш и Какшаал (Кокшаал, Таушкандаря), на протежение '
                         'около 160 km и е най-дълъг. Максимална височина пик Данков 5982 m ( 41°03′34″ с.\xa0ш. '
                         '77°41′05″ и.\xa0д. \ufeff / \ufeff 41.059444° с.\xa0ш. 77.684722° и.\xa0д. 41.059444, '
                         '77.684722 ). Други по-значими върхове са пик Космос, (Шмидт, 5940 m), Къзъл Аскер ('
                         'Червеноармеец, 5842 m), пик Корольов (5816 m), пик Алпинист (5462 m) и др. От северните му '
                         'склонове водят началото си реките Узьонгю Кууш и Мюдюрюм (лява съставяща на Какшаал), '
                         'а от южните – малки, къси и бурни леви притоци на Какшаал.')

        self.assertEqual(result_from_wiki.content[14][0], ContentType.TEXT)
        self.assertEqual(result_from_wiki.content[14][1],
                         'Крайната югозападна част на Какшаал Тоо се простира на протежение около 120 km между '
                         'каньона на река Какшаал (Кокшаал, Таушкандаря) на североизток и прохода Уртасу (3965 m) на '
                         'югозапад. Максимална височина 4942 m ( 40°45′44″ с.\xa0ш. 76°35′51″ и.\xa0д. \ufeff / '
                         '\ufeff 40.762222° с.\xa0ш. 76.5975° и.\xa0д. 40.762222, 76.5975 ). В средната част се '
                         'пресича от прохода Кумбел (4012 m). От северните му склонове водят началото си река Аксай ('
                         'дясна съставяща на Какшаал) и нейните десни пиртоци Терек, Къзълсу, Текелик, Курумджук и '
                         'др., а от южните – множество леви притоци на Къзълсу (от басейна на Тарим ).')

        self.assertEqual(result_from_wiki.content[15][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[15][1],
                         ' Топографска карта редактиране | редактиране на кода')

        self.assertEqual(result_from_wiki.content[16][0], ContentType.TITLE)
        self.assertEqual(result_from_wiki.content[16][1],
                         ' Източници редактиране | редактиране на кода')





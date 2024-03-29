# -*- coding: utf-8 -*-

from ConcordanceCrawler.core.logging_crawler import *
import logging
import pprint

crawler = LoggingCrawler()

def detect_sr(s):
    cyrillic = ['а','б','в','г','д','ђ','е','ж','з','и','ј','к','л','љ','м','н','њ','о','п','р','с','т','ћ','у','ф','х','ц','ч','џ','ш']
    CYR_TRESH = 0.85
    
    text = ''.join(x for x in s if x.isalpha())
    counter_other = 0
    N = len(text)
    for c in text:
        if c.lower() not in cyrillic:
            counter_other += 1
            if (counter_other / N) > (1 - CYR_TRESH):
                return False
    return True 
     
def serbian_filter(text):
    if detect_sr(text):
        return True
    return False

def filter_non_serbian_links(link):
    if '.rs' in link and ConcordanceCrawler.filter_link(link):
        return True
    
    logging.debug('link '+link+' was filtered')
    crawler.links_filtered += 1
    return False

crawler.setup(language_filter=serbian_filter, filter_link=filter_non_serbian_links, allow_logging=True)
logging.basicConfig(level=logging.DEBUG, format=LoggingCrawler.log_format, )

nouns = ['година', 'дан', 'време', 'земља', 'председник', 'држава', 'место', 'реч', 'закон', 'право', 'члан', 'пут', 'људи', 'питање', 'страна', 'дело', 'живот', 'начин', 'влада', 'министар', 'град', 'случај', 'кућа', 'милион', 'проблем', 'суд', 'група', 'број', 'избор','финансирање', 'званичник', 'запад', 'странац', 'гора', 'пацијент', 'одржавање', 'стил', 'курс', 'госпођа', 'операција', 'поље', 'јелен', 'традиција', 'пад', 'финансије', 'конвенција', 'насеље', 'појав', 'војислав', 'конкуренција', 'медаља', 'делегација', 'маса', 'седиште', 'зид', 'процедура', 'приштина', 'ризик', 'илић', 'крв', 'краљ', 'одлазак', 'федерација', 'тајна', 'брзина', 'њујорк', 'канцеларија', 'телефон', 'фотографија', 'контакт', 'криминал', 'књижевност', 'допринос', 'куповина', 'генерација', 'земљиште', 'аустрија', 'површина', 'сагласност', 'повећање', 'острво', 'напор', 'функционер', 'категорија', 'корист', 'тип', 'академија', 'градоначелник', 'пријем', 'првак', 'стадион', 'караџић', 'ненад', 'израз', 'брисел', 'карта', 'појединац', 'присуство', 'база', 'датум', 'инвеститор', 'интеграција', 'стратегија', 'сунце', 'настава', 'корупција', 'бугарска', 'стоп', 'говор', 'стварање', 'надлежност', 'отварање', 'терет', 'споменик', 'траг', 'обама', 'промет', 'кампања', 'ваздух', 'хаг', 'интервју', 'сарајево', 'забран', 'критик', 'дејан', 'комитет', 'структура', 'нафта', 'прозор', 'крагујевац', 'редитељ', 'смањење', 'оставка', 'документација', 'осећање', 'демократија', 'павао', 'руководство', 'подела', 'цветковић', 'румунија', 'мађарска', 'технологија', 'пласман', 'просторија', 'списак', 'потез', 'спровођење', 'дуг', 'аеродром', 'застава', 'напредак', 'међувреме', 'штампа', 'светлост', 'губитак', 'дачић', 'вера', 'престоница', 'пас']

N = 100000

with open('concordances.txt', 'a') as fout:

    for _, x in zip(range(N), crawler.yield_concordances(nouns)):
        fout.write(x['concordance'])
        fout.write('\n')
        fout.flush()

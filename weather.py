# https://duckduckgo.com/?q=weather+badalkumbura&t=brave&ia=web
# https://www.google.com/search?q=weather+badalkumbura
# user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36


from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query ="badalkumbura"
    url =f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

    temp = r.html.find('span#wob_tm', first= True).text

    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text

    desc = r.html.find('span#wob_dc', first= True).text

    return temp+" "+unit+" "+desc



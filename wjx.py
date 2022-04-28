from fake_useragent import UserAgent
from selenium import webdriver
import time
import random


def maydo(persent):
    x = random.randint(1, 10000)
    if x <= persent*100:
        return True
    else:
        return False


def danxuan(_list, _str):  # _list各选项概率;_str选项Xpath
    choice = ''
    x = random.randint(1, 10000)
    a = 0
    b = 0
    for i in _list:
        a += i
        b += 1
        if (x <= a*100) or (b == len(_list)):
            choice = _str.replace('$', str(b))
            return choice


def _run():
    # 0
    delay = 0
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')
    # option.add_argument('--headless')
    ua = str(UserAgent().random)
    option.add_argument('--user-agent={}'.format(ua))
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                           'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

    driver.get("https://www.wjx.cn/vm/Q09or3S.aspx")

    def block(_list, _num, _start, _str):  # _list:总概率表,_num:总题数,_start:开始Xpath编号,_str:Xpath
        for i in range(0, _num):
            if(type(_list[i]) == list):  # 处理单选
                choice = danxuan(
                    _list[i], _str.replace('#', str(_start+i)))
                driver.find_element_by_xpath(choice).click()
                time.sleep(delay)
            if(type(_list[i]) == tuple):  # 处理多选
                choice = _str.replace('#', str(_start+i))
                while True:
                    a = 0  # 第几个选项
                    flag = 0  # 选了几个
                    for j in _list[i]:
                        a += 1
                        if maydo(j):
                            flag += 1
                            driver.find_element_by_xpath(
                                choice.replace('$', str(a))).click()
                            # if a == len(_list):
                            #     choice = '/html/body/form/div[5]/div[4]/fieldset/div[11]/div[2]/div[8]/div[2]/input'
                            #     driver.find_element_by_xpath(choice).send_keys(
                            #         random.choice(['没有', '无', '差不多', '外卖方便', '都一样']))
                    if flag > 0:
                        break
                time.sleep(delay)

    time.sleep(delay)
    list1 = [
        [10, 50, 30, 10],  # 1
        [50, 50],  # 2
        [75, 0, 25, 0, 0, 0],  # 3
        [25, 25, 25, 25],  # 4
        [10, 70, 10, 10],  # 5#6
        [50, 50],  # 6#7
        [20, 50, 20, 10],  # 7#8
        [30, 50, 10, 5, 5],  # 8#9
        (50, 50, 70, 50, 50, 0),  # 9#10
        [50, 40, 10],  # 10#11
        [95, 5],  # 11#12
        [40, 50, 5, 5],  # 12#13
        [20, 30, 20, 20, 10],  # 13#15
        (30, 10, 10, 30, 20, 0),  # 14#16
        (70, 50, 50, 40, 50, 50, 60, 20, 20, 0, 3),  # 15#17
        [15, 35, 35, 10, 5],  # 16#18
        [15, 35, 35, 10, 5],  # 17#19
        [15, 35, 35, 10, 5],  # 18#20
        [15, 35, 35, 10, 5],  # 19#21
        [15, 35, 35, 10, 5],  # 20#22
        [20, 30, 35, 10, 5],  # 21#23
        [15, 35, 35, 10, 5],  # 22#24
        [15, 35, 35, 14, 1],  # 23#25
        [15, 35, 35, 10, 5],  # 24#26
        [15, 35, 35, 10, 5],  # 25#28
        [15, 35, 35, 10, 5],  # 26#30
        [15, 35, 35, 10, 5],  # 27#31
        (50, 50, 50, 50, 50, 50, 0),  # 28#32
        (10, 10, 30, 20, 50, 0)  # 29#33
    ]
    try:
        block(list1, 29, 1,
            '/html/body/form/div[5]/div[4]/fieldset/div[#]/div[2]/div[$]/span/a')
    # for i in range(1, 6):
    #     driver.find_element_by_xpath(
    #         '/html/body/form/div[5]/div[4]/fieldset/div[29]/div[2]/div[$]/span/a'.replace('$', str(i))).click()
        driver.find_element_by_xpath('/html/body/form/div[5]/div[4]/fieldset/div[30]/div[2]/input').send_keys(
            random.choice(["."]))
    except:
        pass
    # time.sleep(10000)
    # 提交
    choice = '/html/body/form/div[5]/div[9]/div[3]/div[1]/div'
    driver.find_element_by_xpath(choice).click()
    time.sleep(delay+1)
    choice = '/html/body/div[8]/div[2]/div[2]/button'
    try:
        driver.find_element_by_xpath(choice).click()
    except:
        pass

    choice = random.choice(['/html/body/form/div[5]/div[9]/div[2]/div/div/div/div[1]/div[2]/div[1]',
                           '/html/body/form/div[5]/div[9]/div[2]/div/div/div/div[1]/div[2]/div[2]'])
    try:
        driver.find_element_by_xpath(choice).click()
    except:
        pass

    time.sleep(3)


def main():
    _run()


if __name__ == "__main__":
    main()

from fake_useragent import UserAgent
from selenium import webdriver
import time
import random

url = "https://www.wjx.cn/vj/eYzdova.aspx"
xpath = "/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[#]/div[2]/ul/li[$]/a"
input_xpath = "/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[#]/div[2]/ul/li[$]/input[2]"
list1 = [
    [0, 0, 0, [0, ["hello"]]],  # 1
    (50, 50, 50, [100, ["hello"]], [100, ["hello"]], [100, ["hello"]]),  # 2
]


def maydo(persent):
    x = random.randint(1, 10000)
    if x <= persent*100:
        return True
    else:
        return False


def _run():
    delay = 0
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')
    # option.add_argument('--headless')
    ua = str(UserAgent().random)
    option.add_argument('--user-agent={}'.format(ua))
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                           'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

    driver.get(url)

    # _list:总概率表,_start:第一题Xpath题号,_xpath:选项,input_xpath:输入框
    def block(_list, _start, _xpath, input_xpath):
        sum_list = len(_list)  # 总题数
        th = _start - 1  # 题目xpath编号记录
        for item in _list:
            th += 1
            print(th)
            if(type(item) == list):  # 处理单选
                x = random.randint(1, 10000)  # 产生随机数
                a = 0  # 概率累计
                b = 0  # 选项序号
                for j in item:
                    b += 1
                    if(type(j) == list):
                        a += j[0]
                    else:
                        a += j
                    if (x <= a*100) or (b == len(item)):
                        choice = _xpath.replace(
                            '#', str(th)).replace('$', str(b))
                        driver.find_element_by_xpath(choice).click()
                        if(type(j) == list):
                            pass
                        else:
                            break
                        time.sleep(delay)
                        if(type(j) == list):
                            choice = input_xpath.replace(
                                '#', str(th)).replace('$', str(b))
                            driver.find_element_by_xpath(
                                choice).send_keys(random.choice(j[1]))

            elif(type(item) == tuple):  # 处理多选
                a = 0  # 概率
                b = 0  # 选项序号
                for j in item:
                    b += 1
                    if(type(j) == list):
                        a = j[0]
                    else:
                        a = j
                    if maydo(a):
                        choice = _xpath.replace(
                            '#', str(th)).replace('$', str(b))
                        driver.find_element_by_xpath(choice).click()
                        if(type(j) == list):
                            pass
                        else:
                            continue
                        time.sleep(delay)
                        if(type(j) == list):
                            choice = input_xpath.replace(
                                '#', str(th)).replace('$', str(b))
                            driver.find_element_by_xpath(
                                choice).send_keys(random.choice(j[1]))
    time.sleep(delay)

    try:
        block(list1, 1, xpath, input_xpath)
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

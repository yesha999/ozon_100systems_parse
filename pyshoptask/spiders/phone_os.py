import time

import scrapy
from scrapy.http import HtmlResponse, Request
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome, ActionChains, ChromeOptions
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


class PhoneOsSpider(scrapy.Spider):
    name = 'phone_os'
    settings = get_project_settings()
    driver_path = settings.get("CHROME_DRIVER_PATH")
    options = ChromeOptions()
    # options.add_argument(settings.get("USER_AGENT"))
    options.add_argument("--disable-blink-features")

    def start_requests(self):
        urls = []
        for page in range(1, 5):
            driver = Chrome(executable_path=self.driver_path, options=self.options)
            driver.get(f"https://www.ozon.ru/category/smartfony-15502/?page={page}&sorting=rating")

            scroll_origin = ScrollOrigin.from_viewport(10, 10)
            ActionChains(driver) \
                .scroll_from_origin(scroll_origin, 0, 10000) \
                .perform()

            time.sleep(6)
            for phone_num in range(2, 37):
                xpath = f'//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[{phone_num}]/div[2]/div/a'
                link_element = driver.find_elements(By.XPATH, xpath)
                if link_element:
                    href = link_element[0].get_attribute("href")
                    urls.append(href)
            driver.quit()

        for url in urls:
            # yield Request(url=url, headers=self.settings.get("HEADERS"), cookies=self.settings.get("COOKIES"),
            #               meta={'dont_merge_cookies': True})
            # На этом этапе происходила ошибка 403 Crawled,
            # какие бы куки, хэдеры и другие параметры не вводил и какие бы прокси (бесплатные) не использовал.
            # На озоне стоит защита cloudflare, а библиотеку, которая ее обходила, автор удалил,
            # среди решений, которые работают, использовал драйвер, но при таком раскладе нецелесообразно
            # использовать Scrapy, так как рушится его концепция в получении request в start_requests

            driver = Chrome(executable_path=self.driver_path, options=self.options)
            driver.get(url)

            scroll_origin = ScrollOrigin.from_viewport(10, 10)
            ActionChains(driver) \
                .scroll_from_origin(scroll_origin, 0, 10000) \
                .perform()
            time.sleep(2)
            link_element = driver.find_elements(By.TAG_NAME, "dd")
            for link in link_element:
                if link.text.startswith("Android ") or link.text.startswith("iOS "):  # На некоторых смартфонах,
                    # например, Huawei стоит ОС Harmony, но об этом нет информации в характеристиках,
                    # поэтому, чтобы получить 100 систем, нужно парсить больше смартфонов
                    with open("operating_systems.txt", "a") as f:
                        f.write(f'{link.text}\n')

            driver.quit()

    def parse(self, response: HtmlResponse, **kwargs):
        pass
    #     elements = response.css('dd::text').getall()
    #     for element in elements:
    #         if element.text.startswith("Android ") or element.text.startswith("iOS "):
    #             with open("operations_systems.txt", "a") as f:
    #                 f.write(f'{element.text}\n')

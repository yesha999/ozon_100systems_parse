# Scrapy settings for pyshoptask project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os.path

BOT_NAME = 'pyshoptask'

SPIDER_MODULES = ['pyshoptask.spiders']
NEWSPIDER_MODULE = 'pyshoptask.spiders'
CHROME_DRIVER_PATH = os.path.abspath("chromedriver.exe")

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'pyshoptask.middlewares.PyshoptaskSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'pyshoptask.middlewares.PyshoptaskDownloaderMiddleware': 543,
# # }
# ROTATING_PROXY_LIST_PATH = os.path.abspath('proxies.txt')
# DOWNLOADER_MIDDLEWARES = {
#     # ...
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
#     # ...
# }
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'pyshoptask.pipelines.PyshoptaskPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://www.ozon.ru/category/smartfony-15502/",
    "sec-ch-ua": 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": 1,
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

COOKIES = {"__Secure-user-id": 0, "__Secure-ab-group": 96, "__Secure-ext_xcid": "47f71f61285c1f55727af62de22a9990",
           "_ga": "GA1.1.1149896790.1667633965", "tmr_lvid": "a40872c86ae55e8b070a863fd76dc8ec",
           "tmr_lvidTS": "1667633965975",
           "cnt_of_orders": "0", "isBuyer": "0", "__exponea_etc__": "ef1a2be1-468d-4538-acb7-38d243e5b874",
           "__Secure-access-token": "3.0.w2RTKhQFQQucyMEFGfMv3w.96.l8cMBQAAAABjZhMjDDAPkKN3ZWKgAICQoA..20221106114519.oqJ3XKKIsNewXxq8qaXu0PXvGtMzWG8HGE22ho9TO94",
           "__Secure-refresh-token": "3.0.w2RTKhQFQQucyMEFGfMv3w.96.l8cMBQAAAABjZhMjDDAPkKN3ZWKgAICQoA..20221106114519.CR1IWVjuLmNei23oS_t11HNOe94_S4IGE_7OiE2T3q4",
           "AREA_ID": 9796, "xcid": "9b6dc9fde499fbb573c7ec4bda2655aa",
           "rfuid": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwtMjg3MDM2NTYzLC0xLDk4MDIxNjIxNCxXM3NpYm1GdFpTSTZJbEJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFsSUZCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxcGRXMGdVRVJHSUZacFpYZGxjaUlzSW1SbGMyTnlhWEIwYVc5dUlqb2lVRzl5ZEdGaWJHVWdSRzlqZFcxbGJuUWdSbTl5YldGMElpd2liV2x0WlZSNWNHVnpJanBiZXlKMGVYQmxJam9pWVhCd2JHbGpZWFJwYjI0dmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmU3g3SW5SNWNHVWlPaUowWlhoMEwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjFkZlN4N0ltNWhiV1VpT2lKTmFXTnliM052Wm5RZ1JXUm5aU0JRUkVZZ1ZtbGxkMlZ5SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpRYjNKMFlXSnNaU0JFYjJOMWJXVnVkQ0JHYjNKdFlYUWlMQ0p0YVcxbFZIbHdaWE1pT2x0N0luUjVjR1VpT2lKaGNIQnNhV05oZEdsdmJpOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5TEhzaWRIbHdaU0k2SW5SbGVIUXZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlYxOUxIc2libUZ0WlNJNklsZGxZa3RwZENCaWRXbHNkQzFwYmlCUVJFWWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDFkLFd5SnlkUzFTVlNKZCwwLDEsMCwyNCwyMzc0MTU5MzAsOCwyMjcxMjY1MjAsMSwxLDAsLTQ5MTI3NTUyMyxHb29nbGUgSW5jLk5ldHNjYXBlR2Vja29XaW4zMjUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIFNhZmFyaS81MzcuMzYyMDAzMDEwN01vemlsbGEsV3lKN1hDSmhjSEJjSWpwN1hDSnBjMGx1YzNSaGJHeGxaRndpT21aaGJITmxMRndpU1c1emRHRnNiRk4wWVhSbFhDSTZlMXdpUkVsVFFVSk1SVVJjSWpwY0ltUnBjMkZpYkdWa1hDSXNYQ0pKVGxOVVFVeE1SVVJjSWpwY0ltbHVjM1JoYkd4bFpGd2lMRndpVGs5VVgwbE9VMVJCVEV4RlJGd2lPbHdpYm05MFgybHVjM1JoYkd4bFpGd2lmU3hjSWxKMWJtNXBibWRUZEdGMFpWd2lPbnRjSWtOQlRrNVBWRjlTVlU1Y0lqcGNJbU5oYm01dmRGOXlkVzVjSWl4Y0lsSkZRVVJaWDFSUFgxSlZUbHdpT2x3aWNtVmhaSGxmZEc5ZmNuVnVYQ0lzWENKU1ZVNU9TVTVIWENJNlhDSnlkVzV1YVc1blhDSjlmWDBpWFE9PSw2NSwtMTI4NTU1MTMsMSwxLC0xLDE2OTk5NTQ4ODcsMTY5OTk1NDg4NywzMzYwMDc5MzMsMTI:",
           "__cf_bm": "IdKtRNf0b8ynxJRz.QhjLp5gPynpP2kqwwnhgwOv.7k-1667727921-0-ASxCNFjvlvfkOm4lW+NJo/5mczccl9zPEFfSw3U1XkZGtb7vRK0SqWXsi+44HDi7UORwr/GndVtbOWPwliVgoh78iYsg9rj/RK5mMVEfEdXyykujJNhK8oNAKxy5LpLm623qKdLvWHYcEVj+t08RwDmv1GtkyIVdqhf3+7hH7OoV",
           "__exponea_time2__": "-0.10323572158813477", "guest": "true",
           "_ga_JNVTMNXQ6F": "GS1.1.1667727922.3.1.1667727943.39.0.0", "tmr_detect": "0%7C1667727945963",
           "tmr_reqNum": 34}

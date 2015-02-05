# -*- coding: utf-8 -*-

# Scrapy settings for bcra project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bcra'

SPIDER_MODULES = ['bcra.spiders']
NEWSPIDER_MODULE = 'bcra.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bcra (+http://www.yourdomain.com)'

AUTOTHROTTLE_ENABLED=True
CONCURRENT_REQUESTS_PER_DOMAIN=1

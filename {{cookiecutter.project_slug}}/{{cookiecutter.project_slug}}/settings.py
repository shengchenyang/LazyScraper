# Scrapy settings for {{ cookiecutter.project_slug }} project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from pathlib import Path

from loguru import logger

BOT_NAME = "{{ cookiecutter.project_slug }}"

SPIDER_MODULES = ["{{ cookiecutter.project_slug }}.spiders"]
NEWSPIDER_MODULE = "{{ cookiecutter.project_slug }}.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Set .conf file path. Same as library default, commentable
_ = Path(__file__).parent
VIT_DIR = _ / "VIT"

# Log configuration example
LOG_LEVEL = "ERROR"
LOG_FILE = _ / "logs/{{ cookiecutter.project_slug.lower() }}.log"
logger.add(
    _ / "logs/error.log",
    level="ERROR",
    rotation="1 week",
    retention="7 days",
    enqueue=True,
)

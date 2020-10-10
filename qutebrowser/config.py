from qutebrowser.config.configfiles import ConfigAPI
from qutebrowser.config.config import ConfigContainer

import sys, os

config = config
c = c

config.bind('Alt-Tab', 'tab-next')
config.bind('Backspace', 'back')

c.url.default_page = "http://pi:8888"
c.input.insert_mode.auto_load = True
c.content.proxy = "http://192.168.178.64:3128"
c.colors.webpage.bg = "#fefefe"
c.content.javascript.enabled = True
c.fonts.default_family = 'Roboto Mono Light for Powerline'
c.fonts.web.family.standard = 'Roboto Mono Light for Powerline'
c.scrolling.smooth = True

c.url.searchengines = { 'DEFAULT':'http://pi:8888/?q={}' }
c.url.start_pages = 'http://pi:8888'

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The Asshole'
SITENAME = u"CRW.dog:  Hey assholes!"
SITEURL = 'http://crw.dog'
SITESUBTITLE = 'Event info and resources for assholes everywhere'

PATH = 'content'

THEME = 'theme/'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = ()

# Social widget

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

# For when I have one
# SITELOGO = 'images/my_site_logo.png'

# For when I have one
# FAVICON = 'images/favicon.png'

HIDE_SITENAME = True

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Share
SHARE = True
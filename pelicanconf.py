AUTHOR = 'R. Kyle Norris'
SITENAME = 'Portfolio: R. Kyle Norris'
SITEURL = '.'
RELATIVE_URLS = True

PATH = "content"
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Theme settings
THEME = 'theme'  # We will move your CSS/HTML here

# Static paths
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Display pages in menu
DISPLAY_PAGES_ON_MENU = True

# pelicanconf.py

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {'raw_html': True},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

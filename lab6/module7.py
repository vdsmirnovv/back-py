import locale

def set_locale(language_code):
    locale.setlocale(locale.LC_ALL, language_code)
    return locale.getlocale()

def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.currency(value, grouping=True)

def locale_info():
    return locale.localeconv()